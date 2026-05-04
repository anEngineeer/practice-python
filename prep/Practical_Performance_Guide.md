# Practical Performance Testing Guide — Zero to Production Analysis

**Purpose:** Take someone with zero performance testing knowledge to confidently designing, executing, and analyzing load tests using any Python-based tool.  
**Tooling stance:** Tool-agnostic concepts first, then a comparative section on Python tools (Locust, k6, Molotov, Grinder, custom `asyncio`+`aiohttp`) so you can choose what fits your context.  
**Companion docs:** `Master_SDET_Implementation_Plan.md` (Tier 6.4), `SDET_Portfolio_Blueprint.md` (portfolio integration).  
**Philosophy:** Performance testing is not "hitting an endpoint many times." It is the discipline of answering: *"Under what conditions does this system stop meeting its promises?"* The tool is 10% of the work. The thinking is 90%.

---

## Table of Contents

- [Part 1: Core Concepts — The Language of Performance](#part-1-core-concepts--the-language-of-performance)
- [Part 2: The Universal Anatomy of a Load Test](#part-2-the-universal-anatomy-of-a-load-test)
- [Part 3: Python Tool Landscape — Choose Your Weapon](#part-3-python-tool-landscape--choose-your-weapon)
- [Part 4: Scripting Principles — Applicable to Any Tool](#part-4-scripting-principles--applicable-to-any-tool)
- [Part 5: Execution Strategies — Ramp-Up, Soak, Spike, and Breakpoint](#part-5-execution-strategies--ramp-up-soak-spike-and-breakpoint)
- [Part 6: Analysis Mastery — Reading Reports Like an Engineer](#part-6-analysis-mastery--reading-reports-like-an-engineer)
- [Part 7: Bottleneck Identification — DB, Network, or Code?](#part-7-bottleneck-identification--db-network-or-code)
- [Part 8: Capstone Project — Load Test a Public API and Generate a Report](#part-8-capstone-project--load-test-a-public-api-and-generate-a-report)
- [Part 9: Performance Testing in CI/CD](#part-9-performance-testing-in-cicd)
- [Part 10: Tool-Specific Quick Starts](#part-10-tool-specific-quick-starts)

---

## Part 1: Core Concepts — The Language of Performance

Before touching any tool, you must speak the language fluently. Every term below appears in performance review meetings, incident postmortems, and interviews. These concepts are universal — they apply whether you use Locust, k6, JMeter, Gatling, or raw `curl` in a loop.

### 1.1 The Five Pillars of Performance

#### Latency (Response Time)

**What it is:** The time between sending a request and receiving the complete response. Measured in milliseconds (ms).

**Why it matters:** Users perceive latency directly. A page that loads in 200ms feels instant. At 1000ms, users notice. At 3000ms, users leave.

**The nuance most people miss:** Latency is NOT a single number. It's a *distribution*. Saying "average response time is 200ms" hides the fact that 5% of users experience 2000ms.

**The percentiles you must know:**

| Percentile | What It Means | Why It Matters |
|-----------|---------------|---------------|
| p50 (median) | Half of requests are faster than this | The "typical" experience |
| p90 | 90% of requests are faster than this | The experience of most users |
| p95 | 95% of requests are faster than this | Industry standard SLA target |
| p99 | 99% of requests are faster than this | The "worst reasonable" experience |
| p99.9 | 99.9% of requests are faster than this | Critical for high-traffic systems |

**Key insight:** p95 is the standard because it represents the experience of your least-happy significant user group. If your p95 is 500ms but your average is 100ms, 1 in 20 users has a terrible experience. That's thousands of users per day at scale.

**How to internalize this:** The next time you use any web app and it feels slow, check your browser's DevTools Network tab. Look at the timing breakdown. You're experiencing a high-percentile latency.

#### Throughput (Transactions Per Second / TPS)

**What it is:** The number of completed requests per second the system handles.

**Why it matters:** Throughput tells you *capacity*. "Our API handles 500 TPS" means 500 requests complete every second.

**The relationship between latency and throughput:**

```
If one request takes 100ms:
  One thread can handle 10 requests/sec (1000ms / 100ms)
  10 threads can handle 100 requests/sec
  50 threads can handle 500 requests/sec

But only if the server has enough resources (CPU, memory, DB connections).
When resources are exhausted:
  Adding more threads INCREASES latency (queuing)
  Throughput PLATEAUS and then DROPS (saturation)
```

This is the most important relationship in performance engineering: **throughput and latency are inversely correlated under load.**

#### Concurrency (Concurrent Users / Virtual Users)

**What it is:** The number of users simultaneously interacting with the system at the same instant.

**Concurrency vs Total Users:**
- 10,000 users may be logged in, but only 500 are actively making a request at any given second.
- The 500 is your concurrency. The 10,000 is your total user base.

**Why it matters:** Concurrency determines the *pressure* on the system. Each concurrent user consumes: a thread (or async slot), a database connection, memory for their request context, network bandwidth.

#### Error Rate

**What it is:** The percentage of requests that return errors (5xx, timeouts, connection refused).

**Acceptable error rate:** Typically < 0.1% for a healthy system. Above 1% usually indicates a problem. Above 5% means the system is failing.

**Key insight:** Error rate often stays at 0% until a specific concurrency threshold, then jumps sharply. Finding that threshold is the goal of breakpoint testing.

#### Saturation

**What it is:** The point where adding more load no longer increases throughput but does increase latency and error rate.

**Visual model:**

```
Throughput (TPS)
    |          ___________
    |        /            \
    |      /               \
    |    /                   \
    |  /                       \
    |/_________________________\____
                                    Concurrent Users

Phase 1: Linear growth (throughput rises with users)
Phase 2: Plateau (throughput maxes out, latency starts rising)
Phase 3: Degradation (throughput drops, errors spike, latency explodes)

The boundary between Phase 2 and Phase 3 is saturation.
```

### 1.2 Types of Performance Tests

| Test Type | What It Answers | How It Works | Duration |
|-----------|----------------|-------------|----------|
| **Load test** | "Can the system handle expected traffic?" | Simulate expected user count for a sustained period | 10–60 min |
| **Stress test** | "At what point does the system break?" | Gradually increase users beyond expected, find the breaking point | 15–30 min |
| **Spike test** | "How does the system handle sudden traffic bursts?" | Jump from low to very high users instantly, then drop back | 5–15 min |
| **Soak test** | "Are there slow leaks (memory, connections) over time?" | Moderate load sustained for hours | 2–12 hours |
| **Breakpoint test** | "What is the absolute maximum capacity?" | Increase users until the system fails completely | Until failure |
| **Scalability test** | "How does adding resources improve performance?" | Run same test with 1 server, then 2, then 4 | Multiple runs |

### 1.3 The SLA/SLO/SLI Framework

| Term | Definition | Example |
|------|-----------|---------|
| **SLI** (Service Level Indicator) | The metric you measure | p95 response time for `GET /users` |
| **SLO** (Service Level Objective) | The target for that metric | p95 response time < 500ms |
| **SLA** (Service Level Agreement) | The contractual commitment (with consequences) | 99.9% of requests meet the SLO; breach = service credit |

**Why this matters for SDET:** Your performance tests validate SLOs. If the SLO says p95 < 500ms at 1000 concurrent users, your load test simulates 1000 users and checks p95. If it exceeds 500ms, the test fails. This is how performance testing connects to business requirements.

---

## Part 2: The Universal Anatomy of a Load Test

Regardless of the tool, every load test has the same five components. Understanding these components means you can pick up *any* tool in a day because you already know what you're building.

### 2.1 The Five Components

```
┌──────────────────────────────────────────────────────────┐
│                   LOAD TEST ANATOMY                       │
│                                                           │
│  1. VIRTUAL USER DEFINITION                               │
│     What does a simulated user DO?                        │
│     (endpoints, methods, payloads, think time)            │
│                                                           │
│  2. LOAD PROFILE (Shape)                                  │
│     How many users, ramping how fast, for how long?       │
│     (ramp-up, steady state, ramp-down)                    │
│                                                           │
│  3. DATA FEEDING                                          │
│     What data do virtual users consume?                   │
│     (CSV files, generated data, correlated responses)     │
│                                                           │
│  4. ASSERTIONS / CHECKS                                   │
│     How do we define success vs failure?                  │
│     (status codes, response body, latency thresholds)     │
│                                                           │
│  5. RESULT COLLECTION                                     │
│     How do we capture and analyze outcomes?               │
│     (CSV, JSON, HTML reports, time-series databases)      │
│                                                           │
└──────────────────────────────────────────────────────────┘
```

### 2.2 Component 1: Virtual User Definition

Every tool uses different syntax, but every tool asks you to define the same thing: *what does a simulated human do?*

**The universal pattern:**

| Concept | What It Means | Locust Syntax | k6 Syntax | Raw Python (`aiohttp`) |
|---------|--------------|---------------|-----------|----------------------|
| User class | A simulated actor | `class MyUser(HttpUser)` | `export default function()` | An `async` function per user |
| Task / action | One HTTP call | `@task` method | `http.get()` inside function | `await session.get()` |
| Task weight | Probability of choosing this action | `@task(weight=3)` | Multiple scenarios with `exec` weights | Custom weighted `random.choices()` |
| Think time | Pause between actions | `wait_time = between(1, 5)` | `sleep(Math.random() * 4 + 1)` | `await asyncio.sleep(random.uniform(1, 5))` |
| Setup (once per user) | Login, get token | `on_start()` method | `setup()` function | Code before the loop |
| Teardown | Logout, cleanup | `on_stop()` method | `teardown()` function | `finally` block |

**The key insight:** Once you understand these six concepts, you can translate any load test from one tool to another in 30 minutes. The concepts are portable; the syntax is not.

### 2.3 Component 2: Load Profile

Every tool lets you control the "shape" of load over time. The parameters are universal:

| Parameter | What It Controls | Universal Concept |
|-----------|-----------------|-------------------|
| Target user count | Maximum concurrent virtual users | Peak concurrency |
| Spawn rate | How fast users are added per second | Ramp-up speed |
| Duration | How long the test runs | Test window |
| Stages | Phases with different user counts | Load shape (ramp → hold → ramp-down) |

### 2.4 Component 3: Data Feeding

| Strategy | How It Works | When to Use |
|----------|-------------|-------------|
| **Static CSV** | Load data from file, each user picks a row | User credentials, known entity IDs |
| **Dynamic generation** | Generate data in code (Faker, uuid, timestamps) | POST bodies, unique identifiers |
| **Correlation** | Extract value from response, use in next request | Auth tokens, created resource IDs, pagination cursors |
| **Shared queue** | Users pull from a common pool (thread-safe) | Unique-per-user data, non-overlapping test accounts |

### 2.5 Component 4: Assertions / Checks

A 200 status code does not mean success. The response body might contain `{"error": "rate limited"}`. Every tool provides a mechanism for custom pass/fail logic:

**Universal assertion categories:**

| Category | Example | Why It Matters |
|----------|---------|---------------|
| Status code | `assert status == 200` | Basic sanity |
| Response body | `assert "id" in response.json()` | Functional correctness under load |
| Latency | `assert response_time < 500` | SLO enforcement per-request |
| Content type | `assert "application/json" in headers["content-type"]` | Protocol correctness |
| Data integrity | `assert response.json()["name"] == expected_name` | No data corruption under concurrency |

### 2.6 Component 5: Result Collection

Every tool outputs results differently, but you need the same data:

| Data Point | What You Need | Common Formats |
|-----------|---------------|----------------|
| Per-request metrics | Timestamp, endpoint, method, status, latency, size | CSV, JSON lines, InfluxDB, Prometheus |
| Aggregate statistics | p50, p95, p99, avg, min, max, error count per endpoint | Summary CSV, HTML table |
| Time-series | Metrics over time (for charts) | CSV with timestamps, time-series DB |
| Error details | Failed request URL, status, response body | Log file, JSON |

---

## Part 3: Python Tool Landscape — Choose Your Weapon

### 3.1 Comprehensive Comparison

| Feature | **Locust** | **Molotov** | **k6** (JS, but CI-relevant) | **Custom asyncio+aiohttp** | **nox/pytest + requests** |
|---------|-----------|-------------|------------------------------|---------------------------|--------------------------|
| **Language** | Python | Python | JavaScript (Go engine) | Python | Python |
| **Concurrency model** | Greenlets (gevent) | asyncio (native) | Go goroutines | asyncio (native) | Threads / multiprocessing |
| **Built-in dashboard** | Yes (web UI) | No | Yes (CLI + cloud) | No (build your own) | No |
| **Distributed mode** | Built-in (master/worker) | No (manual) | k6 Cloud or xk6-distributed | Manual (multiple machines) | Manual |
| **pip install** | `pip install locust` | `pip install molotov` | Binary (not pip) | `pip install aiohttp` | Already have it |
| **Learning curve** | Low | Low | Medium (different language) | Medium (asyncio knowledge) | Low (but limited scale) |
| **Max users per machine** | ~5,000 (gevent) | ~10,000+ (asyncio) | ~30,000+ (Go goroutines) | ~10,000+ (asyncio) | ~200 (thread-limited) |
| **Full Python ecosystem** | Yes | Yes | No (JS only) | Yes | Yes |
| **Best for** | Team adoption, web UI, beginner-friendly | High-concurrency, async-native | Raw performance, polyglot teams | Full control, custom metrics | Simple smoke-level perf checks |

### 3.2 Decision Framework

```
Q1: Do you need a built-in web dashboard and team-friendly UI?
├── YES → Locust
└── NO →
    Q2: Do you need maximum concurrency from a single machine?
    ├── YES → Molotov or custom asyncio+aiohttp
    └── NO →
        Q3: Do you need full control over every HTTP detail and custom metrics?
        ├── YES → Custom asyncio+aiohttp
        └── NO →
            Q4: Is your team mostly Python?
            ├── YES → Locust (ecosystem) or Molotov (modern async)
            └── NO → k6 (polyglot, high performance)
```

### 3.3 Recommendations by Context

| Context | Recommended Tool | Reasoning |
|---------|-----------------|-----------|
| Learning performance testing | Locust | Best docs, web UI for visual feedback, lowest friction |
| Portfolio / showcase project | Locust or Molotov | Python-native, demonstrates Python mastery |
| Production CI pipeline | Locust (team) or k6 (if polyglot) | Both have headless CLI modes for CI |
| Extreme concurrency (50K+ users) | k6 or custom asyncio | Go/async can generate more load per machine |
| Quick smoke perf test in pytest | `pytest` + `requests` + timing assertions | No new tool, integrates into existing test suite |
| Microservice with async Python backend | Molotov | Async-native, matches the backend model |

### 3.4 The "Build Your Own" Option

Understanding how to build a minimal load generator from `asyncio` + `aiohttp` teaches you what every tool does under the hood. This is the single most valuable exercise for understanding performance testing internals.

**What a load generator actually does:**

```
1. Create N concurrent workers (coroutines / threads / greenlets)
2. Each worker loops:
   a. Pick a task (weighted random)
   b. Record start time
   c. Execute HTTP request
   d. Record end time, status, size
   e. Evaluate pass/fail (assertions)
   f. Store the metric
   g. Wait (think time)
3. A collector aggregates all metrics
4. A reporter computes percentiles and generates output
```

That's it. Every tool is a polished version of these 7 steps. Building your own, even a crude version, demystifies all commercial tools permanently.

**How to build this incrementally (as a learning exercise):**

**Level 1:** A single `aiohttp` coroutine that makes 100 requests in a loop, recording `time.monotonic()` before and after each. Print the average latency.

**Level 2:** Use `asyncio.gather()` to run 10 coroutines concurrently. Compare total time vs sequential. You just implemented concurrency.

**Level 3:** Add a `Semaphore(max_concurrent)` to limit how many requests fire simultaneously. You just implemented concurrency control.

**Level 4:** Add think time (`await asyncio.sleep(random.uniform(1, 3))`) between requests. You just made it realistic.

**Level 5:** Collect all latencies in a list. Compute p50, p95, p99 using `statistics.quantiles()`. You just built a metrics engine.

**Level 6:** Add a `while time.monotonic() - start < duration:` loop instead of a fixed count. Add a spawning mechanism that adds new coroutines every second. You just built a load profile.

**Level 7:** Write results to a CSV file with columns: `timestamp, endpoint, method, status, latency_ms, size_bytes`. You just built result collection.

Each level teaches one fundamental concept. By Level 7, you understand what every load testing tool does internally, and you can evaluate any tool's trade-offs intelligently.

---

## Part 4: Scripting Principles — Applicable to Any Tool

These principles apply universally. The code syntax changes per tool; the thinking does not.

### 4.1 Realistic User Modeling

**Principle: Model humans, not machines.**

Every virtual user should behave like a real person with a plausible workflow. Real humans don't:
- Hit the same endpoint 1000 times in a row
- Send requests with zero delay
- Use identical data for every request
- Skip authentication

Your load test must avoid all four anti-patterns.

**The workflow approach:** Define 2–4 user personas that represent real traffic patterns.

| Persona | Typical Actions | Weight (% of traffic) | Think Time |
|---------|----------------|----------------------|------------|
| Browser | GET endpoints, pagination, search | 60% | 2–5 seconds |
| Creator | POST new resources, verify with GET | 25% | 3–7 seconds |
| Admin | GET reports, DELETE resources, PUT updates | 10% | 5–10 seconds |
| Background/Bot | API polling, webhook verification | 5% | 0.5–1 second |

**Weight rationale:** In most systems, reads vastly outnumber writes. If your load test is 50% POST and 50% GET, you're testing a scenario that doesn't exist in production. Check your real traffic ratios (analytics, APM dashboards) and mirror them.

### 4.2 Data Parameterization

**The problem:** If all 500 virtual users request `GET /users/1`, the server caches that response and you're testing the cache, not the API. You need each user to request different data.

**Approach 1: CSV-driven data.**
Load a CSV file with test data (user IDs, emails, passwords). Each virtual user picks a row.

Implementation principle: Read the CSV once at module/script initialization (not per-request). Use a thread-safe mechanism for picking rows. In async tools, concurrent access to a shared list requires care.

```
Data flow:
  CSV file → Python list (loaded once) → random.choice() per request
```

**Approach 2: Dynamic generation.**
Generate data on the fly using Faker or uuid. No file management, infinite variety.

When to use: For POST requests where you need unique data (creating users, submitting forms). Also for fields like timestamps, UUIDs, unique email addresses.

**Approach 3: Correlation (response-driven data).**
Extract data from a response and use it in the next request. Example: POST /orders returns `{"id": 12345}` → GET /orders/12345.

Implementation principle: Store the extracted value in the user's state (instance variable, dict, context object). This is the difference between a "script" and a "simulation."

**Common correlation scenarios:**

| Scenario | Extract From | Use In |
|----------|-------------|--------|
| Authentication | Login response → token | All subsequent requests → Authorization header |
| Pagination | Response → `next_page_url` | Next request → URL |
| Resource creation | POST response → `id` | GET/PUT/DELETE → URL path |
| CSRF protection | HTML page → hidden CSRF token | Form submission → request body |
| Session tracking | Response → `Set-Cookie` | Subsequent requests → `Cookie` header |

**Approach 4: Shared queue.**
A thread-safe queue of unique data. Each user pops from the queue. Once consumed, the data is not reused. Useful for test accounts that must be unique per virtual user.

**Key principle:** Parameterization makes your test realistic. Without it, you're testing a single code path. With it, you're testing the system's ability to handle diverse traffic.

### 4.3 Realistic Think Time and Pacing

**The anti-pattern:** Zero wait time between requests ("machine gun" traffic).

**Why it's wrong:** No real user sends 100 requests per second. Zero think time means your 100 virtual users generate the traffic of 10,000 real users. Your test results are meaningless because you're testing a scenario that will never happen.

**The formula (universal, tool-independent):**

```
Real concurrent users = Virtual users × (average response time / (average response time + average think time))

Example:
  100 virtual users with average 3.5s think time
  Average response time: 0.2s
  Effective concurrency: 100 × (0.2 / (0.2 + 3.5)) ≈ 5.4 truly concurrent at any instant

To simulate 50 truly concurrent users with 3.5s think time:
  Virtual users needed: 50 × (3.5 + 0.2) / 0.2 ≈ 925 virtual users
```

**Key insight:** The number of virtual users is NOT the number of concurrent connections. It's the number of users in the system, most of whom are "thinking" at any given moment. This is true in Locust, k6, JMeter, Gatling, or any custom tool.

**Think time strategies (universal concepts):**

| Strategy | Behavior | When to Use |
|----------|----------|-------------|
| Fixed delay | Always wait exactly N seconds | Simple benchmarks, synthetic tests |
| Uniform random | Wait between min and max seconds (each equally likely) | Most realistic for general testing |
| Gaussian random | Cluster around a mean with some variance | Modeling realistic human behavior (most people take ~3s, few take 1s or 6s) |
| Constant pacing | Ensure one action every N seconds regardless of response time | When you need fixed per-user TPS |
| No delay | Zero wait between requests | Only for stress tests / breakpoint tests where you want maximum pressure |

### 4.4 Custom Validation Beyond Status Codes

Every tool counts a non-error HTTP status as "success." But in the real world:

- `200 OK` with `{"error": "rate limited"}` is a failure
- `200 OK` with `{"data": []}` when you expected data is a failure
- `200 OK` with response time > 5 seconds is an SLO violation
- `200 OK` with `Content-Length: 5MB` for a list endpoint is a bug (missing pagination)

**Universal validation checklist for any load test:**

| Check | What to Validate | Why |
|-------|-----------------|-----|
| Status code | Expected 2xx for happy path, specific 4xx for negative tests | Basic correctness |
| Response body structure | Expected keys exist in JSON | Contract adherence under load |
| Response body values | Specific field equals expected value | Data integrity under concurrency |
| Response time | Per-request latency below threshold | SLO enforcement at request level |
| Response size | Body size within expected range | Detect pagination failures, data leaks |
| Content type | Header matches expected type | Protocol correctness |

---

## Part 5: Execution Strategies — Ramp-Up, Soak, Spike, and Breakpoint

These strategies are universal to all performance testing tools. The diagrams and logic apply regardless of implementation.

### 5.1 Load Shapes

#### Ramp-Up Pattern (Standard Load Test)

```
Users
  |         ___________
  |       /
  |     /
  |   /
  | /
  |/________________________ Time
  0   5min   10min    20min

Phase 1 (0–5 min): Ramp from 0 to target users
Phase 2 (5–20 min): Hold at target (steady state)
```

**Why ramp:** Jumping to 500 users instantly causes a connection storm. Ramping allows the server to warm up caches, connection pools, and JIT compilation.

**Universal implementation:** Every tool supports staged user addition. The parameter is typically `spawn_rate` (users added per second) and `target_users` (maximum count).

#### Spike Pattern

```
Users
  |     *
  |    * *
  |   *   *
  |  *     *
  | *       *___________
  |*_________*__________ Time
```

**When to use:** Black Friday, product launch, viral tweet. The system goes from idle to peak in seconds, then back down.

**Universal implementation:** Define stages — (10 users for 2 min) → (500 users for 1 min) → (10 users for 5 min). Most tools support stage-based profiles natively or via a shaping function.

#### Soak Pattern

```
Users
  |  ___________________________________
  | |
  | |
  |_|___________________________________ Time
  0        2 hours         8 hours
```

**When to use:** Finding memory leaks, connection pool exhaustion, log file disk space, garbage collection pauses. These bugs only appear after hours of sustained load.

#### Breakpoint Pattern (Step-Up)

```
Users
  |               _____
  |          ____|
  |     ____|
  |____|
  |_________________________________ Time
  100  200  300  400  500
```

**When to use:** Finding the exact concurrency where the system degrades. Increase users in steps (e.g., +50 every 5 minutes) and monitor when p95 exceeds the SLO.

### 5.2 Custom Load Shapes — The Universal Concept

Every serious tool provides a way to programmatically control the user count over time. The mechanism is always the same: a function that is called periodically (every 1–10 seconds) and returns the desired user count and spawn rate for that moment.

**Mental model:** Think of it as a "what should the load be right now?" function. The tool calls it on a timer, and you answer based on elapsed time.

| Tool | Mechanism | Return Value |
|------|-----------|-------------|
| Locust | `LoadTestShape.tick()` method | `(user_count, spawn_rate)` or `None` to stop |
| k6 | `stages` array in `options` | `{duration: "5m", target: 200}` |
| Molotov | CLI args + custom scenarios | `--workers`, `--duration`, `--ramp-up` |
| Custom asyncio | Your own timer loop | You control everything |

**How to study this:** Implement one load shape at a time in your chosen tool. Start with a simple ramp. Then a spike. Then a step-up. For each one, run the test and verify the user count chart matches your intended shape.

---

## Part 6: Analysis Mastery — Reading Reports Like an Engineer

This section is entirely tool-agnostic. Every performance tool produces the same categories of data. The format differs; the analysis is identical.

### 6.1 The Universal Statistics Table

After a test run, every tool provides a statistics summary. Here's how to read it like an engineer, not a data consumer.

| Column | What It Tells You | Red Flag |
|--------|-------------------|----------|
| **# Requests** | Total requests for this endpoint | Very low count = not enough data for percentiles |
| **# Failures** | Failed requests | Any failures > 0% during steady state is concerning |
| **Median (p50)** | Typical response time | If median is high, the entire system is slow |
| **p95** | 95th percentile response time | Primary SLO metric. If this exceeds your target, investigate. |
| **p99** | 99th percentile response time | If p99 is 10x the median, you have a "long tail" problem |
| **Average** | Mean response time | MISLEADING. Averages hide outliers. Always use percentiles. |
| **Min** | Fastest response | The theoretical best. Useful for baseline comparison. |
| **Max** | Slowest response | Often an outlier. But if max is 30s, someone's connection timed out. |
| **Avg Size** | Average response body size | Unexpectedly large = N+1 query, missing pagination, debug data leaking |
| **RPS/TPS** | Requests per second (throughput) | If RPS plateaus while users increase, you've hit saturation |

### 6.2 The Charts — What Each Line Means

Every tool produces four core chart types (some as built-in dashboards, others as exported data you chart yourself):

**Response Time Chart (line chart):**
- X-axis: time. Y-axis: response time in ms.
- Lines for p50, p95, p99.
- What to look for: **divergence**. If p50 stays flat but p95 rises sharply, a subset of requests is getting slow (possibly hitting a slow DB query or external service timeout).

**Users/Concurrency Chart:**
- Shows active virtual user count over time.
- Should match your intended load shape (ramp, spike, soak).

**Requests per Second Chart (Throughput):**
- Shows throughput over time.
- What to look for: **plateau**. If users increase but RPS stops increasing, the system is saturated.

**Failures/Errors Chart:**
- Shows error rate over time.
- What to look for: **cliff**. Error rate often stays at 0% then jumps to 20% at a specific concurrency. That's your breaking point.

### 6.3 The Analysis Framework (Step-by-Step)

When you finish a load test, follow this framework. It works regardless of tool.

**Step 1: Did we meet the SLO?**
Check p95 against your target. Yes/No. This is the headline result.

**Step 2: At what concurrency did we stop meeting the SLO?**
Look at the response time chart. Find the point where p95 crossed the SLO threshold. Cross-reference with the users chart to find the concurrency level. This is your capacity limit.

**Step 3: What was the throughput at saturation?**
Check RPS at the point where p95 started rising. This is your maximum sustainable throughput.

**Step 4: Were there errors?**
If error rate > 0% during steady state, categorize: 5xx (server error, investigate backend), 4xx (client error, might be test script issue), timeout (server too slow, connection pool exhausted).

**Step 5: Was there a long tail?**
Calculate: `p99 / p50`. If this ratio is > 5, you have a long tail. Some requests are dramatically slower than others. This usually indicates: slow DB queries on specific data, garbage collection pauses, external service timeouts, or resource contention.

**Step 6: Did throughput plateau?**
If RPS stopped increasing while users increased, the bottleneck is capacity (CPU, memory, DB connections, network bandwidth). The system needs horizontal scaling or optimization.

---

## Part 7: Bottleneck Identification — DB, Network, or Code?

### 7.1 The Three Bottleneck Categories

When performance degrades, the cause is almost always in one of three places: the database, the network, or the application code. Your job is to figure out which. This analysis is identical regardless of what tool generated the load.

### 7.2 Database Bottleneck Indicators

| Signal | What You See | Why It Happens |
|--------|-------------|---------------|
| Response time climbs linearly with users | p95 goes 100ms → 200ms → 400ms as users double | Queries compete for DB connections; lock contention |
| Throughput plateaus early | RPS maxes at 200 despite 500 users | Connection pool exhausted (e.g., pool_size=20) |
| Specific endpoints are slow, others are fine | `GET /reports` is 5s, `GET /users` is 50ms | The reports endpoint has an unoptimized query (missing index, N+1) |
| Errors include "connection pool exhausted" | 500 errors with pool-related messages | Not enough DB connections for the load |

**How to confirm:** If you have access to DB metrics:
- Check `active_connections` — if it matches `max_connections`, the pool is exhausted.
- Check `query_duration_p95` — if it's high, specific queries are slow.
- Check `lock_wait_time` — if it's high, transactions are blocking each other.

**The N+1 query problem (must know for interviews):**

```
BAD: For each of 100 users, query their 10 posts individually = 101 queries
GOOD: Get all 100 users, then get all posts WHERE user_id IN (...) = 2 queries

Signal in load test: Response time grows linearly with data size.
```

### 7.3 Network Bottleneck Indicators

| Signal | What You See | Why It Happens |
|--------|-------------|---------------|
| High p99 but low p50 | Median is 50ms but p99 is 5000ms | Packet loss, TCP retransmission, DNS resolution delays |
| Response times have high variance | Same endpoint: 30ms, 40ms, 2500ms, 35ms | Network jitter, routing issues |
| `Avg Size` is very large | Response bodies are 5MB | No pagination, entire dataset returned |
| Timeout errors increase | Connection timeout, read timeout | Server is responding but network drops the connection |

**How to confirm:**
- Check `ping` and `traceroute` to the server — are there hops with high latency?
- Check if the load test machine's network is saturated (`iftop`, `nload`).
- Compare results from a load test machine in the same datacenter vs a remote machine.

### 7.4 Application Code Bottleneck Indicators

| Signal | What You See | Why It Happens |
|--------|-------------|---------------|
| CPU utilization at 100% on the server | All metrics degrade simultaneously | CPU-bound operation (serialization, encryption, computation) |
| Memory usage grows over time (soak test) | Memory climbs, eventually OOM kill | Memory leak (objects not released, growing caches) |
| All endpoints slow equally | Every endpoint's p95 rises together | Thread pool exhaustion, GIL contention, shared resource |
| Periodic latency spikes | Every 30 seconds, p95 jumps for 2 seconds | Garbage collection pause (JVM, Go GC, Python GC) |

**How to confirm:**
- Check CPU utilization on the server — if it's at 100%, the code is the bottleneck.
- Check memory usage trend — if it's a straight upward line, there's a leak.
- Profile the application (if possible) — find the hottest functions.

### 7.5 The Diagnostic Decision Tree

```
Start: p95 exceeds SLO

Q1: Is only ONE endpoint slow, or ALL endpoints?
├── ONE endpoint →
│   Q2: Does that endpoint query a database?
│   ├── YES → Check query plan (EXPLAIN ANALYZE). Likely: missing index, N+1, full table scan.
│   └── NO → Check if it calls external services. Likely: external dependency timeout.
│
└── ALL endpoints →
    Q3: Does server CPU hit 100%?
    ├── YES → Application code bottleneck. Profile the app.
    └── NO →
        Q4: Does DB connection count hit the max?
        ├── YES → Database connection pool exhaustion. Increase pool size or optimize query duration.
        └── NO →
            Q5: Is the load test machine itself saturated?
            ├── YES → Your load generator is the bottleneck, not the server. Scale out your load gen.
            └── NO → Network issue. Check for packet loss, bandwidth saturation, DNS delays.
```

---

## Part 8: Capstone Project — Load Test a Public API and Generate a Report

### 8.1 The Project

**Target:** JSONPlaceholder API (`https://jsonplaceholder.typicode.com`) — a free, public REST API perfect for practice.

**Choose your tool:** Use whichever tool you selected from Part 3. The deliverables are identical regardless.

**Deliverables:**
1. A load test suite with 3 user behaviors
2. Execution of 4 test types (load, stress, spike, soak)
3. A PDF analysis report with findings and recommendations

### 8.2 Phase 1: Script Design (Tool-Agnostic)

**User Behavior 1: Browser (weight 60%)**
- GET /posts (list posts)
- GET /posts/{id} (read a post — use random ID 1–100)
- GET /posts/{id}/comments (read comments on a post)
- Think time: random 2–5 seconds between actions

**User Behavior 2: Creator (weight 30%)**
- POST /posts (create a post — dynamically generated title and body)
- GET /posts/{id} (verify creation — use the ID from the POST response)
- Think time: random 3–7 seconds between actions

**User Behavior 3: Admin (weight 10%)**
- GET /users (list all users)
- GET /users/{id}/todos (check a user's todos — random user ID 1–10)
- DELETE /posts/{id} (delete a post — random ID 1–100)
- Think time: random 5–10 seconds between actions

**Weight rationale:** In a real system, ~60% of traffic is reading, ~30% is creating, ~10% is admin operations. These weights model that.

### 8.3 Phase 2: Parameterization

| Data Point | Strategy | Implementation |
|-----------|----------|---------------|
| Post IDs | Random integer 1–100 | Avoids cache-hit-only testing |
| User IDs | Random integer 1–10 | JSONPlaceholder has 10 users |
| POST body | Faker-generated | `fake.sentence()` for title, `fake.paragraph()` for body |
| Created resource ID | Correlation | Parse POST response, use in subsequent GET |

### 8.4 Phase 3: Execution Matrix

Run each test and record results:

| Test Type | Users | Spawn Rate | Duration | What to Observe |
|-----------|-------|------------|----------|-----------------|
| Load test | 50 | 5/sec | 10 min | Baseline p95, RPS, error rate |
| Stress test | 200 | 10/sec | 10 min | When p95 exceeds 1000ms |
| Spike test | 10 → 150 → 10 | Instant | 5 min | Recovery time after spike |
| Soak test | 30 | 3/sec | 60 min | Memory/latency drift over time |

### 8.5 Phase 4: Analysis Report Structure

Your PDF report should contain:

```
1. Executive Summary
   - System under test
   - Test objectives
   - Key finding: "System handles X concurrent users within SLO"

2. Test Environment
   - Target: JSONPlaceholder API
   - Load generator: <your tool> (version), local machine specs
   - Network: home broadband / cloud (affects results — note this)

3. Test Scenarios
   - User behaviors and weights (table)
   - Data parameterization strategy

4. Results per Test Type
   For each test:
   - Configuration (users, spawn rate, duration)
   - Statistics table (formatted data)
   - Response time chart (p50, p95, p99)
   - Throughput chart (RPS)
   - Error rate chart
   - Key observation (one paragraph)

5. Bottleneck Analysis
   - Apply the diagnostic decision tree (Part 7.5)
   - Identify: DB, network, code, or load generator limitation
   - Note: JSONPlaceholder is a public API with rate limiting;
     this affects results and is itself a finding.

6. Recommendations
   - For a real system, what would you recommend based on these findings?
   - Examples: "Increase connection pool", "Add caching for GET /posts",
     "Investigate p99 long tail on POST endpoint"

7. Appendix
   - Load test scripts (full code)
   - Raw statistics (CSV or JSON export)
```

### 8.6 Generating the PDF Programmatically

**Tool: `fpdf2` (Python library)**

Why not Jupyter/Matplotlib? Because you want to demonstrate that you can build a pipeline: run tests → parse results → generate report → deliver artifact. This is an automation skill.

**The universal flow (works with any tool's output):**

1. **Export results** to CSV or JSON. Every tool supports this:
   - Locust: `--csv=results` flag
   - k6: `--out csv=results.csv` flag
   - Molotov: `--statsd` or custom output
   - Custom asyncio: you control the output format
2. **Parse results** with a Python script. Read the CSV/JSON into pandas or plain dicts.
3. **Generate charts** using `matplotlib`. Create response time, throughput, and error rate time-series charts. Save as PNG files.
4. **Compose the PDF** using `fpdf2`. Embed the charts, add text sections, format tables.
5. **Integrate into CI** as the final pipeline step. The PDF becomes a build artifact.

---

## Part 9: Performance Testing in CI/CD

### 9.1 Where Performance Tests Fit in the Pipeline

```
PR opened:
  Lint → Unit tests → API tests → UI tests
  (Performance tests do NOT run on every PR — too slow, too noisy)

Merge to main:
  Build → Deploy to staging → Smoke tests → PERFORMANCE TESTS → Promote to production

Scheduled (nightly/weekly):
  Full load test suite against staging
  Soak test against staging (weekly, overnight)
```

### 9.2 Performance Gate: Pass/Fail Criteria

Define thresholds that cause the pipeline to fail:

| Metric | Threshold | Action on Breach |
|--------|-----------|-----------------|
| p95 response time | > 500ms | Fail pipeline |
| Error rate | > 1% | Fail pipeline |
| Throughput | < 200 RPS | Warning (don't fail, but alert) |
| p99 response time | > 2000ms | Warning |

**Universal implementation:** Run your load test tool in headless/CLI mode. After the test, parse the output (CSV, JSON, stdout) with a Python script that checks thresholds and exits with code 1 on breach. CI treats non-zero exit code as failure.

This pattern works identically with any tool. The "performance gate" is not a feature of the tool — it's a 30-line Python script that reads results and asserts.

### 9.3 Distributed Load Generation

When your load test needs more virtual users than a single machine can generate (typically >5,000 for Python-based tools), you need distributed execution.

**The universal architecture:**

```
Coordinator (1): Controls the test, aggregates results, serves dashboard (if any)
Workers (N):     Generate the actual load

Coordinator doesn't generate load — it only coordinates.
Workers don't serve UI — they only generate load.
```

**Tool-specific distributed modes:**

| Tool | Built-in Distributed? | How |
|------|----------------------|-----|
| Locust | Yes | `--master` / `--worker` flags. Workers connect to master over TCP. |
| k6 | Partial | k6 Cloud (paid) or `xk6-distributed` extension (open source). |
| Molotov | No | Run multiple instances manually; aggregate results post-run. |
| Custom asyncio | No | Run on multiple machines; aggregate CSV outputs. |

**In CI (universal pattern):** Use Docker Compose with 1 coordinator container and N worker containers. All share the same test script via a volume mount. The Compose file defines the topology.

### 9.4 Trending and Regression Detection

**Why trending matters:** A single test run tells you "how fast is it now." Trending tells you "is it getting faster or slower over time." Performance regressions are gradual — you only catch them by comparing against history.

**Universal trending approach:**

1. After each performance test run, append key metrics (p95, p99, RPS, error rate, timestamp, git commit SHA) to a persistent store.
2. Persistent store options (all free):
   - SQLite file committed to a `perf-results` branch
   - JSON lines file appended via CI
   - GitHub Pages site with a chart built from the data
3. A comparison script checks: "Is today's p95 more than 20% higher than the 7-day rolling average?" If yes, alert.
4. Publish a trend chart (matplotlib → PNG → GitHub Pages) showing performance over the last 30 runs.

---

## Part 10: Tool-Specific Quick Starts

This section provides just enough to get running with each tool. The concepts from Parts 1–9 apply universally; this section covers only the syntax differences.

### 10.1 Locust Quick Start

```
Install:     pip install locust
Run:         locust -f locustfile.py --host=https://target-api.com
Headless:    locust -f locustfile.py --host=https://target-api.com --headless -u 100 -r 10 -t 5m
CSV output:  --csv=results
Dashboard:   localhost:8089 (built-in web UI)

Key concepts:
  - User class inherits from HttpUser
  - Tasks defined with @task(weight) decorator
  - Think time via wait_time = between(min, max)
  - Sequential flows via SequentialTaskSet
  - Setup/teardown via on_start() / on_stop()
  - Custom validation via catch_response=True + response.failure()
  - Custom load shapes via LoadTestShape class
  - Distributed via --master / --worker flags

Search term: "Locust Python load testing quick start tutorial"
```

### 10.2 Molotov Quick Start

```
Install:     pip install molotov
Run:         molotov loadtest.py --workers 10 --duration 300
CSV output:  Custom (use --statsd or write results in your scenario)
Dashboard:   None built-in (use Grafana + StatsD)

Key concepts:
  - Scenarios defined with @scenario(weight) decorator
  - Native asyncio — uses aiohttp ClientSession directly
  - Think time via await asyncio.sleep()
  - Setup/teardown via @setup / @teardown decorators
  - Global setup via @global_setup / @global_teardown
  - Very lightweight — thin wrapper over aiohttp
  - Better raw concurrency than Locust (asyncio vs gevent)

Search term: "Molotov Python async load testing tutorial"
```

### 10.3 Custom asyncio + aiohttp Quick Start

```
Install:     pip install aiohttp
Run:         python loadtest.py
CSV output:  You build it (write to CSV in your collection logic)
Dashboard:   You build it (matplotlib charts, or push to Grafana)

Key concepts:
  - Full control over everything
  - asyncio.Semaphore for concurrency control
  - aiohttp.ClientSession for connection pooling
  - asyncio.gather() for running N coroutines
  - statistics.quantiles() for percentile computation
  - time.monotonic() for precise timing
  - No framework overhead — maximum performance
  - Best for learning what load testing tools actually do

Search term: "Python aiohttp asyncio load testing custom"
```

### 10.4 pytest-Based Performance Smoke Tests

```
Install:     pip install pytest requests
Run:         pytest tests/performance/ -v
CSV output:  Custom (write timing data in fixtures)
Dashboard:   Allure or custom

Key concepts:
  - Not a real load test tool — limited concurrency
  - Useful for: response time assertions in functional tests
  - Pattern: time each API call, assert < threshold
  - Use @pytest.mark.performance to tag perf tests
  - Run in CI on every merge for single-user latency regression
  - Complements (not replaces) a real load test tool

Search term: "pytest performance testing response time assertions"
```

---

## Terminology Quick Reference

| Term | Definition |
|------|-----------|
| Latency | Time from request sent to response received |
| Throughput | Requests completed per second (RPS/TPS) |
| Concurrency | Number of users active simultaneously |
| p50, p95, p99 | Percentiles of response time distribution |
| Saturation | Point where adding load no longer increases throughput |
| SLI/SLO/SLA | Indicator / Objective / Agreement for service performance |
| Think time | Simulated pause between user actions |
| Ramp-up | Gradually increasing users from 0 to target |
| Breakpoint | The concurrency at which the system fails |
| Long tail | Large gap between median and high-percentile latency |
| N+1 query | A database anti-pattern: 1 query + N sub-queries |
| Connection pool | Pre-allocated set of reusable database connections |
| Virtual user | A simulated user in the load test tool |
| Jitter | Random variation added to backoff/wait times |
| Greenlet | Lightweight cooperative thread (used by Locust/gevent) |
| Coroutine | Async function (used by Molotov/asyncio) |
| Load shape | The pattern of user count over time (ramp, spike, soak, step) |
| Headless mode | Running a load test without the GUI (for CI) |
| Distributed mode | Spreading load generation across multiple machines |
| Performance gate | CI check that fails the build if perf thresholds are breached |

---

*Performance testing is engineering, not tool operation. The value isn't in learning Locust or k6 or any specific tool — it's in understanding load profiles, analyzing results, diagnosing bottlenecks, and communicating findings to stakeholders. Master the thinking, and any tool becomes a 1-day learn.*
