# QA Learning Roadmap — Deep Acceptance-Repo Mapping

**Purpose:** Every learning topic tied to **exact files, patterns, and workflows in jumpcloud-acceptance** so you relate while building + gain general market skills.  
**Companion doc:** `QA_Learning_Roadmap_Acceptance_Aligned.md` (platforms, minor topics, anti-patterns).

---

## How to read this document

Each phase has three columns for every topic:

1. **What you learn & build yourself** (your personal repo)
2. **Where it lives in jumpcloud-acceptance** (exact paths you open to relate)
3. **Market-level skill** (what interviewers expect you to explain)

---

## Phase 0 — Habits & Toolchain (Weeks 1–2)

### 0.1 Git

| You build | In jumpcloud-acceptance | Market skill |
|-----------|------------------------|--------------|
| Create `qa-learning-journey` repo, practice branch → PR → merge | The repo itself — 48 workflows triggered on `push`, `pull_request`, `merge_group` in `.github/workflows/ci.yaml` lines 1–17. Look at `concurrency:` block (line 28–30) to see how CI cancels stale runs on the same branch. | Rebase, cherry-pick, bisect, resolve conflict, explain `concurrency` in CI |
| Intentionally create a merge conflict and resolve it | `.pre-commit-config-py.yaml`, `.pre-commit-config-js.yaml`, `.pre-commit-config-feature-files.yaml` — three separate pre-commit configs. When you edit Python + feature files in one branch, pre-commit may flag different things — understanding how hooks interact with git. | Pre-commit hooks as a git concept (not just a tool) |

### 0.2 venv + requirements.txt

| You build | In jumpcloud-acceptance | Market skill |
|-----------|------------------------|--------------|
| `python3 -m venv .venv`, install `requests`, freeze to `requirements.txt` | `poc-flaky-ai/README.md` documents: `python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt`. Also `tools/flaky-test-healer/requirements.txt`. | Create venv, explain isolation, read/write requirements files |
| Delete venv, recreate from `requirements.txt`, verify it reproduces | `poc-flaky-ai/requirements.txt` is a **flat list**; contrast with `pyproject.toml` (structured, grouped). Why does the smaller tool use requirements.txt? Because it's standalone, simple, no lockfile needed. | When to use requirements.txt vs Poetry — trade-offs |

### 0.3 Poetry

| You build | In jumpcloud-acceptance | Market skill |
|-----------|------------------------|--------------|
| `poetry init` → `poetry add requests pytest` → `poetry run pytest` | **Root `pyproject.toml`** — the main project definition. Open and trace: | |
| | `[tool.poetry.dependencies]` (line 8–36): runtime deps — `requests`, `playwright`, `confluent-kafka`, `datadog-api-client`, `pandas` | Explain main vs dev dependency groups |
| | `[tool.poetry.group.dev.dependencies]` (line 39–75): test/dev deps — `pytest==8.0.2` (pinned exact), `pytest-bdd>=8.1.0` (range), `ddtrace`, `pre-commit`, `pytest-rerunfailures` | Pins vs ranges; why pytest is pinned exactly (known import issue at 8.1.0, see comment line 52–53) |
| | `[tool.poetry.scripts]` (line 82–88): CLI entry points like `run-sso-connector-validation-tests`, `get-tag-data` | Poetry scripts = runnable commands from your package |
| | `poetry.lock` — 10,000+ lines of locked transitive deps | Lockfile guarantees CI and local match |
| Compare: `mcp_server/pyproject.toml` + `mcp_server/poetry.lock` — same pattern, smaller scope | How sub-projects in a monorepo each have their own Poetry config | Monorepo dependency isolation |

### 0.4 Shell basics + repo scripts

| You build | In jumpcloud-acceptance | Market skill |
|-----------|------------------------|--------------|
| Write a shell script: clone → venv → install → run tests → log output | **`bin/`** folder has 58 scripts. Study: | |
| | `bin/run_tests` — the main test runner (how tests are invoked in CI and locally) | Reading and writing bash scripts |
| | `bin/lint` — runs linters | Linting as a CI gate |
| | `bin/set-up-local-pre-commit` — configures pre-commit hooks | Local dev setup automation |
| | `bin/ci/determine_test_run.py` — Python script that decides which tests to run based on changed files | Smart test selection (not running everything) |
| | `bin/wait_for_pods` — waits for Kubernetes pods to be ready (you'll understand this fully in Phase 5) | Shell + K8s interaction |

### 0.5 .gitignore and repo hygiene

| You build | In jumpcloud-acceptance | Market skill |
|-----------|------------------------|--------------|
| Create `.gitignore` for Python project | Root `.gitignore` — see what the team excludes: `.venv/`, `__pycache__/`, `node_modules/`, `.pytest_cache/`, local env files | What belongs in .gitignore and why |
| | Root `.dockerignore` — different from `.gitignore`; controls what Docker COPY includes in the image | .gitignore vs .dockerignore distinction |

---

## Phase 1 — Python + OOP + DSA (Weeks 3–8)

### 1.1 Python fundamentals → relate to helpers

| You build | In jumpcloud-acceptance | Market skill |
|-----------|------------------------|--------------|
| Task Manager CLI (variables, lists, dicts, functions, file I/O, error handling) | **`tests/python/helpers/`** — 80+ helper modules. Each is plain Python: classes, functions, error handling. Start with: | |
| | `helpers/retry.py` — **37 lines of clean Python.** Uses `TypeVar`, `Callable`, `logging.getLogger(__name__)`, `time.sleep()`, custom error matching with `_is_transient()`. This is exactly the kind of utility code you'll write. | Writing utility functions; retry patterns; logging |
| | `helpers/requests.py` — HTTP helper layer. Functions like `base_headers()`, `headers_apiKey(admin)`, `assert_body_contains_field()`. Shows how the team wraps `requests` library calls. | API client abstraction; custom assertion functions |
| | `helpers/context.py` — **the `Context` class.** A data bag that steps share. 700+ lines. Uses type hints (`session: JCRequestsSession`, `response: Any`, `Dict`, `List`, `Optional`). This is OOP for test state. | Shared test context pattern; type annotations |

### 1.2 OOP → relate to models and helpers

| You build | In jumpcloud-acceptance | Market skill |
|-----------|------------------------|--------------|
| Library System (classes, inheritance, encapsulation) | `helpers/context.py` → `Context` class: `__init__` with defaults, class-level type annotations, properties that store test state across steps | Classes as state containers |
| | `tests/python/models/` — model directory. Contains data classes for test objects (PWM users, SCIM users, etc.) | Modeling API entities as classes |
| | `helpers/users.py`, `helpers/system.py`, `helpers/administrator.py` — domain-specific helper classes that wrap JumpCloud APIs (users, systems, admins) | Domain modeling for tests |
| | `helpers/ad_controller.py`, `helpers/gsuite_controller.py`, `helpers/m365_controller.py` — **controller pattern**: classes that manage external integrations (Active Directory, Google Suite, M365) | Controller/service pattern in test code |

### 1.3 Data structures / string parsing → relate to real parsers

| You build | In jumpcloud-acceptance | Market skill |
|-----------|------------------------|--------------|
| Log Parser (read file, regex, group by error type, count) | `bin/ci/determine_test_run.py` — Python that parses git diffs to determine which tests need to run. Uses file path matching, string operations, data grouping. | Parsing structured data; decision logic |
| | `jumpcloud/acceptance/print_test_failure_report.py` — parses test results, formats output. Uses dicts, lists, string formatting. | Report generation from test data |
| | `jumpcloud/acceptance/get_tag_data.py` — reads tag metadata, processes it. | Data extraction and transformation |

### 1.4 Constants, config, and environment variables

| You build | In jumpcloud-acceptance | Market skill |
|-----------|------------------------|--------------|
| Use `os.environ.get()` and `.env` files in your project | **`tests/python/constants.py`** — the central constants file. See how it works: | |
| | `EXTERNAL_DOMAIN = os.environ.get("EXTERNAL_DOMAIN", "jumpcloud.local")` — env var with fallback default (line 14) | Environment-based config with safe defaults |
| | `BULK_USER_COUNT = int(os.environ.get("BULK_USER_COUNT", 3))` — env var cast to int (line 40) | Type-safe env var reading |
| | Uses `faker.fake.password()` for test data generation — `Faker` library for dynamic test data (lines 22–36) | Test data generation with Faker |
| | Constants grouped by domain: AD passwords, LDAP, GSuite, Office365, Bulk operations | Organizing test constants by domain |

---

## Phase 2 — API Automation, Pytest, BDD, CI/CD (Weeks 9–16)

This is the **core phase** — everything you build here directly mirrors what you do daily at JumpCloud.

### 2.1 HTTP client layer

| You build | In jumpcloud-acceptance | Market skill |
|-----------|------------------------|--------------|
| Base API client class with `get()`, `post()`, `put()`, `delete()` | **`helpers/requests.py`** — the team's HTTP layer: | |
| | `base_headers()` → returns `{"Accept": "application/json", "Content-Type": "application/json"}` | Standard API headers |
| | `headers_apiKey(admin)` → adds auth header from admin model | Auth header injection pattern |
| | Functions use `requests.get()`, `requests.post()` with explicit headers, URL construction from constants like `WEBUI_URL` | Building URLs from config + path |
| | **`helpers/retry.py`** → `retry_on_transient()` function: retries on 500s, timeouts, transient errors with configurable `max_retries` and `retry_delay` | Retry logic for flaky APIs |
| | `TRANSIENT_ERROR_PATTERNS` tuple (line 13–17): `"Status: 500"`, `"InternalServerError"`, `"UserModel validation failed"` — real patterns from production failures | Pattern-matching for transient errors |

### 2.2 Pytest deep dive

| You build | In jumpcloud-acceptance | Market skill |
|-----------|------------------------|--------------|
| Fixtures with different scopes (function, session) | **`tests/python/conftest.py`** — 1000+ line conftest. This is the heart of the framework. Key fixtures: | |
| | `context` fixture → returns `Context()` instance (shared state bag for steps) | Fixtures as dependency injection |
| | `admin` fixture → creates/returns a registered admin user for API calls | Fixture as test data factory |
| | Cleanup fixtures using `yield` → code after yield runs as teardown | Setup/teardown via yield |
| | Imports like `from tests.python.step_definitions import *` → auto-registers all step definitions | Conftest as the framework bootstrap |
| Markers (`@pytest.mark.smoke`, `@pytest.mark.api`) | **`tests/python/pytest.ini`**: | |
| | `addopts = "--gherkin-terminal-reporter"` → default pytest options (line 3) | pytest.ini / pyproject.toml pytest config |
| | `bdd_features_base_dir = ../../features` → tells pytest-bdd where .feature files live (line 5) | BDD features path configuration |
| | `markers = slow:` → custom marker definition (line 23) | Custom markers for test categorization |
| | `xfail_strict = true` → xfail must actually fail; prevents silently passing xfails (line 28) | Strict xfail for test hygiene |
| | `log_cli = true`, `log_cli_level = WARNING` → live logging during test runs (lines 32–38) | Pytest logging configuration |
| Parametrize tests | Step definitions use `parsers.parse()` from pytest-bdd which is similar to parametrize — same data, different scenarios | Data-driven testing |

### 2.3 BDD with pytest-bdd (your #1 daily tool)

| You build | In jumpcloud-acceptance | Market skill |
|-----------|------------------------|--------------|
| Write `.feature` files with Scenarios, Background, tags | **`features/kala/bulk-jobs/bulk_jobs.feature`** — a feature you recently viewed. Study the patterns: | |
| | Tags: `@kala @bulk-jobs @all-envs` at feature level, `@p0` / `@p1` per scenario → priority-based tagging | Tag taxonomy for filtering in CI |
| | `Background: Given a registered administrator` → shared precondition for all scenarios | Background as DRY setup |
| | `Scenario Outline` with `Examples:` table → data-driven BDD | Scenario Outlines for coverage without duplication |
| | Assertions across multiple `Then` steps: status code, body structure, field values | Multi-assertion scenarios |
| Write step definitions in Python | **`tests/python/step_definitions/kala_bulk_jobs.py`** — the matching steps: | |
| | `from pytest_bdd import given, parsers, then, when` → the four step decorators | pytest-bdd step definition syntax |
| | `@given(parsers.parse("{count:d} activated system users exist"))` → `{count:d}` extracts an integer from Gherkin text | Parser-based step parameters |
| | Step function receives `context: Context, admin: models.rest.User, count: int` → fixtures + parsed params as function args | Fixtures injected into step definitions |
| | `BULK_USERSTATES_API = f"{WEBUI_URL}/api/v2/bulk/userstates"` → API endpoint as a constant built from config | URL construction from env-based config |
| | Uses `factories.rest.systemusers.SystemuserFactory(admin=admin, ...)` → factory pattern for test data | Factory pattern for test entities |
| | Uses `time.time()` in usernames for uniqueness → `f"test_user_{int(time.time())}_{i}"` | Unique test data generation |
| Explore other features | **84 feature directories** under `features/`. Each maps to a JumpCloud domain: | |
| | `features/users/` → user CRUD, user lifecycle | Pick ONE feature area per week to read |
| | `features/auth/` → authentication flows | |
| | `features/ldap/` → LDAP integration tests | |
| | `features/policies/` → policy management | |
| | `features/kala/` → scheduled jobs (bulk ops) | |
| | `features/playwright-specs/` → UI test features | |
| | Each feature dir has `.feature` files; matching steps live in `tests/python/step_definitions/` with similar names | Feature ↔ step definition naming convention |

### 2.4 Framework architecture (the "big picture" of acceptance)

| Concept | In jumpcloud-acceptance | Market skill |
|---------|------------------------|--------------|
| **Project structure** | Root: `features/` (Gherkin) + `tests/python/` (code) + `jumpcloud/` (package) + `bin/` (scripts) + `python-tools/` (utilities) | Separation of specs, code, tooling |
| **Helpers = service layer** | `tests/python/helpers/` — 80+ modules: one per JumpCloud domain (users, systems, policies, AD, GSuite, M365, LDAP, RADIUS, SCIM, OAuth, etc.) | Helpers wrap APIs; steps call helpers; features define behavior |
| **Models = data layer** | `tests/python/models/` — Pydantic/dataclass models for API entities | Typed models > raw dicts |
| **Factories = data generation** | Used via `jumpcloud.si.tdk.factories` (external TDK package, see `pyproject.toml` line 39) | Factory pattern for test data |
| **Constants = config** | `tests/python/constants.py` — env vars + defaults + test data | Central config, no magic strings |
| **Conftest = bootstrap** | `tests/python/conftest.py` — registers step definitions, configures Datadog tracing, sets up fixtures | Conftest as framework entry point |
| **Step definitions = glue** | `tests/python/step_definitions/` — 120+ files, one per domain | Steps are thin; business logic lives in helpers |
| **Test files = scenario wiring** | `tests/python/test_*.py` — each imports scenarios from feature files | `test_*.py` files connect features to pytest collection |

### 2.5 CI/CD with GitHub Actions

| You build | In jumpcloud-acceptance | Market skill |
|-----------|------------------------|--------------|
| Simple workflow: on push → install → test → report | **`.github/workflows/ci.yaml`** — the main CI workflow. 380+ lines. Key patterns: | |
| | Triggers: `pull_request`, `push` (branches-ignore: master), `merge_group`, `workflow_dispatch` (lines 3–17) | Multiple trigger types |
| | Permissions: `contents: read`, `id-token: write` (for AWS OIDC) (lines 19–23) | Least-privilege permissions |
| | Concurrency: cancel in-progress builds on same branch (lines 28–30) | CI cost optimization |
| | `changes` job uses `dorny/paths-filter` to detect which files changed → only runs relevant tests (lines 33–80) | Smart test selection based on changed files |
| | Separate filters for: `selenium`, `feature-files`, `python`, `javascript`, `cypress-tests`, `pytest-playwright-tests`, `ai-tooling` | Monorepo CI patterns |
| | **48 total workflows** in `.github/workflows/` including: `acceptance_tests.yaml`, `daily_flaky_test_run.yaml`, `daily_test_broken.yaml`, `flaky_test_healer.yaml`, `manage_flaky_tests.yaml`, `hourly_WOK2_acceptance_tests.yaml` | Scheduled runs, flaky management, multi-env testing |
| Add secrets management | `${{ secrets.* }}` used throughout workflows for API keys, AWS credentials | Never hardcode secrets |
| Add artifacts upload | Workflows upload test results, logs as artifacts | Test reports as CI artifacts |

### 2.6 Linting and code quality

| You build | In jumpcloud-acceptance | Market skill |
|-----------|------------------------|--------------|
| Add `black`, `ruff` to your project | Root config files: `.flake8`, `.isort.cfg`, `.pylintrc`, `mypy.ini` — four different Python quality tools | Code quality tool configuration |
| | `.pre-commit-config-py.yaml` — pre-commit hooks for Python: runs formatters/linters before commit | Pre-commit as quality gate |
| | `.pre-commit-config-feature-files.yaml` — pre-commit for Gherkin files | Linting non-code files (feature files) |
| | `.gherkin-lintrc`, `.reformat-gherkin.yaml` — Gherkin-specific formatting rules | BDD file standards enforcement |
| | `bin/lint` — manual lint runner | Linting in scripts |

### 2.7 Datadog integration for your API framework

| You build | In jumpcloud-acceptance | Market skill |
|-----------|------------------------|--------------|
| Add ddtrace to your framework | `pyproject.toml` line 62: `ddtrace = "2.13.0"` — add to your own framework's dependencies | APM library integration |
| Auto-instrument HTTP calls | `conftest.py` lines 38–40: `patch_all(urllib3=True)` + `ddtrace.config.urllib3["split_by_domain"] = True` | Auto-instrumentation configuration |
| Add test metadata to traces | `conftest.py` lines 407–420: `datadog_tags = {"test.name": scenario_name}` + `set_dd_tags_for_scenario()` | Custom trace tagging for test correlation |
| Environment-based tracing | `conftest.py` line 420: `add_cluster_info_to_ddtrace()` — adds environment context | Environment context in observability |
| Failure categorization | `conftest.py` line 185: `derive_datadog_failure_category()` — maps exceptions to categories | Structured failure analysis in traces |

---

## Phase 3 — Playwright + AI in Test Automation (Weeks 17–22)

### 3.1 Playwright

| You build | In jumpcloud-acceptance | Market skill |
|-----------|------------------------|--------------|
| Playwright project with Page Objects, fixtures, trace viewer | Playwright is **already in this repo** (Python, not TypeScript). Trace the setup: | |
| | `pyproject.toml` line 32–33: `playwright = "^1.54.0"`, `pytest-playwright = "^0.7.0"` → declared as main dependencies | Playwright as a test dependency |
| | `tests/python/conftest.py` line 36: `from playwright.sync_api import sync_playwright` → sync API, not async | Sync vs async Playwright APIs |
| | `tests/python/conftest.py` lines 33–35: `from PIL import Image`, `from pixelmatch.contrib.PIL import pixelmatch` → **visual regression testing** with pixel comparison | Visual testing with screenshot comparison |
| | `tests/python/helpers/playwright_ui_helpers/admin_portal_page.py` → Page Object for admin portal | Page Object Model in real use |
| | `tests/python/step_definitions/playwright_ap_visual.py` → step definitions for Playwright visual tests | BDD + Playwright combined |
| | `tests/python/step_definitions/playwright_login_logout.py` → login/logout UI flows via Playwright | Common UI flow automation |
| | `features/playwright-specs/` → Gherkin features for UI tests | BDD for UI testing (not just API) |
| | `features/_ui_tests/` → additional UI test features | |
| | `Dockerfile` (root) lines ~15–25: installs GTK, Xvfb, fluxbox for **headless browser** support in Docker | Running Playwright in containers |
| | `.github/workflows/ci.yaml` filter `pytest-playwright-tests:` (line 46) → separate CI detection for Playwright changes | Playwright CI pipeline |

### 3.2 AI tooling in test automation

| You build | In jumpcloud-acceptance | Market skill |
|-----------|------------------------|--------------|
| Write reusable Cursor prompts for test generation | **`.github/prompts/`** — 13 team-maintained prompt files: | |
| | `write-feature-files.prompt.md` → how to write BDD features with correct tags, structure | AI-assisted BDD authoring |
| | `write-API-step-definitions.prompt.md` → how to write step definitions following repo patterns | AI-assisted step definition writing |
| | `write-UI-tests.prompt.md` → Playwright UI test generation guidance | AI-assisted UI test authoring |
| | `automation-help.prompt.md` → general automation assistance with repo context | AI as automation pair-programmer |
| | `bdd-assistant.prompt.md` → BDD-specific AI guidance | |
| | `running_tests.prompt.md` → how to run tests locally and in CI | |
| | `reformat_feature_file.prompt.md` → auto-format Gherkin files | |
| | `self-test.prompt.md` → AI self-verification | Quality control for AI outputs |
| | `README.md` in `.github/prompts/` → documents the prompt system | Team-scale prompt management |
| Create one Cursor skill | **`.cursorrules`** at repo root — the project-wide AI behavior rules (you already know this from your daily work) | Project-level AI configuration |
| | **`.cursor/BUGBOT.md`**, `.cursor/bugbot/python-code-review.md` → bug detection AI rules | AI-assisted code review |

---

## Phase 4 — Docker + AWS (Weeks 23–28)

### 4.1 Docker

| You build | In jumpcloud-acceptance | Market skill |
|-----------|------------------------|--------------|
| Dockerfile for your API test runner | **`Dockerfile`** (root) — the main test image. Multi-stage, complex. Key patterns: | |
| | Base: `python:3.10.11-bullseye` → Debian-based Python image | Choosing base images |
| | Installs: LDAP libs, SSH, FreeRADIUS, GTK/headless browser stack, `grpcurl` → system-level deps for integration tests | System dependency installation in Docker |
| | This is a **heavy** image (full browser stack) — contrast with lighter alternatives | Image size trade-offs |
| | **`Dockerfile.python`** — builds on top of the base image. Uses `ARG BASE_IMAGE` for parameterization | Multi-stage / parameterized Docker builds |
| | Copies `pyproject.toml`, `poetry.lock` first → installs deps → then copies code → **layer caching optimization** | Docker layer caching strategy |
| | `bin/poetry`, `bin/pip`, `bin/aws` → custom wrapper scripts for CI use inside containers | Tool wrappers for containers |
| Docker Compose for test + mock API | **`docker-compose.yml`** at root — container orchestration for the test environment | docker-compose for test environments |
| | **`mcp_server/docker-compose.yml`** — simpler example: just the MCP server | Simpler compose reference |
| | **`mcp_server/Dockerfile`** — clean, small: `python:3.10-slim`, Poetry install, `CMD ["python", "server.py"]` | Clean Dockerfile (good template to learn from) |
| `.dockerignore` | Root `.dockerignore` — excludes `.git`, `node_modules`, `venv`, `__pycache__` from build context | Reducing Docker build context |

### 4.2 AWS

| You build | In jumpcloud-acceptance | Market skill |
|-----------|------------------------|--------------|
| S3 for test reports, IAM basics | `.github/workflows/ci.yaml` line 23: `id-token: write` → OIDC for AWS role assumption (no hardcoded keys) | AWS OIDC authentication in CI |
| | `bin/aws` — AWS CLI wrapper | AWS CLI usage in automation |
| | `.github/workflows/export-db-clone-to-s3.yaml` → exports data to S3 | S3 as artifact storage |
| | `.github/workflows/cleanup_wok_instances.yaml` → manages cloud resources | Cloud resource lifecycle management |
| EC2/ECS concepts | `Dockerfile.python` → the image that runs in CI (likely on AWS infrastructure) | Container images for cloud execution |
| | Terraform files: `.terraform-version`, `.terraformignore`, `terraform/` directory | Infrastructure as Code (IaC) awareness |

---

## Phase 5 — Kubernetes + GCP (Weeks 29–32)

### 5.1 Kubernetes

| You build | In jumpcloud-acceptance | Market skill |
|-----------|------------------------|--------------|
| Deployment, Service, ConfigMap on local minikube | **`charts/`** directory — Helm charts for K8s deployment of the test infrastructure | Helm charts as K8s package manager |
| | `devspace.yaml` — DevSpace configuration for local K8s development (WoK) | Local K8s development workflows |
| | `bin/wait_for_pods` — shell script that waits for pods to be ready before running tests | K8s readiness in automation |
| | `.github/workflows/create-persistent-wok.yaml` → creates WoK (Workspace on Kubernetes) environments | K8s environment provisioning |
| | `.github/workflows/spin_up_wok_from_ci.yaml` → spins up K8s workspaces from CI | CI ↔ K8s integration |
| | `.github/workflows/trigger_wok_hibernate_namespace.yaml` → manages K8s namespace lifecycle | K8s namespace management |
| | `.github/workflows/clone-persistent-wok-data.yaml` → clones data for test environments | Test data in K8s |
| | `primary-cluster-info.yaml` — cluster configuration | K8s cluster config |
| | `wok_service_resources_config.json` — resource config for WoK services | K8s resource planning |
| `kubectl logs`, `kubectl describe`, `kubectl exec` | Your daily `k9s` usage → now you understand the YAML behind what k9s shows you | kubectl as the foundation behind k9s |

### 5.2 GCP

| You build | In jumpcloud-acceptance | Market skill |
|-----------|------------------------|--------------|
| GKE basics, Cloud Build | `pyproject.toml` lines 47–49: `google-api-python-client`, `google-auth-oauthlib`, `google-auth-httplib2` → GCP client libraries in the test suite | GCP SDK usage in Python |
| | `helpers/gsuite_controller.py`, `helpers/gsuite.py` → interacts with Google Workspace APIs | GCP API integration testing |
| | `gsuite_service_account_creds.p12` at root → service account credentials for Google integration | GCP service account auth |

---

## Phase 6 — MCP, Cursor Skills/Agents, Polish (Weeks 33–36)

### 6.1 MCP servers

| You build | In jumpcloud-acceptance | Market skill |
|-----------|------------------------|--------------|
| One personal MCP tool (e.g. test failure summarizer) | **`mcp_server/`** — a full MCP server implementation: | |
| | `mcp_server/server.py` → the entrypoint | MCP server architecture |
| | `mcp_server/helpers/unified_api_parser.py` → parses API definitions | Building MCP tools |
| | `mcp_server/helpers/mcp_tool_logic.py` → tool implementations | MCP tool design |
| | `mcp_server/helpers/api_parsing_utils.py` → utility functions | |
| | `mcp_server/Dockerfile` + `docker-compose.yml` → containerized MCP server | Containerizing AI tools |
| | `mcp_server/pyproject.toml` → Poetry-managed dependencies | |
| | **`README.md`** MCP section (lines 32–100+) → full setup guide: `bin/mcp-manager` script, Docker container management, VS Code and Cursor configuration | MCP integration documentation |
| | `bin/mcp-manager` → automated setup script for MCP | AI tool deployment automation |

### 6.2 Cursor / AI project configuration

| You build | In jumpcloud-acceptance | Market skill |
|-----------|------------------------|--------------|
| `.cursorrules` for your personal project | **`.cursorrules`** at repo root → project-wide AI behavior (conciseness, think-first, automation guardrails, testing standards) | AI coding assistant configuration |
| Reusable prompts | **`.github/prompts/`** → 13 prompt files covering feature writing, step definitions, UI tests, test running, BDD assistance, MCP status, reformatting | Team-scale AI prompt management |
| | `.github/prompts/constants.md` → shared context injected into prompts | Prompt context management |
| AI-assisted code review | `.cursor/BUGBOT.md`, `.cursor/bugbot/python-code-review.md` → automated bug detection and code review rules | AI in code review pipelines |

---

## Phase 2+ — Datadog Observability (integrated, not separate)

### Datadog APM & Test Tracing

| You build | In jumpcloud-acceptance | Market skill |
|-----------|------------------------|--------------|
| Add ddtrace to your API framework | **`pyproject.toml` line 62:** `ddtrace = "2.13.0"` → Datadog APM tracing library | APM integration in test frameworks |
| Auto-instrument HTTP calls | **`tests/python/conftest.py` lines 23–24, 30–31, 38–40:** | |
| | `import ddtrace` → import the tracing library | Understanding APM library imports |
| | `from ddtrace import Pin, patch_all, tracer` → core tracing components | APM instrumentation patterns |
| | `patch_all(urllib3=True)` → auto-instruments all urllib3/requests calls | Auto-instrumentation vs manual |
| | `ddtrace.config.urllib3["split_by_domain"] = True` → separate traces per domain | Trace configuration for microservices |
| Add test metadata to traces | **`tests/python/conftest.py` lines 407–420, 753–760:** | |
| | `datadog_tags = {"test.name": scenario_name}` → BDD scenario name in traces | Test metadata in observability |
| | `set_dd_tags_for_scenario(datadog_tags)` → custom function to set trace tags | Custom tagging for test correlation |
| | `add_cluster_info_to_ddtrace()` → adds K8s cluster info to traces | Environment context in traces |
| | `add_test_owner_to_ddtrace()` → adds team ownership to traces | Team attribution in observability |
| Failure categorization | **`tests/python/conftest.py` line 185:** `derive_datadog_failure_category()` → maps exceptions to failure categories | Structured failure analysis |

### Datadog Dashboards & Monitoring

| You build | In jumpcloud-acceptance | Market skill |
|-----------|------------------------|--------------|
| Create test dashboards | **Live dashboard:** `README.md` line 919 links to [DATADOG DASHBOARD](https://app.datadoghq.com/dashboard/h6b-yat-wi2/acceptance-tests-envs) for acceptance test results | Production dashboard design |
| Query test results | **`devspace.yaml` line 118:** Auto-opens Datadog with query `test_level:test @test.service:${HELM_INSTANCE_NAME} env:${devspace.namespace}` | Datadog query syntax for test filtering |
| Filter by environment | **`README.md` line 454–455:** Query pattern `env:wok-$USER` to filter test data by developer environment | Environment-based observability |
| Flaky test monitoring | **`python-tools/tag_management_automation/.../flaky_tests_auto_tag.py` line 62:** Links to [flaky test dashboard](https://app.datadoghq.com/dashboard/fbh-2fe-u9z/flaky-acceptance-tests) | Specialized dashboards for test health |

### Datadog API Integration

| You build | In jumpcloud-acceptance | Market skill |
|-----------|------------------------|--------------|
| Build Datadog API client | **`python-tools/datadog-utils/src/datadog_utils/client.py`** — full Datadog API client: | |
| | Uses `datadog-api-client` library (line 11–25) → official Datadog Python SDK | Official SDK usage patterns |
| | `CIVisibilityTestsApi`, `DORAMetricsApi`, `MetricsApi` → different Datadog API endpoints | Understanding Datadog API structure |
| | Rate limiting handling (lines 36–42) → `HTTPStatus.TOO_MANY_REQUESTS`, retry logic | Production-grade API client patterns |
| | Authentication via `DD_API_KEY` and `DD_APP_KEY` env vars | Datadog authentication patterns |
| Send custom metrics | **`python-tools/datadog-utils/src/datadog_utils/upload_metrics.py`** — sends custom metrics: | |
| | `METRIC_PREFIX = "custom.jumpcloud.repo"` → custom namespace for metrics | Custom metric naming conventions |
| | `MetricPayload`, `MetricPoint`, `MetricSeries` → Datadog metric data structures | Datadog metrics API usage |
| | Combines DORA metrics + test automation metrics → business intelligence from test data | Combining multiple data sources |
| CI integration | **`.github/workflows/metrics_to_datadog.yaml`** — scheduled Datadog upload: | |
| | `DD_API_KEY: ${{ secrets.DD_API_KEY }}`, `DD_APP_KEY: ${{ secrets.DD_APP_KEY }}` → secure credential handling | Datadog credentials in CI |
| | `upload-metrics` command → Poetry script that runs the upload | CLI tools for observability |
| | Daily cron schedule `"0 2 * * *"` → automated metric collection | Scheduled observability workflows |

### Datadog in Test Automation Workflows

| You build | In jumpcloud-acceptance | Market skill |
|-----------|------------------------|--------------|
| Flaky test detection | **`tools/flaky-test-healer/`** uses Datadog to identify flaky tests: | |
| | `config.yaml` line 7–11: `datadog:` section with test service tags | Configuration-driven observability |
| | **`generate_llm_context_package.py` line 539:** `Extract test history from Datadog` → pulls historical test data for AI analysis | Historical test data analysis |
| | **`llm_flaky_fixer.py` line 1169:** Handles Datadog test name formats → "Feature Name Scenario Name" | Datadog data format understanding |
| Auto-tagging workflows | **`python-tools/tag_management_automation/`** — auto-tags tests based on Datadog data: | |
| | **`stg01_passing_tests_auto_tag.py`** → tags consistently passing tests | Data-driven test categorization |
| | **`flaky_tests_auto_tag.py`** → tags flaky tests for exclusion | Automated test health management |
| | Uses Datadog API to query test results → automated decision making | Observability-driven automation |
| WoK environment linking | **Multiple workflows** automatically link to Datadog: | |
| | `create-persistent-wok.yaml`, `spin_up_wok_from_ci.yaml` → pass `datadog-api-key` to WoK environments | Environment observability integration |
| | Auto-opens browser to Datadog filtered by environment → immediate test result access | Developer experience optimization |

### Datadog Query Patterns (JumpCloud-Specific)

| Pattern | Usage in jumpcloud-acceptance | Market skill |
|---------|------------------------------|--------------|
| Service filtering | `@test.service:test-coverage` → filters to specific test service | Service-based observability |
| Environment filtering | `env:wok-$USER` → filters to developer's WoK environment | Environment isolation in observability |
| Test level filtering | `test_level:test` → filters to acceptance tests vs unit tests | Test pyramid observability |
| Feature filtering | `@test.feature:bulk-jobs` → filters to specific feature area | Feature-based test analysis |
| Team filtering | `@test.owning_team:autobots` → filters to team's tests | Team ownership in observability |
| Failure categorization | `@test.failure_category:infrastructure` → groups failures by type | Structured failure analysis |
| Time-based queries | `@test.run_id:${RUN_ID}` → filters to specific test run | Test run correlation |

---

## Phase 2+ — Additional Python tools (integrated, not separate)

| Tool | Path | What it teaches |
|------|------|-----------------|
| Datadog utils | `python-tools/datadog-utils/pyproject.toml` | Metrics/monitoring integration |
| Test management | `python-tools/test-management/pyproject.toml` | Test case management automation |
| DB management | `python-tools/db-management/pyproject.toml` | Database operations for test environments |
| Tag management | `python-tools/tag_management_automation/pyproject.toml` | Test tagging automation |
| PR commenting | `python-tools/post-pr-comment/pyproject.toml` | GitHub API integration |
| Test summary | `python-tools/generate-test-summary/pyproject.toml` | Report generation |
| JIRA management | `python-tools/manage_nonoperational_jira/pyproject.toml` | JIRA API integration |
| Cypress filtering | `python-tools/filter_cypress_feature_files/pyproject.toml` | Test filtering logic |

Each is a **small, focused Poetry project** — perfect examples of single-responsibility tooling. When you build your own utilities in later phases, these are your reference implementations.

---

## Cross-cutting: the acceptance repo's technology stack summary

| Layer | Technology | Where |
|-------|-----------|-------|
| Test specs | Gherkin / BDD | `features/` (84 domains) |
| Test framework | pytest + pytest-bdd | `tests/python/`, `pyproject.toml` |
| API client | `requests` + custom helpers | `tests/python/helpers/requests.py` |
| Test data | TDK factories + Faker | `jumpcloud.si.tdk.factories`, `constants.py` |
| UI testing | Playwright (Python sync) | `playwright` in `pyproject.toml`, `playwright_ui_helpers/` |
| Visual testing | Pillow + pixelmatch | `conftest.py` imports |
| CI/CD | GitHub Actions (48 workflows) | `.github/workflows/` |
| Containers | Docker + Docker Compose | `Dockerfile`, `Dockerfile.python`, `docker-compose.yml` |
| Orchestration | Kubernetes (WoK, DevSpace) | `charts/`, `devspace.yaml`, `bin/wait_for_pods` |
| Observability | Datadog (ddtrace, API, dashboards) | `pyproject.toml`, `conftest.py`, `python-tools/datadog-utils/`, live dashboards, CI workflows |
| Cloud | AWS (OIDC, S3, ECR) + GCP (GSuite APIs) | Workflows, helpers |
| Dependency mgmt | Poetry | `pyproject.toml`, `poetry.lock` |
| Code quality | flake8, isort, pylint, mypy, black, pre-commit | Root config files |
| AI tooling | MCP server, Cursor rules, GitHub prompts | `mcp_server/`, `.cursorrules`, `.github/prompts/` |
| IaC | Terraform | `terraform/`, `.terraform-version` |
| Scripts | 58 shell/Python scripts | `bin/` |
| Smaller tools | 8 Poetry sub-projects | `python-tools/` |
| Legacy UI | Cypress | `cypress/`, `cypress.config.js` |
| Legacy browser | Selenium | `tests/selenium/` |

**Everything you learn in this roadmap maps to something in this table.**

---

## How to use this document daily

```
1. Check which Phase you are in.
2. Pick ONE row from that Phase's table.
3. Build the "You build" column in your personal repo (45–60 min).
4. Open the "In jumpcloud-acceptance" path and read it (15 min).
5. Ask yourself the "Market skill" question — can you explain it? (5 min).
6. If yes → commit and move to next row.
7. If no → re-read, try again tomorrow. Don't skip.
```

---

*Every learning topic now maps to a real file you can open in jumpcloud-acceptance. No topic is orphaned from your daily work.*
