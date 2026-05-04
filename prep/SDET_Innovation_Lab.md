# SDET Innovation Lab — 10 Custom Tools That Solve Real Problems

**Purpose:** Build tools that demonstrate engineering thinking, not wrapper scripts. Each tool here solves a genuine QA bottleneck with non-trivial logic.  
**Companion docs:** `SDET_Portfolio_Blueprint.md` (how to showcase them), `Master_SDET_Implementation_Plan.md` (skills to build them).  
**Portfolio strategy:** Build 3–5 of these well. Put them in a single `sdet-tools` monorepo or as standalone repos. Quality over quantity.

---

## How Each Tool Is Structured

Every tool follows the same documentation pattern:

1. **The Problem** — A real pain point SDETs face daily.
2. **Why Existing Solutions Fall Short** — Why you can't just `pip install` something.
3. **The Core Logic** — The algorithm or approach, explained so you understand it before coding.
4. **Architecture** — How to structure the code.
5. **Tech Stack** — Libraries and why each is chosen.
6. **Zero-Cost Hosting** — How to deploy for free.
7. **Complexity Level** — So you can sequence your builds.
8. **Interview Value** — What this tool proves to a hiring manager.

---

## Tool 1: API Contract Drift Detector

### The Problem

Your API tests validate response *values*, but not response *shape*. A backend developer adds a new required field, deprecates an old one, or changes a type from `string` to `int`. Your tests still pass because they never checked the schema. Two weeks later, a consumer breaks in production.

### Why Existing Solutions Fall Short

Pact and Schemathesis test against a *spec*. But many teams don't maintain their OpenAPI specs — the code drifts from the spec. This tool compares **actual API responses** against a **baseline snapshot**, detecting structural changes without needing a spec.

### The Core Logic

1. **Baseline capture:** Make API calls, record the JSON response structure (keys, types, nesting depth) — not the values. Store as a fingerprint.
2. **Recursive schema extraction:** Walk the JSON tree recursively. For each node, record: `{path: "user.address.city", type: "string", nullable: false, is_array: false}`. Arrays are sampled (first element defines the schema).
3. **Diff engine:** Compare current response fingerprint against baseline. Detect: new fields (additive, usually safe), removed fields (breaking), type changes (breaking), nullability changes (potentially breaking).
4. **Severity classification:** Additive changes = INFO. Removed/type changes = WARNING. Required field removal = CRITICAL.

### Architecture

```
contract-drift-detector/
├── src/
│   ├── schema_extractor.py     # Recursive JSON → schema fingerprint
│   ├── diff_engine.py          # Compare two fingerprints
│   ├── severity_classifier.py  # Classify each diff
│   ├── reporter.py             # Generate Markdown/HTML report
│   └── cli.py                  # CLI entry point
├── baselines/                  # Stored schema fingerprints (JSON)
├── tests/
│   ├── test_extractor.py
│   └── test_diff_engine.py
└── pyproject.toml
```

### Tech Stack

| Component | Library | Why |
|-----------|---------|-----|
| HTTP | `httpx` | Async support for parallel endpoint scanning |
| CLI | `typer` | Type-hinted CLI with auto-generated help |
| Reporting | `jinja2` | Templated HTML/Markdown reports |
| Diffing | Custom (stdlib) | `deepdiff` is too generic; you need schema-level, not value-level |

### Zero-Cost Hosting

- **GitHub Actions scheduled workflow:** Run nightly against staging. Commit the baseline diffs as PR comments using `gh api`.
- **GitHub Pages:** Publish the HTML report to `gh-pages` branch. Free static hosting.

### Complexity Level: Medium

**Key algorithms to learn:** Recursive tree traversal, structural diffing, schema inference from samples.

### Interview Value

Proves: recursive algorithms, schema design, API contract understanding, CI integration thinking.

---

## Tool 2: Synthetic Test Data Generator (API-Aware)

### The Problem

You need test data that is:
- **Realistic** (not `"test123"`, `"aaa@bbb.com"`)
- **Relationally consistent** (a user's `org_id` must reference a real org)
- **API-aware** (generated data must pass the API's own validation — correct email format, password complexity, field lengths)

Faker generates random data. Factory Boy generates structured data. Neither reads your API spec to know what's valid.

### Why Existing Solutions Fall Short

Faker doesn't know your API's password policy is `min 12 chars, 1 uppercase, 1 number, 1 special`. Factory Boy doesn't know your `username` field has a `max_length: 64` constraint. You end up hardcoding rules that drift from the API.

### The Core Logic

1. **Schema ingestion:** Parse an OpenAPI spec (or JSON Schema) to extract field constraints: `type`, `format`, `minLength`, `maxLength`, `pattern` (regex), `enum`, `required`.
2. **Constraint-aware generation:** For each field, select a Faker provider that satisfies all constraints. `string + format:email + maxLength:100` → `fake.email()` truncated to 100 chars. `string + pattern:^[A-Z]{3}-\d{4}$` → `rstr.xeger()` (regex-based string generation).
3. **Relational graph:** Parse `$ref` relationships in the spec. If `User` has `org_id: {$ref: '#/components/schemas/Organization/properties/id'}`, generate `Organization` first, then use its `id` for `User.org_id`.
4. **Topological generation:** Sort entities by dependency (topological sort), generate parents before children.

### Architecture

```
synthetic-data-gen/
├── src/
│   ├── schema_parser.py        # OpenAPI/JSON Schema → field constraints
│   ├── constraint_resolver.py  # Map constraints → Faker providers
│   ├── dependency_graph.py     # Build entity relationship graph
│   ├── generator.py            # Topological generation engine
│   ├── exporters/
│   │   ├── json_exporter.py
│   │   ├── csv_exporter.py
│   │   └── sql_exporter.py     # INSERT statements
│   └── cli.py
├── tests/
└── pyproject.toml
```

### Tech Stack

| Component | Library | Why |
|-----------|---------|-----|
| Schema parsing | `openapi-spec-validator` + `jsonref` | Resolve `$ref`, validate spec |
| Data generation | `faker` + `rstr` | Faker for common types, rstr for regex patterns |
| Graph | `networkx` | Topological sort for dependency resolution |
| CLI | `typer` | |
| Export | `jinja2` (for SQL templates) | |

### Zero-Cost Hosting

- **CLI tool** distributed via PyPI (free) or GitHub Releases.
- **GitHub Actions:** Workflow that generates a fresh data set on schedule and commits to a `test-data` branch.

### Complexity Level: Hard

**Key algorithms to learn:** Topological sort, constraint satisfaction, schema parsing, regex-based generation.

### Interview Value

Proves: graph algorithms, OpenAPI understanding, data engineering, constraint-aware design.

---

## Tool 3: Flaky Test Forensic Analyzer

### The Problem

Your test suite has 15% flaky tests. You know *which* tests are flaky (they sometimes pass, sometimes fail). You don't know *why*. Is it timing? Network? Test ordering? Shared state? Data pollution?

### Why Existing Solutions Fall Short

`pytest-rerunfailures` retries tests but doesn't analyze root causes. Datadog CI Visibility shows flaky tests but doesn't correlate with *what changed* between the pass and the fail.

### The Core Logic

1. **Multi-run execution:** Run the test suite N times (e.g., 10), capturing JUnit XML results for each run.
2. **Instability scoring:** For each test, calculate: `instability = (distinct_outcomes / total_runs)`. A test that passes 10/10 times has instability 0. A test that passes 5/10 has instability 0.5.
3. **Correlation analysis:**
   - **Time correlation:** Do failures cluster at specific times? (Suggests timeout/rate-limit issues.)
   - **Order correlation:** Does test X always fail when test Y runs before it? (Suggests shared state pollution.) Use permutation testing: run with `--randomly-seed` and correlate failure with predecessor.
   - **Duration correlation:** Is the test faster when it passes and slower when it fails? (Suggests timing/race condition.)
   - **Error pattern clustering:** Group failures by error message similarity (Levenshtein distance). Are all flaky tests failing with the same error?
4. **Root cause classification:** Based on correlations, classify each flaky test: `timing`, `shared_state`, `network`, `data_dependency`, `unknown`.
5. **Report generation:** Markdown report with: flaky tests ranked by instability, probable root cause, correlation evidence, suggested fix.

### Architecture

```
flaky-forensics/
├── src/
│   ├── runner.py               # Execute test suite N times
│   ├── result_parser.py        # Parse JUnit XML results
│   ├── instability_scorer.py   # Calculate flakiness metrics
│   ├── correlators/
│   │   ├── time_correlator.py
│   │   ├── order_correlator.py
│   │   ├── duration_correlator.py
│   │   └── error_clusterer.py
│   ├── classifier.py           # Classify root cause
│   └── reporter.py             # Generate Markdown report
├── tests/
└── pyproject.toml
```

### Tech Stack

| Component | Library | Why |
|-----------|---------|-----|
| XML parsing | `lxml` or `junitparser` | Parse JUnit XML efficiently |
| String similarity | `python-Levenshtein` or `rapidfuzz` | Cluster error messages |
| Statistics | `statistics` (stdlib) | Correlation calculations |
| Reporting | `jinja2` | Templated reports |
| CLI | `typer` | |

### Zero-Cost Hosting

- **GitHub Actions workflow:** Run nightly, commit the flaky report as a GitHub wiki page or `gh-pages` site.
- **GitHub Issues integration:** Auto-create issues for newly detected flaky tests using `gh issue create`.

### Complexity Level: Hard

**Key algorithms to learn:** Statistical correlation, string similarity clustering, permutation analysis.

### Interview Value

Proves: statistical thinking, root cause analysis methodology, understanding of flaky test taxonomy.

---

## Tool 4: Environment Health Monitor

### The Problem

Before running tests, you need to know: is the environment healthy? Is the API up? Is the database reachable? Are required services running? Currently, tests fail after 5 minutes of setup only to discover the environment was down.

### Why Existing Solutions Fall Short

Uptime monitoring tools (Pingdom, UptimeRobot) check if a URL returns 200. But "healthy for testing" means more: the API returns expected schema, the database has the expected seed data, the auth service issues valid tokens, response times are within acceptable range.

### The Core Logic

1. **Health check definition:** YAML config file defines checks. Each check has: name, type (http, tcp, dns, db_query), target, expected result, timeout, severity (critical, warning, info).
2. **Async execution:** Run all checks concurrently using `asyncio` + `aiohttp`. A 10-check suite with 5s timeouts completes in 5s, not 50s.
3. **Result aggregation:** Each check returns `{name, status: pass|fail|warn, latency_ms, detail}`. Aggregate into overall health score.
4. **Dependency-aware assessment:** If the auth service is down (critical), mark all API checks as "blocked" rather than "failed" — they couldn't have been tested meaningfully.
5. **Trend tracking:** Store results in a local SQLite database. Detect degradation patterns: "API latency has increased 300% over the last 7 days."

### Architecture

```
env-health-monitor/
├── src/
│   ├── checks/
│   │   ├── http_check.py       # HTTP endpoint health
│   │   ├── tcp_check.py        # Port reachability
│   │   ├── dns_check.py        # DNS resolution
│   │   └── db_check.py         # Database query execution
│   ├── config_loader.py        # Parse YAML health config
│   ├── executor.py             # Async check execution
│   ├── aggregator.py           # Result aggregation + scoring
│   ├── trend_tracker.py        # SQLite-based trend storage
│   └── cli.py
├── config/
│   ├── staging.yaml            # Health checks for staging
│   └── production.yaml         # Health checks for production
├── tests/
└── pyproject.toml
```

### Tech Stack

| Component | Library | Why |
|-----------|---------|-----|
| Async HTTP | `aiohttp` | Concurrent health checks |
| TCP checks | `asyncio.open_connection` (stdlib) | Raw socket check |
| DNS | `aiodns` | Async DNS resolution |
| Database | `aiosqlite` | Async SQLite for trend storage |
| Config | `pyyaml` + `pydantic` | Typed config loading |
| CLI | `typer` | |
| Reporting | `rich` | Beautiful terminal output with tables and colors |

### Zero-Cost Hosting

- **GitHub Actions pre-job step:** Run before tests in CI. If environment is unhealthy, skip tests and report.
- **Render cron job (free tier):** Run every 5 minutes, push results to a status page on GitHub Pages.

### Complexity Level: Medium

**Key algorithms to learn:** Async programming, dependency graph analysis, time-series trend detection.

### Interview Value

Proves: async Python, infrastructure awareness, proactive failure prevention thinking.

---

## Tool 5: API Mock Server Generator

### The Problem

You need to test a frontend or a service that depends on 5 external APIs. Those APIs are slow, rate-limited, or unavailable in your test environment. You need mocks, but writing mock responses manually is tedious and they drift from the real API.

### Why Existing Solutions Fall Short

WireMock is Java-based (complex setup for Python teams). `responses` library mocks at the Python process level (doesn't help frontend tests). Postman mocks require a paid account for persistence.

### The Core Logic

1. **Recording mode:** Proxy real API traffic, capture request-response pairs. For each pair, extract: method, path pattern (replace IDs with `{id}`), query params, request body schema, response body, status code, headers.
2. **Scenario generation:** Group captured pairs by endpoint. Generate a "happy path" scenario (200 responses) and "error scenarios" (4xx, 5xx) per endpoint.
3. **Stateful mocking:** Track state across requests. POST `/users` adds a user to in-memory store. GET `/users/{id}` retrieves it. DELETE `/users/{id}` removes it. The mock server behaves like a real (simplified) API.
4. **FastAPI server generation:** Generate a FastAPI application with routes matching the captured API, returning recorded or stateful responses.
5. **Spec-first mode (alternative):** Parse an OpenAPI spec and generate the server from the spec instead of recorded traffic.

### Architecture

```
mock-server-gen/
├── src/
│   ├── recorder/
│   │   ├── proxy.py            # mitmproxy-based traffic capture
│   │   └── normalizer.py       # Normalize paths (replace IDs with params)
│   ├── generator/
│   │   ├── route_builder.py    # Generate FastAPI routes
│   │   ├── state_engine.py     # In-memory stateful store
│   │   └── response_builder.py # Build response from template
│   ├── spec_parser.py          # OpenAPI → routes (alternative mode)
│   └── cli.py
├── templates/                  # Jinja2 templates for generated code
├── tests/
└── pyproject.toml
```

### Tech Stack

| Component | Library | Why |
|-----------|---------|-----|
| Mock server | `fastapi` + `uvicorn` | Fast, typed, auto-documented |
| Recording | `mitmproxy` (Python API) | Programmable proxy |
| Code generation | `jinja2` | Generate Python files from templates |
| Spec parsing | `openapi-spec-validator` | Parse OpenAPI specs |
| CLI | `typer` | |

### Zero-Cost Hosting

- **Render free tier:** Deploy generated FastAPI mock server (sleeps after 15 min inactivity, wakes on request).
- **Docker:** Ship as a Docker image for CI use.

### Complexity Level: Hard

**Key algorithms to learn:** HTTP proxy interception, URL pattern normalization (regex), stateful mock design, code generation.

### Interview Value

Proves: service virtualization understanding, proxy/network knowledge, code generation, FastAPI proficiency.

---

## Tool 6: Test Impact Analyzer

### The Problem

Your monorepo has 500 tests and 200 source files. A developer changes one file. Running all 500 tests takes 30 minutes. Which tests actually need to run for this change?

### Why Existing Solutions Fall Short

`dorny/paths-filter` in GitHub Actions checks file paths, but it's coarse: "if anything in `src/` changed, run all tests." It doesn't understand which tests *actually import* the changed module.

### The Core Logic

1. **Import graph construction:** Parse all Python files using `ast` module. For each file, extract its imports (`import X`, `from X import Y`). Build a directed graph: `module_A → module_B` means A imports B.
2. **Reverse dependency mapping:** Invert the graph. For `module_B`, its reverse dependencies are all modules that import it (directly or transitively).
3. **Change detection:** Use `git diff --name-only HEAD~1` to identify changed files.
4. **Impact calculation:** For each changed file, walk the reverse dependency graph to find all affected test files (files in `tests/` that transitively depend on the changed module).
5. **Output:** List of test files to run, passable to `pytest` as arguments.

### Architecture

```
test-impact-analyzer/
├── src/
│   ├── ast_parser.py           # Parse imports from Python files
│   ├── graph_builder.py        # Build import dependency graph
│   ├── impact_calculator.py    # Reverse walk from changed files to tests
│   ├── git_differ.py           # Get changed files from git
│   └── cli.py
├── tests/
└── pyproject.toml
```

### Tech Stack

| Component | Library | Why |
|-----------|---------|-----|
| AST parsing | `ast` (stdlib) | Parse Python imports without executing |
| Graph | `networkx` | Graph operations, reverse traversal |
| Git | `subprocess` calling `git` | Lightweight, no library needed |
| CLI | `typer` | |

### Zero-Cost Hosting

- **GitHub Actions composite action:** Package as a custom action. Others can use it in their workflows.
- **PyPI:** Publish as `pip install test-impact-analyzer`, run as `tia --changed $(git diff --name-only HEAD~1)`.

### Complexity Level: Medium-Hard

**Key algorithms to learn:** AST parsing, directed graph traversal, transitive closure computation.

### Interview Value

Proves: AST/metaprogramming knowledge, graph algorithms, CI optimization thinking, understanding of build systems.

---

## Tool 7: Log Pattern Anomaly Detector

### The Problem

After a test run, you have 10,000 lines of application logs. Somewhere in those logs are clues about why 3 tests failed. Finding them manually is like searching for a needle in a haystack.

### Why Existing Solutions Fall Short

`grep "ERROR"` finds explicit errors but misses: unexpected warnings that precede failures, unusual patterns (a normally-fast query suddenly taking 10s), missing expected log lines (a service didn't start).

### The Core Logic

1. **Log parsing:** Parse semi-structured logs into events: `{timestamp, level, service, message, metadata}`. Support common formats (JSON logs, syslog, Python logging format) via configurable parsers.
2. **Baseline profiling:** From a "known good" log, build a statistical profile: which log patterns appear, at what frequency, in what order.
3. **Anomaly detection (frequency):** Compare current run against baseline. If `"DB connection pool exhausted"` appears 50 times vs baseline of 0, flag it.
4. **Anomaly detection (sequence):** If the baseline shows `"Service started" → "Health check passed" → "Ready"` but the current log shows `"Service started" → "Health check failed" → "Retry"`, flag the sequence deviation.
5. **Anomaly detection (timing):** If `"Query executed"` normally takes <100ms between log lines but now shows 5s gaps, flag the latency anomaly.
6. **Correlation with test failures:** Cross-reference anomalous log timestamps with test failure timestamps. If an anomaly occurred 2 seconds before a test failure, highlight the probable connection.

### Architecture

```
log-anomaly-detector/
├── src/
│   ├── parsers/
│   │   ├── json_parser.py
│   │   ├── syslog_parser.py
│   │   └── python_parser.py
│   ├── baseline_profiler.py    # Build statistical baseline
│   ├── frequency_analyzer.py   # Detect frequency anomalies
│   ├── sequence_analyzer.py    # Detect sequence anomalies
│   ├── timing_analyzer.py      # Detect timing anomalies
│   ├── correlator.py           # Correlate with test results
│   └── cli.py
├── tests/
└── pyproject.toml
```

### Tech Stack

| Component | Library | Why |
|-----------|---------|-----|
| Log parsing | `regex` (faster than `re`) | Complex log format parsing |
| Statistics | `statistics` + `numpy` (optional) | Mean, std, z-score for anomaly |
| Reporting | `rich` + `jinja2` | Terminal + HTML output |
| CLI | `typer` | |

### Zero-Cost Hosting

- **GitHub Actions post-test step:** Parse logs after test execution, attach anomaly report as a PR comment.
- **CLI tool:** Distributed via PyPI.

### Complexity Level: Hard

**Key algorithms to learn:** Statistical anomaly detection (z-scores), sequence alignment, log parsing with regex, time-series analysis.

### Interview Value

Proves: observability engineering, statistical analysis, log management, root cause analysis methodology.

---

## Tool 8: Test Coverage Gap Finder

### The Problem

You have 100 API endpoints. You have 200 tests. Are all endpoints covered? Which endpoints have no tests? Which have only "happy path" tests but no error cases? Code coverage tools measure *line* coverage — they don't tell you about *scenario* coverage.

### Why Existing Solutions Fall Short

Code coverage (`coverage.py`) measures which lines of *your test code* execute — not which API endpoints or scenarios are tested. It can't tell you "there's no test for DELETE /users/{id} with an invalid ID."

### The Core Logic

1. **Endpoint inventory:** Parse the OpenAPI spec to list all endpoints: method, path, parameters, possible response codes.
2. **Test inventory:** Parse test files using AST. Extract: which endpoints are called (find string patterns matching URL paths and HTTP methods), which response codes are asserted.
3. **Gap matrix:** Cross-reference: for each endpoint × response code, is there a test? Result is a matrix: `endpoint → [tested_codes] vs [spec_codes]`.
4. **Risk scoring:** Endpoints with no tests = HIGH risk. Endpoints with only 200 tests but no 400/401/404/500 tests = MEDIUM risk. Fully covered = LOW risk.
5. **Report:** HTML matrix showing coverage per endpoint, color-coded by risk.

### Architecture

```
coverage-gap-finder/
├── src/
│   ├── spec_parser.py          # OpenAPI → endpoint inventory
│   ├── test_scanner.py         # AST → test inventory
│   ├── gap_analyzer.py         # Cross-reference and find gaps
│   ├── risk_scorer.py          # Score each gap
│   └── reporter.py             # HTML matrix report
├── tests/
└── pyproject.toml
```

### Tech Stack

| Component | Library | Why |
|-----------|---------|-----|
| Spec parsing | `openapi-spec-validator` | |
| AST parsing | `ast` (stdlib) | Extract API calls from test code |
| Reporting | `jinja2` | HTML matrix |
| CLI | `typer` | |

### Zero-Cost Hosting

- **GitHub Pages:** Publish coverage matrix as a static site.
- **GitHub Actions:** Run on every PR to show coverage impact of new tests.

### Complexity Level: Medium

**Key algorithms to learn:** AST parsing, set operations (intersection, difference), matrix computation.

### Interview Value

Proves: test strategy thinking, OpenAPI knowledge, AST metaprogramming, coverage analysis beyond code coverage.

---

## Tool 9: API Response Time Tracker (Lightweight APM)

### The Problem

Performance regressions creep in gradually. Response time for `GET /users` was 120ms last month, now it's 350ms. No single commit caused a dramatic jump — it's a slow degradation. Nobody noticed until users complained.

### Why Existing Solutions Fall Short

Full APM (Datadog, New Relic) requires infrastructure setup and costs money. You need something that runs as part of your existing test suite and tracks trends.

### The Core Logic

1. **Instrumentation via pytest plugin:** A pytest plugin that hooks into every HTTP call made via `requests.Session()` using a response hook. Records: endpoint, method, status code, response time, timestamp.
2. **Storage:** Append results to a local SQLite database after each test run. Schema: `(run_id, timestamp, endpoint, method, status, latency_ms, test_name)`.
3. **Trend analysis:** For each endpoint, calculate rolling average latency over the last 30 runs. Detect if current run's latency exceeds `mean + 2*stddev` (statistical outlier).
4. **Regression alerting:** If an endpoint shows a statistically significant slowdown, output a warning with: endpoint, baseline latency, current latency, percentage increase, and which commit introduced the change.
5. **Dashboard:** Generate a static HTML page with time-series charts showing latency trends per endpoint.

### Architecture

```
response-time-tracker/
├── src/
│   ├── plugin.py               # Pytest plugin (conftest-based)
│   ├── interceptor.py          # requests.Session hook
│   ├── storage.py              # SQLite operations
│   ├── analyzer.py             # Trend analysis + outlier detection
│   ├── alerter.py              # Regression alerts
│   └── dashboard.py            # Static HTML chart generation
├── tests/
└── pyproject.toml
```

### Tech Stack

| Component | Library | Why |
|-----------|---------|-----|
| DB | `sqlite3` (stdlib) | Zero-dependency, file-based |
| Charts | `plotly` (exported as static HTML) | Interactive charts, no server needed |
| Statistics | `statistics` (stdlib) | Mean, stdev, outlier detection |
| Plugin | `pytest` hook system | Integrates without code changes |

### Zero-Cost Hosting

- **GitHub Pages:** Publish dashboard HTML after each CI run.
- **GitHub Actions artifact:** Upload the SQLite DB as an artifact for historical analysis.

### Complexity Level: Medium

**Key algorithms to learn:** Statistical outlier detection, pytest plugin authoring, time-series analysis.

### Interview Value

Proves: performance engineering awareness, pytest internals, observability thinking, statistical analysis.

---

## Tool 10: Test Dependency Graph Visualizer

### The Problem

Your test suite has hidden dependencies. Test A creates a user. Test B (unknowingly) depends on that user existing. When you run tests in parallel or in a different order, Test B fails. You need to see these invisible connections.

### Why Existing Solutions Fall Short

`pytest --co` shows test collection but not dependencies. `pytest-dependency` requires explicit annotations — it can't detect *implicit* dependencies that exist in your fixture chain or shared state.

### The Core Logic

1. **Static analysis:** Parse all conftest files and test files using AST. Extract: which fixtures each test uses, which shared resources (database records, files, env vars) each fixture modifies.
2. **Shared state detection:** Identify fixtures that *write* to shared state (database inserts, file creation, global variable mutation) and tests that *read* from shared state. Any test that reads state written by another test's fixture has an implicit dependency.
3. **Graph construction:** Build a dependency graph: `Test A → writes → shared_state_X ← reads ← Test B`. This means Test B implicitly depends on Test A.
4. **Visualization:** Generate an interactive graph (nodes = tests, edges = dependencies, color = fixture scope).
5. **Isolation scoring:** Score each test: 0 dependencies = fully isolated (green). >3 dependencies = high coupling (red). Output ranking.

### Architecture

```
test-dependency-viz/
├── src/
│   ├── ast_analyzer.py         # Parse fixtures and test functions
│   ├── state_tracker.py        # Detect shared state read/write
│   ├── graph_builder.py        # Build dependency graph
│   ├── visualizer.py           # Generate interactive HTML graph
│   ├── isolation_scorer.py     # Score test isolation
│   └── cli.py
├── tests/
└── pyproject.toml
```

### Tech Stack

| Component | Library | Why |
|-----------|---------|-----|
| AST | `ast` (stdlib) | Static code analysis |
| Graph | `networkx` | Graph construction and analysis |
| Visualization | `pyvis` | Interactive HTML graph from networkx |
| CLI | `typer` | |

### Zero-Cost Hosting

- **GitHub Pages:** Publish interactive graph as a static HTML site.
- **GitHub Actions:** Generate and publish on every push to main.

### Complexity Level: Hard

**Key algorithms to learn:** AST analysis, shared state detection heuristics, graph construction and visualization.

### Interview Value

Proves: deep understanding of test isolation, AST/metaprogramming, graph algorithms, test architecture thinking.

---

## Build Sequence Recommendation

Build these in order of increasing complexity. Each builds on skills from the previous:

| Order | Tool | Key Skill Gained |
|-------|------|-----------------|
| 1 | Tool 4: Environment Health Monitor | Async Python, YAML config, concurrent execution |
| 2 | Tool 9: Response Time Tracker | Pytest plugins, SQLite, statistical analysis |
| 3 | Tool 8: Test Coverage Gap Finder | AST parsing, OpenAPI, set operations |
| 4 | Tool 6: Test Impact Analyzer | Import graph, reverse traversal, git integration |
| 5 | Tool 1: Contract Drift Detector | Recursive traversal, structural diffing |
| 6 | Tool 7: Log Anomaly Detector | Statistical anomaly detection, log parsing |
| 7 | Tool 3: Flaky Test Forensics | Correlation analysis, permutation testing |
| 8 | Tool 10: Dependency Graph Visualizer | Static analysis, shared state heuristics |
| 9 | Tool 2: Synthetic Data Generator | Topological sort, constraint satisfaction |
| 10 | Tool 5: Mock Server Generator | HTTP proxy, code generation, stateful mocking |

---

## Hosting Quick Reference

| Platform | Best For | Limitations | Free Tier |
|----------|---------|-------------|-----------|
| **GitHub Pages** | Static HTML reports, dashboards, documentation | Static only, no server-side logic | Unlimited for public repos |
| **GitHub Actions** | CLI tools run in CI, scheduled tasks, artifact generation | 2000 min/month free for private repos | Unlimited for public repos |
| **Render** | FastAPI/Flask web services (Tool 5 mock server) | Spins down after 15 min inactivity, 750 hours/month | 1 free web service |
| **Vercel** | Static sites, serverless functions | 100GB bandwidth/month, 10s function timeout | Generous free tier |
| **PyPI** | CLI tools distributed as pip packages | Package only, no hosting | Free forever |
| **Railway** | Persistent services with databases | 500 hours/month, 1GB RAM | Limited free tier |

---

*Build 3–5 of these tools well. Each one in your portfolio communicates: "I identify engineering problems and build solutions." That's what separates a senior SDET from someone who runs tests.*
