# Master SDET Implementation Plan

**Subtitle:** A Sequential Engineering Blueprint for Becoming a Developer Who Specializes in Testing  
**Version:** 1.0  
**Date:** March 2026  
**Prerequisite audit:** This plan was derived from a gap analysis of `QA_Learning_Roadmap.md` and `QA_Roadmap_Deep_Acceptance_Mapping.md`. Every section marked with **[GAP]** addresses a deficiency found in those documents. Sections marked **[DEEPEN]** expand on topics that were mentioned but insufficiently covered.

---

## How to Use This Document

1. **Work sequentially.** Each tier builds on the previous. Do not skip ahead.
2. **Every micro-topic is searchable.** Copy the exact sub-heading (e.g., "Python Descriptor Protocol") into Google, YouTube, or ChatGPT to find study material instantly.
3. **Exercises are non-trivial by design.** If an exercise takes less than 90 minutes, you did not go deep enough.
4. **Commit everything.** Every exercise result goes into your `qa-learning-journey` repo with a descriptive commit message.
5. **Time estimate:** 6–8 hours/week across 9–10 months for full completion. Prioritize Tiers 1–4 for interview readiness within 4–5 months.

---

## Table of Contents

- [Tier 1: Foundational Software Engineering](#tier-1-foundational-software-engineering)
- [Tier 2: Python as an Engineering Language](#tier-2-python-as-an-engineering-language)
- [Tier 3: Testing Frameworks — Deep Internals](#tier-3-testing-frameworks--deep-internals)
- [Tier 4: API & Protocol Engineering](#tier-4-api--protocol-engineering)
- [Tier 5: UI Automation Architecture](#tier-5-ui-automation-architecture)
- [Tier 6: Test Architecture & Design Patterns](#tier-6-test-architecture--design-patterns)
- [Tier 7: Data Engineering for Test](#tier-7-data-engineering-for-test)
- [Tier 8: Containerization & Orchestration Engineering](#tier-8-containerization--orchestration-engineering)
- [Tier 9: CI/CD Pipeline Engineering](#tier-9-cicd-pipeline-engineering)
- [Tier 10: Observability & Monitoring Engineering](#tier-10-observability--monitoring-engineering)
- [Tier 11: Cloud Infrastructure for SDET](#tier-11-cloud-infrastructure-for-sdet)
- [Tier 12: Architectural Framework Design](#tier-12-architectural-framework-design)
- [Appendix A: Mastery Validation Exercises (Cross-Tier)](#appendix-a-mastery-validation-exercises-cross-tier)
- [Appendix B: Interview Simulation Bank](#appendix-b-interview-simulation-bank)

---

## Tier 1: Foundational Software Engineering

> **Goal:** Build the habits and mental models of a software engineer, not a script writer.

### 1.1 Development Environment Mastery

#### 1.1.1 Shell Proficiency (Bash/Zsh)

| Micro-Topic | What to Know | Search Term |
|-------------|-------------|-------------|
| File system navigation | `cd`, `ls -la`, `pwd`, `tree`, symlinks (`ln -s`), `find` with `-exec` | "Bash file system navigation tutorial" |
| Text processing pipeline | `grep`, `sed`, `awk`, `cut`, `sort`, `uniq`, `wc`, `xargs` as a chain | "Unix text processing pipeline examples" |
| Process management | `ps aux`, `kill`, `nohup`, `bg`, `fg`, `jobs`, `&`, signals (SIGTERM, SIGKILL, SIGHUP) | "Linux process management tutorial" |
| Environment variables | `export`, `env`, `printenv`, `.bashrc` vs `.bash_profile` vs `.zshrc` load order | "Bash environment variables load order" |
| Shell scripting constructs | `if/elif/else`, `for/while`, `case`, functions, `set -euo pipefail`, trap, exit codes, `$?` | "Bash scripting best practices set -euo pipefail" |
| I/O redirection | `>`, `>>`, `2>&1`, `<`, `|`, `/dev/null`, heredocs (`<<EOF`), process substitution (`<()`) | "Bash I/O redirection and process substitution" |
| SSH essentials | Key generation (`ssh-keygen`), `~/.ssh/config`, tunneling (`-L`, `-R`), `scp`, `rsync` | "SSH config and tunneling tutorial" |
| `jq` for JSON | Parse, filter, transform JSON from CLI — essential for API debugging | "jq JSON command line tutorial" |
| `curl` mastery | Methods, headers, auth, data, verbose mode, following redirects, certificate handling | "curl advanced usage examples" |

**Exercise 1.1.1 — [GAP]:** Write a bash script that: (a) accepts a GitHub repo URL as argument, (b) clones it, (c) creates a Python venv, (d) installs dependencies from `requirements.txt` or `pyproject.toml` (detect which exists), (e) runs `pytest` with JUnit XML output, (f) parses the XML with `grep`/`sed` to extract pass/fail counts, (g) exits with code 1 if any test failed. Use `set -euo pipefail` and `trap` for cleanup.

#### 1.1.2 Git as an Engineering Tool

| Micro-Topic | What to Know | Search Term |
|-------------|-------------|-------------|
| Branching models | Git Flow, GitHub Flow, Trunk-Based Development — trade-offs | "Git branching strategies comparison" |
| Interactive rebase | `git rebase -i` — squash, fixup, reword, reorder, drop | "Git interactive rebase tutorial" |
| Cherry-pick | `git cherry-pick <sha>`, handling conflicts, `-x` flag for traceability | "Git cherry-pick with conflict resolution" |
| Bisect | `git bisect start`, `good`, `bad`, automated bisect with a script | "Git bisect automated script example" |
| Reflog | `git reflog` — recovering lost commits, understanding HEAD movement | "Git reflog recovery tutorial" |
| Stash advanced | `git stash push -m`, `stash apply` vs `pop`, `stash show -p`, partial stashing (`--patch`) | "Git stash advanced usage" |
| Worktrees | `git worktree add` — working on multiple branches simultaneously without stashing | "Git worktree tutorial" |
| Hooks | Client-side hooks (`pre-commit`, `commit-msg`, `pre-push`) — what runs where and when | "Git hooks client side tutorial" |
| Submodules vs subtrees | When each is appropriate, how to update, gotchas | "Git submodules vs subtrees comparison" |
| Blame and log archaeology | `git blame`, `git log -S` (pickaxe), `git log --follow`, `git shortlog` | "Git blame and pickaxe search" |

**Exercise 1.1.2 — [DEEPEN]:** In your learning repo: (a) Create 10 commits across 3 branches with intentional merge conflicts. (b) Use `git bisect` with a test script to find a "bug" you introduced. (c) Use `git reflog` to recover a commit you "accidentally" deleted via `reset --hard`. (d) Write a `commit-msg` hook that rejects commits without a JIRA-style ticket prefix (e.g., `PROJ-123:`).

#### 1.1.3 Python Environment Engineering

| Micro-Topic | What to Know | Search Term |
|-------------|-------------|-------------|
| `pyenv` | Install, manage, switch Python versions per-project (`.python-version`) | "pyenv install and usage tutorial" |
| `venv` internals | What `pyvenv.cfg` does, how `sys.prefix` changes, `include-system-site-packages` | "Python venv internals pyvenv.cfg" |
| `pip` advanced | `--constraint`, `--find-links`, `--index-url` (private PyPI), editable installs (`-e .`) | "pip advanced options constraints editable" |
| Poetry deep | Dependency groups, extras, scripts, `poetry export`, `poetry build`, publishing, `poetry self add` plugins | "Poetry Python advanced usage groups extras" |
| `pyproject.toml` anatomy | `[build-system]`, `[project]`, `[tool.*]` sections — understanding PEP 517/518/621 | "pyproject.toml PEP 621 full anatomy" |
| Packaging: wheels & sdists | `python -m build`, `.whl` vs `.tar.gz`, when to publish an internal package | "Python packaging wheel sdist tutorial" |
| Private package registries | AWS CodeArtifact, GCP Artifact Registry, self-hosted (devpi) — consuming and publishing | "Python private PyPI registry setup" |

**Exercise 1.1.3 — [GAP]:** Build a small Python library (e.g., a retry utility), package it with Poetry, build a wheel, install it in a separate project via `pip install ./dist/retry_util-0.1.0-py3-none-any.whl`, and verify it works. Then configure `poetry export` to generate a constraints file for CI.

---

### 1.2 Software Design Principles [GAP]

> **This entire section is missing from the original roadmap.** An SDET who cannot reason about design is limited to writing scripts, not engineering frameworks.

#### 1.2.1 SOLID Principles

| Principle | What to Know | SDET Application | Search Term |
|-----------|-------------|-------------------|-------------|
| Single Responsibility | One class/module, one reason to change | Each helper module wraps one API domain. Each fixture does one thing. | "SOLID Single Responsibility Principle Python" |
| Open/Closed | Open for extension, closed for modification | Base API client extended via subclassing for different services without modifying the base | "Open Closed Principle Python examples" |
| Liskov Substitution | Subtypes must be substitutable for base types | `ChromeDriver` and `FirefoxDriver` both usable where `WebDriver` is expected | "Liskov Substitution Principle Python" |
| Interface Segregation | No client should depend on methods it doesn't use | Split `TestClient` into `APIClient` + `AuthClient` instead of one god-class | "Interface Segregation Principle Python abc" |
| Dependency Inversion | Depend on abstractions, not concretions | Fixtures inject dependencies; test code never constructs its own HTTP clients | "Dependency Inversion Principle Python" |

#### 1.2.2 Design Patterns for Test Automation

| Pattern | What It Solves | Where You'll Use It | Search Term |
|---------|---------------|---------------------|-------------|
| Factory | Creating test data objects with sane defaults | User factories, system factories, policy factories | "Factory design pattern Python" |
| Builder | Constructing complex objects step-by-step | Building API request payloads with optional fields | "Builder design pattern Python" |
| Strategy | Swapping algorithms at runtime | Different auth strategies (API key, OAuth, JWT) injected into the same client | "Strategy design pattern Python" |
| Observer | Reacting to events | Custom pytest hooks that react to test pass/fail/skip | "Observer design pattern Python" |
| Singleton | One instance globally | Database connection pool, configuration object | "Singleton design pattern Python" |
| Adapter | Bridging incompatible interfaces | Wrapping a third-party SDK to match your framework's interface | "Adapter design pattern Python" |
| Page Object Model | Encapsulating UI page structure | Playwright page classes with locators and actions | "Page Object Model Playwright Python" |
| Facade | Simplifying complex subsystems | A single `TestEnvironment` class that orchestrates Docker, DB seed, and service health checks | "Facade design pattern Python" |

**Exercise 1.2 — [GAP]:** Refactor a flat script (e.g., one that creates a user via API, assigns them to a group, and verifies the assignment) into a design that uses: a `UserFactory` (Factory), an `APIClient` base with `JumpCloudClient(APIClient)` (Adapter + DI), and a `RequestBuilder` (Builder) for constructing payloads. Write tests for each component in isolation.

---

### 1.3 Algorithmic Thinking for SDET [GAP]

> The original roadmap stops at Codewars 6kyu. An SDET needs more: graph traversal for dependency analysis, state machines for test flow modeling, and combinatorial generation.

| Micro-Topic | Why an SDET Needs It | Search Term |
|-------------|---------------------|-------------|
| Hash maps and sets | O(1) lookup for deduplication, test data indexing, assertion on large datasets | "Python dict set time complexity" |
| Graph traversal (BFS/DFS) | Dependency resolution (which tests depend on which services), service topology mapping | "BFS DFS Python implementation" |
| State machines | Modeling user lifecycle (created → activated → suspended → deleted) for test coverage | "Finite state machine Python implementation" |
| Combinatorial/pairwise testing | Reducing test matrix from N^M to manageable subsets using pairwise algorithms | "Pairwise testing allpairs Python" |
| Topological sort | Determining test execution order based on dependencies | "Topological sort Python" |
| Complexity analysis (Big-O) | Identifying O(n^2) loops in test setup, justifying optimization decisions | "Big O notation Python examples" |
| Tree traversal | Parsing nested JSON responses, DOM tree navigation, org hierarchy testing | "Tree traversal recursive iterative Python" |
| Regex engine mechanics | Understanding greedy vs lazy, lookahead/lookbehind, backtracking costs | "Python regex lookahead lookbehind tutorial" |

**Exercise 1.3 — [GAP]:** (a) Model a user lifecycle (states: created, invited, activated, suspended, locked, deleted; transitions: activate, suspend, unlock, delete, reinvite) as a state machine in Python. Write a function that takes a starting state and a list of transitions and returns the final state, raising an `InvalidTransition` error for illegal moves. (b) Write tests that verify all valid paths and all invalid transitions. (c) Use `itertools.product` to generate all possible transition sequences of length 3, then filter to valid ones — this is your test coverage matrix.

---

## Tier 2: Python as an Engineering Language

> **Goal:** Write Python like a developer, not like someone who learned just enough to call APIs.

### 2.1 Core Language Mechanics [GAP — most of these are absent]

#### 2.1.1 Functions — Advanced

| Micro-Topic | What to Know | Search Term |
|-------------|-------------|-------------|
| First-class functions | Functions as arguments, return values, stored in variables/dicts | "Python first class functions tutorial" |
| Closures | Inner function capturing outer scope; use for factory functions | "Python closures explained" |
| `*args` and `**kwargs` deep | Unpacking, forwarding to wrapped functions, combining with explicit params | "Python args kwargs advanced examples" |
| `functools.partial` | Pre-filling arguments — useful for creating specialized API callers from a generic one | "Python functools partial usage" |
| `functools.wraps` | Preserving metadata in decorators — critical for debuggability | "Python functools wraps decorator" |
| `functools.lru_cache` | Memoization for expensive computations (e.g., caching API schema parsing) | "Python lru_cache memoization" |
| `functools.reduce` | Accumulating results — useful in data pipelines | "Python functools reduce examples" |
| Lambda functions | Anonymous functions for `sorted(key=)`, `filter()`, `map()` — and when NOT to use them | "Python lambda best practices" |
| Function annotations and overloads | `typing.overload` for multi-signature functions | "Python typing overload decorator" |

#### 2.1.2 Decorators — Full Depth [DEEPEN]

| Micro-Topic | What to Know | Search Term |
|-------------|-------------|-------------|
| Simple decorator (no args) | Function that wraps another, preserves `__name__` via `@wraps` | "Python decorator basic tutorial" |
| Decorator with arguments | Triple-nested function pattern: `def decorator(arg)` → `def wrapper(func)` → `def inner(*args)` | "Python decorator with arguments" |
| Class-based decorators | Using `__call__` on a class — cleaner state management than closures | "Python class based decorator" |
| Stacked decorators | Execution order (bottom-up application, top-down execution) | "Python stacked decorators execution order" |
| Decorators for logging | `@log_call` that logs function name, args, return value, execution time | "Python logging decorator implementation" |
| Decorators for retry | `@retry(max_attempts=3, backoff=2)` with exponential backoff | "Python retry decorator exponential backoff" |
| Decorators for auth | `@requires_admin` that checks context before executing | "Python authorization decorator" |
| `@property` deep | Getters, setters, deleters, computed properties, caching with `@cached_property` | "Python property decorator advanced" |
| `@staticmethod` vs `@classmethod` | When to use each, `cls` parameter, factory methods via `@classmethod` | "Python staticmethod classmethod difference" |
| Decorators in pytest | How `@pytest.fixture`, `@pytest.mark.*`, `@given`, `@when`, `@then` work internally | "pytest fixture decorator internals" |

**Exercise 2.1.2 — [GAP]:** Build a decorator library (`test_decorators.py`) containing: (a) `@timed(threshold_ms=500)` — logs a warning if the decorated function exceeds the threshold, (b) `@retry(max_attempts=3, on_exceptions=(ConnectionError, TimeoutError), backoff_factor=2)` — retries with exponential backoff, (c) `@validate_response(schema: dict)` — validates the return value against a JSON Schema, (d) `@tag(name="smoke", priority="p0")` — attaches metadata readable via `func.tag_name` and `func.tag_priority`. Write unit tests for each. Stack `@timed` and `@retry` on a single function and verify both execute correctly.

#### 2.1.3 Generators and Iterators [GAP]

| Micro-Topic | What to Know | Search Term |
|-------------|-------------|-------------|
| `yield` keyword | Lazy evaluation, memory efficiency for large datasets | "Python yield generator tutorial" |
| Generator expressions | `(x for x in range(10**9))` vs list comprehension — memory difference | "Python generator expression vs list comprehension" |
| `yield from` | Delegating to sub-generators, flattening nested iteration | "Python yield from delegation" |
| `itertools` module | `chain`, `islice`, `groupby`, `product`, `combinations`, `permutations`, `count`, `cycle`, `tee` | "Python itertools practical examples" |
| Custom iterator class | `__iter__` and `__next__` protocol, `StopIteration` | "Python custom iterator class" |
| Infinite generators | Generating test data on demand (infinite user IDs, rotating credentials) | "Python infinite generator examples" |
| `send()` and `throw()` | Coroutine-style generators — advanced, but useful for understanding `asyncio` foundations | "Python generator send throw" |

**Exercise 2.1.3 — [GAP]:** Write a test data generator that: (a) Yields unique user objects indefinitely (never repeats an email or username), (b) Accepts a `send()` call to change the "domain" of generated emails mid-stream, (c) Can be sliced with `itertools.islice(gen, 100)` to get exactly 100 users, (d) Uses `itertools.product` to generate all combinations of `[admin, user, readonly]` roles and `[active, suspended, invited]` states — yielding 9 test scenarios.

#### 2.1.4 Context Managers [DEEPEN]

| Micro-Topic | What to Know | Search Term |
|-------------|-------------|-------------|
| `with` statement protocol | `__enter__` and `__exit__`, exception handling in `__exit__` | "Python context manager protocol" |
| `contextlib.contextmanager` | Decorator that turns a generator function into a context manager | "Python contextlib contextmanager" |
| `contextlib.ExitStack` | Managing multiple context managers dynamically | "Python ExitStack multiple context managers" |
| `contextlib.suppress` | Ignoring specific exceptions cleanly | "Python contextlib suppress" |
| Custom context managers for test | DB transaction rollback, temporary file cleanup, API resource lifecycle | "Python custom context manager examples" |
| Async context managers | `async with`, `__aenter__`, `__aexit__` | "Python async context manager" |

**Exercise 2.1.4 — [GAP]:** Build: (a) `APIResource(client, endpoint, payload)` context manager — on enter, creates a resource via POST and returns the ID; on exit, deletes it via DELETE (guaranteed cleanup even on test failure), (b) `DatabaseTransaction(connection)` — on enter, begins transaction; on exit, rolls back (for test isolation), (c) Use `ExitStack` to manage 5 `APIResource` instances in a single test, ensuring all are cleaned up.

#### 2.1.5 Object-Oriented Python — Advanced [DEEPEN]

| Micro-Topic | What to Know | Search Term |
|-------------|-------------|-------------|
| Abstract Base Classes (`abc`) | `ABC`, `@abstractmethod`, enforcing interface contracts | "Python abc abstract base class" |
| Multiple inheritance and MRO | Method Resolution Order, `super()` in diamond inheritance, `__mro__` | "Python MRO method resolution order" |
| Mixins | Adding behavior via multiple inheritance without full class hierarchy | "Python mixin pattern" |
| `__slots__` | Memory optimization, preventing dynamic attribute creation | "Python __slots__ memory optimization" |
| `__new__` vs `__init__` | Object creation vs initialization, singleton via `__new__` | "Python __new__ vs __init__" |
| Descriptor protocol | `__get__`, `__set__`, `__delete__` — how `@property` works under the hood | "Python descriptor protocol tutorial" |
| Metaclasses | `type` as metaclass, `__init_subclass__`, when to use (almost never, but understand them) | "Python metaclasses practical guide" |
| Dataclasses deep | `field()`, `__post_init__`, frozen, `asdict()`, `astuple()`, inheritance with dataclasses | "Python dataclasses advanced features" |
| `__repr__` vs `__str__` | Debugging vs display, making objects inspectable | "Python repr vs str best practices" |
| Comparison methods | `__eq__`, `__lt__`, `__hash__`, `@total_ordering` | "Python comparison methods total_ordering" |
| Protocols (structural subtyping) | `typing.Protocol` for duck typing with type safety — PEP 544 | "Python typing Protocol structural subtyping" |

**Exercise 2.1.5 — [GAP]:** Design a test model hierarchy: (a) `BaseEntity(ABC)` with abstract methods `create()`, `delete()`, `to_dict()`, (b) `User(BaseEntity)` and `System(BaseEntity)` concrete implementations, (c) `TimestampMixin` that adds `created_at` and `updated_at` tracking to any entity, (d) `AuditableEntity(TimestampMixin, BaseEntity)` combining both, (e) Use `__slots__` on `User` and benchmark memory vs without slots for 100,000 instances, (f) Implement `__repr__`, `__eq__`, and `__hash__` so instances work correctly in sets and as dict keys.

#### 2.1.6 Exception Handling Engineering [GAP]

| Micro-Topic | What to Know | Search Term |
|-------------|-------------|-------------|
| Custom exception hierarchies | Base `FrameworkError` → `APIError` → `AuthenticationError`, `NotFoundError`, `RateLimitError` | "Python custom exception hierarchy design" |
| Exception chaining | `raise NewError() from original_error` — preserving root cause | "Python exception chaining from" |
| `try/except/else/finally` | `else` runs only if no exception; `finally` always runs | "Python try except else finally" |
| Context in exceptions | Attaching request/response data, timestamps, correlation IDs to exceptions | "Python exception context information" |
| Warning framework | `warnings.warn()`, `@pytest.warns`, deprecation warnings | "Python warnings module usage" |
| `assert` vs explicit checks | `assert` is removed with `-O` flag — never use for production validation | "Python assert vs explicit exception" |

**Exercise 2.1.6 — [GAP]:** Build a custom exception hierarchy for your test framework: `FrameworkError` → `APIError(FrameworkError)` with `status_code`, `response_body`, `request_url` attributes → `AuthError(APIError)`, `NotFoundError(APIError)`, `RateLimitError(APIError)` with a `retry_after` attribute. Write a `handle_response(response)` function that raises the correct exception based on status codes. Write tests that verify the right exception type, message, and attributes for each code.

#### 2.1.7 Concurrency and Parallelism [GAP]

| Micro-Topic | What to Know | Search Term |
|-------------|-------------|-------------|
| The GIL | What it is, what it affects (CPU-bound vs I/O-bound), why it matters for test execution | "Python GIL global interpreter lock explained" |
| `threading` module | Threads for I/O-bound tasks (parallel API calls), `Lock`, `Event`, `Semaphore` | "Python threading module tutorial" |
| `concurrent.futures` | `ThreadPoolExecutor` and `ProcessPoolExecutor`, `as_completed`, `map` | "Python concurrent.futures tutorial" |
| `asyncio` fundamentals | `async/await`, `asyncio.run()`, `asyncio.gather()`, event loop | "Python asyncio tutorial beginner" |
| `aiohttp` | Async HTTP client for high-concurrency API testing | "Python aiohttp client tutorial" |
| `multiprocessing` | Process-based parallelism for CPU-bound tasks, `Pool`, shared state pitfalls | "Python multiprocessing Pool tutorial" |
| Thread safety in test frameworks | Why shared fixtures under `pytest-xdist` can race, how to use locks or separate state | "pytest-xdist thread safety fixtures" |

**Exercise 2.1.7 — [GAP]:** (a) Write a script that makes 100 API calls to a public API (e.g., `httpbin.org/delay/1`): first sequentially, then with `ThreadPoolExecutor(max_workers=20)`, then with `asyncio` + `aiohttp`. Compare wall-clock times. (b) Write a `ParallelAPIClient` class that accepts a list of requests and executes them concurrently with a configurable concurrency limit, collecting results and errors.

#### 2.1.8 The `collections` Module [GAP]

| Micro-Topic | What to Know | Search Term |
|-------------|-------------|-------------|
| `defaultdict` | Auto-initializing dicts — grouping test results by status | "Python defaultdict examples" |
| `Counter` | Counting occurrences — error frequency analysis | "Python Counter most_common" |
| `namedtuple` | Lightweight immutable objects — test parameters, API responses | "Python namedtuple usage" |
| `deque` | Efficient append/pop from both ends — log buffering, sliding windows | "Python deque operations" |
| `OrderedDict` | Insertion-ordered dict (pre-3.7 compatibility, `move_to_end`) | "Python OrderedDict usage" |
| `ChainMap` | Layered lookups — config overrides (env → file → defaults) | "Python ChainMap config example" |

---

### 2.2 Pydantic — Deep Mastery [DEEPEN]

> The original roadmap mentions "Pydantic / dataclasses" as a one-liner. Pydantic is the backbone of modern API test validation.

| Micro-Topic | What to Know | Search Term |
|-------------|-------------|-------------|
| `BaseModel` fundamentals | Field declarations, type coercion, `model_dump()`, `model_validate()` | "Pydantic v2 BaseModel tutorial" |
| Validators | `@field_validator`, `@model_validator`, `mode='before'` vs `mode='after'` | "Pydantic v2 field_validator model_validator" |
| Custom types | `Annotated`, `BeforeValidator`, `AfterValidator`, `PlainSerializer` | "Pydantic v2 custom types Annotated" |
| Nested models | Models containing other models, `List[ChildModel]`, recursive models | "Pydantic nested models example" |
| Model inheritance | Base response model → specialized response models | "Pydantic model inheritance" |
| Discriminated unions | `Literal` + `Discriminator` for polymorphic responses | "Pydantic discriminated union" |
| JSON Schema generation | `model.model_json_schema()` for contract validation | "Pydantic JSON schema generation" |
| Settings management | `BaseSettings` for environment-based config (replaces raw `os.environ.get`) | "Pydantic BaseSettings environment variables" |
| Serialization control | `model_dump(exclude_none=True, by_alias=True)`, aliases, field exclusion | "Pydantic serialization exclude alias" |

**Exercise 2.2 — [DEEPEN]:** Model a complete API response ecosystem: (a) `PaginatedResponse[T]` generic model with `results: List[T]`, `total_count: int`, `next_url: Optional[HttpUrl]`, (b) `UserResponse` with validators (email must be valid, `created_at` must parse from ISO string), (c) `ErrorResponse` with `status_code`, `message`, `detail: Optional[dict]`, (d) `ApiResponse = Union[PaginatedResponse[UserResponse], ErrorResponse]` discriminated by a field. Write tests that validate real API JSON against these models.

---

## Tier 3: Testing Frameworks — Deep Internals

> **Goal:** Understand pytest not as a user, but as a framework engineer who can extend it.

### 3.1 Pytest Internals [GAP]

#### 3.1.1 The Collection Phase

| Micro-Topic | What to Know | Search Term |
|-------------|-------------|-------------|
| Test discovery | `conftest.py` loading order, `__init__.py` effect, `rootdir` detection | "pytest test discovery conftest loading order" |
| `conftest.py` layering | Root conftest vs package conftest vs module conftest — fixture scope and override rules | "pytest conftest.py layering scoping" |
| `pytest_collect_modifyitems` hook | Reordering, deselecting, or modifying tests after collection | "pytest pytest_collect_modifyitems hook" |
| `pytest_collection_modifyitems` | Sorting tests (e.g., smoke first), deselecting by custom criteria | "pytest modify test collection order" |
| Custom collectors | `pytest_pycollect_makeitem` — adding custom test item types | "pytest custom collector" |

#### 3.1.2 Fixtures — Engineering Level [DEEPEN]

| Micro-Topic | What to Know | Search Term |
|-------------|-------------|-------------|
| Fixture scopes | `function`, `class`, `module`, `package`, `session` — lifecycle and caching | "pytest fixture scopes lifecycle" |
| Fixture factories | Fixture that returns a factory function (create many objects, each with different config) | "pytest fixture factory pattern" |
| Dynamic fixtures | Using `request.getfixturevalue()` to get fixtures by name at runtime | "pytest request getfixturevalue dynamic" |
| Fixture finalization | `yield` vs `addfinalizer` — when each is appropriate | "pytest fixture yield vs addfinalizer" |
| Fixture parametrize | `@pytest.fixture(params=[...])` with `ids` — data-driven fixture setup | "pytest parametrize fixture params ids" |
| Fixture dependency graph | How pytest resolves fixture dependencies, circular dependency detection | "pytest fixture dependency resolution" |
| `autouse` fixtures | When to use (sparingly), scope implications, override rules | "pytest autouse fixture best practices" |
| `tmp_path` and `tmp_path_factory` | Built-in fixtures for temporary file handling in tests | "pytest tmp_path fixture" |

#### 3.1.3 Hooks [GAP]

| Hook | What It Does | SDET Use Case | Search Term |
|------|-------------|---------------|-------------|
| `pytest_configure` | Early configuration, registering markers, plugins | Registering custom markers, environment setup | "pytest pytest_configure hook" |
| `pytest_sessionstart` | Runs once at session start | Global resource allocation (DB pool, API token) | "pytest pytest_sessionstart hook" |
| `pytest_runtest_makereport` | Access test result (pass/fail/error) per phase (setup/call/teardown) | Custom reporting, failure screenshots, Datadog tagging | "pytest pytest_runtest_makereport example" |
| `pytest_terminal_summary` | Add content to the terminal summary | Custom summary (flaky count, slowest tests, environment info) | "pytest pytest_terminal_summary hook" |
| `pytest_addoption` | Add custom CLI options | `--env staging`, `--browser chrome`, `--api-key <key>` | "pytest pytest_addoption custom options" |
| `pytest_generate_tests` | Dynamic parametrize from external sources (CSV, DB, API) | Loading test data from files or services at collection time | "pytest pytest_generate_tests dynamic" |
| `pytest_exception_interact` | Debug on failure | Dropping into debugger, capturing extra diagnostics | "pytest pytest_exception_interact hook" |

#### 3.1.4 Plugin Authoring [GAP]

| Micro-Topic | What to Know | Search Term |
|-------------|-------------|-------------|
| Plugin as `conftest.py` | Every conftest is a plugin — hooks, fixtures, markers | "pytest conftest as plugin" |
| Plugin as installable package | `setuptools` entry point `pytest11`, distributing via pip | "pytest plugin installable package" |
| `pytest_plugins` variable | Declaring plugin dependencies in conftest | "pytest pytest_plugins variable" |
| Hook specification vs implementation | `@pytest.hookspec` vs `@pytest.hookimpl`, `tryfirst`, `trylast` | "pytest hookspec hookimpl" |

**Exercise 3.1 — [GAP]:** Build a pytest plugin (`conftest.py` first, then extract to a package): (a) `pytest_addoption` adds `--env` (staging/production/local) and `--slow` (include slow tests), (b) `pytest_configure` registers markers `smoke`, `regression`, `slow`, (c) `pytest_collection_modifyitems` deselects `@pytest.mark.slow` tests unless `--slow` is passed, (d) `pytest_runtest_makereport` captures failure details and writes them to a JSON file with test name, duration, error message, and timestamp, (e) `pytest_terminal_summary` prints a summary: "X passed, Y failed, Z slow tests skipped, total time: N seconds".

### 3.2 pytest-bdd — Beyond Basics [DEEPEN]

| Micro-Topic | What to Know | Search Term |
|-------------|-------------|-------------|
| Step argument converters | Custom type converters with `parsers.cfparse` and `parsers.re` | "pytest-bdd step argument parsers cfparse" |
| Scenario outlines with complex types | Injecting lists, dicts, JSON via Examples tables | "pytest-bdd scenario outline complex data" |
| Shared steps across features | Step reuse via conftest, avoiding duplication | "pytest-bdd shared step definitions" |
| Tags as markers | Using Gherkin tags to drive pytest markers/fixtures | "pytest-bdd tags markers mapping" |
| Feature file organization | One feature per file vs grouped, naming conventions, directory structure | "pytest-bdd feature file organization" |
| Background vs fixtures | When to use Gherkin `Background` vs pytest fixture for shared setup | "pytest-bdd background vs fixture" |
| Reporting integration | Allure + pytest-bdd step tracking | "pytest-bdd allure reporting steps" |

### 3.3 Parametrize — Advanced Patterns [DEEPEN]

| Micro-Topic | What to Know | Search Term |
|-------------|-------------|-------------|
| `@pytest.mark.parametrize` basics | Tuples, `ids`, `marks` within parametrize | "pytest parametrize ids marks" |
| Stacked parametrize | Multiple `@parametrize` decorators = cartesian product | "pytest stacked parametrize cartesian" |
| `indirect` parametrize | Passing parametrized values to fixtures | "pytest parametrize indirect fixture" |
| Parametrize from external data | CSV, JSON, YAML, database — loading at collection time | "pytest parametrize from json file" |
| Conditional parametrize | Skip certain parameter combos based on environment | "pytest parametrize conditional skip" |

**Exercise 3.3 — [DEEPEN]:** Create a parametrized test suite for a CRUD API: (a) Parametrize HTTP method × valid/invalid payload × expected status code (at least 12 combinations), (b) Use `ids` for readable test names, (c) Mark invalid-auth combos with `pytest.param(..., marks=pytest.mark.xfail)`, (d) Load an additional set of edge-case parameters from a JSON file using `pytest_generate_tests`.

### 3.4 Parallel Test Execution with pytest-xdist [GAP]

| Micro-Topic | What to Know | Search Term |
|-------------|-------------|-------------|
| `pytest-xdist` basics | `-n auto`, `-n 4`, `--dist loadscope`, `--dist loadfile` | "pytest-xdist parallel execution tutorial" |
| Worker isolation | Each worker gets its own process — no shared memory | "pytest-xdist worker isolation" |
| Session-scoped fixture under xdist | `FileLock` for one-time setup across workers | "pytest-xdist session fixture filelock" |
| Test grouping | `--dist loadscope` groups by module/class, `--dist loadfile` by file | "pytest-xdist distribution modes" |
| Database isolation | Each worker gets its own DB schema/transaction | "pytest-xdist database isolation strategy" |
| Ordering and dependencies | `pytest-ordering` + xdist considerations | "pytest test ordering parallel execution" |

**Exercise 3.4 — [GAP]:** Take an existing test suite (20+ tests) and: (a) Run with `pytest -n 4`, identify any failures due to shared state, (b) Fix the shared state issues using fixture isolation and `FileLock` for session setup, (c) Benchmark: sequential time vs 4-worker time, calculate actual speedup vs theoretical.

---

## Tier 4: API & Protocol Engineering

> **Goal:** Test any API protocol with confidence and deep understanding of the network layer.

### 4.1 HTTP Protocol Deep Dive [DEEPEN]

| Micro-Topic | What to Know | Search Term |
|-------------|-------------|-------------|
| HTTP/1.1 vs HTTP/2 | Multiplexing, header compression, server push, binary framing | "HTTP/1.1 vs HTTP/2 differences explained" |
| Request/response lifecycle | DNS → TCP → TLS → HTTP → response parsing → connection pooling | "HTTP request lifecycle complete" |
| Headers deep | `Content-Type`, `Accept`, `Authorization`, `Cache-Control`, `ETag`, `If-None-Match`, `X-Request-ID` | "HTTP headers comprehensive guide" |
| Status codes — the non-obvious ones | 201, 202, 204, 206, 301 vs 302 vs 307, 304, 401 vs 403, 409, 422, 429, 503 | "HTTP status codes when to use which" |
| Content negotiation | `Accept` header, `Content-Type` negotiation, multipart | "HTTP content negotiation explained" |
| Cookies and sessions | `Set-Cookie`, `Cookie`, `SameSite`, `Secure`, `HttpOnly`, session management | "HTTP cookies session management security" |
| CORS | Preflight requests, `Access-Control-*` headers, why it matters for UI test debugging | "CORS preflight request explained" |
| Caching mechanisms | `ETag`, `Last-Modified`, `Cache-Control` directives, conditional requests | "HTTP caching mechanisms tutorial" |
| Connection pooling | `requests.Session()`, keep-alive, connection reuse — performance implications | "Python requests Session connection pooling" |

### 4.2 Authentication & Authorization Protocols [GAP]

| Micro-Topic | What to Know | Search Term |
|-------------|-------------|-------------|
| API Keys | Header-based, query-param-based, rotation, scoping | "API key authentication best practices" |
| OAuth 2.0 flows | Authorization Code, Client Credentials, PKCE, Implicit (deprecated) — when each is used | "OAuth 2.0 flows explained" |
| JWT anatomy | Header.Payload.Signature, `HS256` vs `RS256`, claims (`sub`, `exp`, `iat`, `aud`), verification | "JWT JSON Web Token anatomy verification" |
| OIDC | Building on OAuth 2.0, ID tokens, UserInfo endpoint | "OpenID Connect OIDC tutorial" |
| SAML | Assertions, IdP vs SP, SSO flow — high-level understanding | "SAML SSO flow explained" |
| mTLS | Mutual TLS, client certificates, certificate pinning | "mTLS mutual TLS client certificate" |
| Token refresh | Refresh token flow, handling expired tokens in test automation | "OAuth refresh token automation" |
| RBAC testing | Testing role-based access: admin, user, readonly, cross-tenant | "RBAC testing strategy API" |

**Exercise 4.2 — [GAP]:** Build an `AuthProvider` abstraction with implementations for: (a) `APIKeyAuth` (injects `x-api-key` header), (b) `BearerTokenAuth` (injects `Authorization: Bearer <token>`), (c) `OAuth2ClientCredentials` (fetches token from token endpoint, caches it, auto-refreshes on 401). Write an `APIClient` that accepts any `AuthProvider` via constructor injection. Test all three against `httpbin.org` or a local mock.

### 4.3 Network Protocol Literacy [GAP]

| Micro-Topic | What to Know | Search Term |
|-------------|-------------|-------------|
| TCP/IP fundamentals | 3-way handshake, ports, sockets, `TIME_WAIT`, `netstat`/`ss` | "TCP IP handshake explained simply" |
| DNS resolution | A/AAAA/CNAME records, TTL, `dig`, `nslookup`, DNS caching issues in tests | "DNS resolution process dig command" |
| TLS/SSL handshake | Certificate chain, CA verification, SNI, `openssl s_client` for debugging | "TLS SSL handshake step by step" |
| Certificate debugging | Self-signed certs, expired certs, `requests verify=False` implications, `certifi` | "Python requests SSL certificate verification" |
| Proxy interception | `mitmproxy` for debugging, `http_proxy`/`https_proxy` env vars | "mitmproxy API debugging tutorial" |
| WebSocket protocol | Upgrade handshake, frames, `ping/pong`, testing with `websockets` library | "WebSocket protocol Python testing" |
| gRPC protocol | HTTP/2 based, Protocol Buffers, streaming types (unary, server, client, bidirectional) | "gRPC Python tutorial protocol buffers" |
| GraphQL protocol | Single endpoint, queries, mutations, subscriptions, introspection | "GraphQL Python testing tutorial" |

**Exercise 4.3 — [GAP]:** (a) Use `mitmproxy` to intercept HTTPS traffic from a Python `requests` call. Capture the request/response, modify a header in-flight, and observe the change. (b) Use `openssl s_client` to inspect the certificate chain of `google.com`. Identify the CA, expiry date, and supported TLS versions. (c) Write a WebSocket test client that connects to `wss://echo.websocket.org`, sends 10 messages, and verifies each echo.

### 4.4 `requests` Library — Advanced [DEEPEN]

| Micro-Topic | What to Know | Search Term |
|-------------|-------------|-------------|
| Session objects | `requests.Session()`, persistent cookies, connection pooling, default headers | "Python requests Session advanced" |
| Retry with `urllib3` | `HTTPAdapter` + `Retry(total=3, backoff_factor=0.5, status_forcelist=[500, 502, 503])` | "Python requests retry adapter urllib3" |
| Timeouts | `timeout=(connect_timeout, read_timeout)`, why no timeout = hanging tests | "Python requests timeout connect read" |
| Streaming responses | `stream=True`, `iter_content()`, large file downloads without memory explosion | "Python requests streaming response" |
| Multipart uploads | `files` parameter, `Content-Type: multipart/form-data` | "Python requests multipart file upload" |
| Custom authentication | `requests.auth.AuthBase` subclass for custom auth flows | "Python requests custom AuthBase" |
| Event hooks | `response` hooks for logging, metrics collection on every request | "Python requests event hooks response" |
| Certificate handling | Custom CA bundles, client certificates, `verify`, `cert` parameters | "Python requests client certificate" |

### 4.5 API Client Architecture [DEEPEN]

| Micro-Topic | What to Know | Search Term |
|-------------|-------------|-------------|
| Base client class | Abstract base with `get()`, `post()`, `put()`, `patch()`, `delete()`, shared config | "Python API client base class design" |
| Response wrapping | Converting raw `Response` to typed objects (Pydantic models) | "Python API client response parsing Pydantic" |
| Error handling in clients | Translating HTTP errors to domain exceptions | "Python API client error handling pattern" |
| Request/response logging | Structured logging with `correlation_id`, method, URL, status, duration | "Python API client request logging" |
| Rate limiting | Client-side rate limiting with token bucket or leaky bucket | "Python rate limiting token bucket" |
| Pagination handling | Auto-paginating generators for list endpoints | "Python API client pagination generator" |

**Exercise 4.5 — [GAP]:** Build a complete API client framework: (a) `BaseClient(ABC)` with shared session, retry adapter, timeouts, logging, (b) `JSONPlaceholderClient(BaseClient)` targeting `jsonplaceholder.typicode.com`, (c) Auto-pagination: `client.list_posts()` returns a generator that fetches all pages, (d) All responses parsed into Pydantic models, (e) All errors mapped to custom exception hierarchy, (f) Structured logging: every request logs `{method, url, status, duration_ms, correlation_id}`.

---

## Tier 5: UI Automation Architecture

> **Goal:** Move beyond "can automate a login" to "can architect a UI test framework."

### 5.1 DOM & CSS Selector Engineering [GAP]

| Micro-Topic | What to Know | Search Term |
|-------------|-------------|-------------|
| CSS selectors — full spec | Type, class, ID, attribute (`[data-testid="x"]`), pseudo-classes (`:nth-child`, `:first-of-type`, `:not()`) | "CSS selectors complete reference" |
| CSS combinators | Descendant (` `), child (`>`), adjacent sibling (`+`), general sibling (`~`) | "CSS sibling combinators explained" |
| CSS pseudo-elements | `::before`, `::after` — understanding computed styles in assertions | "CSS pseudo elements before after" |
| XPath axes | `parent::`, `ancestor::`, `following-sibling::`, `preceding::`, `descendant::` | "XPath axes complete tutorial" |
| XPath functions | `contains()`, `text()`, `starts-with()`, `normalize-space()`, `position()` | "XPath functions for testing" |
| Shadow DOM | Open vs closed, `shadowRoot`, piercing shadow DOM in Playwright | "Shadow DOM Playwright testing" |
| iframe handling | Frame switching, cross-origin iframes, nested iframes | "Playwright iframe handling" |
| Accessibility selectors | `role`, `getByRole()`, `getByLabel()`, `getByText()`, `getByTestId()` — ARIA-first strategy | "Playwright accessibility selectors getByRole" |

**Exercise 5.1 — [GAP]:** On a complex public site (e.g., `https://the-internet.herokuapp.com/`): (a) Write 5 CSS selectors using different combinators (descendant, child, sibling), (b) Write 5 XPath expressions using different axes, (c) Write 3 selectors targeting Shadow DOM elements, (d) Rewrite all selectors using Playwright's `getByRole`/`getByLabel` and explain why the accessibility approach is more stable.

### 5.2 Playwright — Framework Architecture [DEEPEN]

| Micro-Topic | What to Know | Search Term |
|-------------|-------------|-------------|
| Browser contexts | Isolation between tests, state persistence, multi-user scenarios | "Playwright browser context isolation" |
| Page Object Model — advanced | Base page class, component objects, page factory | "Playwright Page Object Model advanced" |
| Network interception | `page.route()`, mocking API responses, blocking resources | "Playwright network interception route" |
| API testing via Playwright | `request` context for API calls within UI tests — hybrid testing | "Playwright API testing request context" |
| Trace viewer | Recording, viewing, attaching to CI artifacts | "Playwright trace viewer CI tutorial" |
| Visual regression | Screenshot comparison, threshold tuning, baseline management | "Playwright visual regression testing" |
| Auto-waiting internals | Actionability checks, how Playwright waits for elements | "Playwright auto-waiting actionability" |
| Parallel execution | `pytest-playwright` with `pytest-xdist`, browser instance management | "Playwright parallel execution pytest" |
| Custom fixtures | Browser fixture overrides, context fixture customization, storage state | "Playwright pytest custom fixtures" |
| Mobile emulation | Device descriptors, viewport, touch events | "Playwright mobile emulation testing" |

**Exercise 5.2 — [GAP]:** Build a Playwright framework for `https://demo.playwright.dev/todomvc/`: (a) Page Objects with `BasePage`, `TodoPage`, `TodoItem` component object, (b) Fixtures: `authenticated_page` (uses `storageState`), `api_context` for API setup, (c) Network interception: mock the API to return predefined todos, verify UI renders them, (d) Visual regression: screenshot comparison for the todo list in empty/populated/completed states, (e) Run in parallel with 4 workers, verify no flakiness.

---

## Tier 6: Test Architecture & Design Patterns

> **Goal:** Think in systems, not scripts. Design frameworks that other engineers want to use.

### 6.1 Test Strategy as Engineering [GAP]

| Micro-Topic | What to Know | Search Term |
|-------------|-------------|-------------|
| Test Pyramid | Unit → Integration → E2E ratios, cost/speed/confidence trade-offs | "Test pyramid strategy design" |
| Test diamond/trophy | When the pyramid doesn't apply (microservices, API-first products) | "Testing trophy Kent C Dodds" |
| Hermetic testing | Tests that don't depend on external state — full isolation | "Hermetic testing pattern" |
| Test coupling analysis | Identifying tests that fail together due to shared state — detecting hidden coupling | "Test coupling shared state analysis" |
| Flaky test engineering | Root causes (time, network, state, ordering), detection, quarantine, healing | "Flaky test root cause analysis" |
| Test environment abstraction | One test runs against local/staging/production by swapping config, not code | "Test environment abstraction layer pattern" |

### 6.2 Service Virtualization [GAP]

| Micro-Topic | What to Know | Search Term |
|-------------|-------------|-------------|
| WireMock | Stub HTTP services, record/playback, request matching, stateful mocking | "WireMock Python testing tutorial" |
| Testcontainers | Spin up real dependencies (Postgres, Redis, Kafka) in Docker for tests | "Testcontainers Python usage" |
| `responses` library | Mocking `requests` calls in Python unit tests | "Python responses library mock requests" |
| `respx` library | Mocking `httpx` calls for async tests | "Python respx mock httpx" |
| Contract-first mocking | Generate mocks from OpenAPI specs | "Generate mock server from OpenAPI spec" |

### 6.3 Contract Testing [DEEPEN]

| Micro-Topic | What to Know | Search Term |
|-------------|-------------|-------------|
| Consumer-driven contracts (Pact) | Consumer writes contract, provider verifies it | "Pact consumer driven contract testing Python" |
| Provider verification | Running provider tests against consumer contracts | "Pact provider verification Python" |
| Pact Broker | Sharing contracts between teams, versioning, can-i-deploy | "Pact Broker can-i-deploy workflow" |
| Schema validation (JSON Schema) | Validating API responses against a schema at test time | "JSON Schema validation Python jsonschema" |
| OpenAPI contract testing | Validating responses against OpenAPI spec definitions | "OpenAPI response validation testing" |

**Exercise 6.3 — [GAP]:** Implement a consumer-driven contract test: (a) Consumer: write a Pact test for "get user by ID" — specifying expected request and response shape, (b) Provider: verify the contract against a real (or mocked) API, (c) Add the contract to a Pact Broker (use the free PactFlow starter). (d) Separately, write a JSON Schema for the user response and validate it in your API tests using `jsonschema` library.

### 6.4 Performance Testing [DEEPEN]

| Micro-Topic | What to Know | Search Term |
|-------------|-------------|-------------|
| Load testing concepts | Throughput, latency (p50, p95, p99), saturation, error rate | "Load testing metrics p95 p99 explained" |
| k6 scripting | Virtual users, scenarios, thresholds, checks, custom metrics | "k6 load testing tutorial Python" |
| Locust (Python) | Python-based load testing, distributed execution | "Locust Python load testing tutorial" |
| Stress testing | Finding breaking points, gradual ramp-up patterns | "Stress testing vs load testing" |
| Soak testing | Long-duration tests for memory leaks, connection pool exhaustion | "Soak testing strategy" |
| Performance baselines | Establishing baselines, detecting regressions in CI | "Performance testing baseline CI regression" |

**Exercise 6.4 — [DEEPEN]:** Write a Locust test for a public API: (a) Define 3 user behaviors with different weights (browse: 70%, create: 20%, delete: 10%), (b) Ramp from 10 to 200 users over 5 minutes, (c) Set pass/fail thresholds: p95 < 500ms, error rate < 1%, (d) Generate a report and identify the saturation point.

### 6.5 Security Testing Fundamentals [DEEPEN]

| Micro-Topic | What to Know | Search Term |
|-------------|-------------|-------------|
| OWASP API Security Top 10 | Broken object-level auth, broken authentication, excessive data exposure, etc. | "OWASP API Security Top 10 2023" |
| BOLA testing | Accessing resources belonging to other users via ID manipulation | "Broken Object Level Authorization testing" |
| Injection testing | SQL injection, NoSQL injection, command injection in API parameters | "API injection testing examples" |
| Authentication bypass | Missing auth checks, JWT manipulation, token reuse | "Authentication bypass testing API" |
| Rate limiting verification | Verifying rate limits are enforced and return proper 429 responses | "API rate limiting testing" |
| IDOR testing | Insecure Direct Object Reference — horizontal privilege escalation | "IDOR testing methodology" |
| Header security | `X-Frame-Options`, `Strict-Transport-Security`, `Content-Security-Policy`, `X-Content-Type-Options` | "Security headers testing checklist" |

**Exercise 6.5 — [DEEPEN]:** Against a deliberately vulnerable API (use OWASP Juice Shop or DVGA): (a) Test for BOLA by manipulating resource IDs, (b) Test for SQL injection in a search parameter, (c) Verify rate limiting by sending 1000 requests in 10 seconds, (d) Check all security headers on the response. Document each finding with: vulnerability, risk level, reproduction steps, and recommended fix.

---

## Tier 7: Data Engineering for Test

> **Goal:** Master the data layer — generation, validation, storage, lifecycle.

### 7.1 SQL — Beyond Basics [DEEPEN]

| Micro-Topic | What to Know | Search Term |
|-------------|-------------|-------------|
| Joins deep | INNER, LEFT, RIGHT, FULL OUTER, CROSS, self-join — all with multi-table scenarios | "SQL joins comprehensive tutorial" |
| Window functions | `ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`, `LAG()`, `LEAD()`, `NTILE()`, `PARTITION BY` | "SQL window functions tutorial examples" |
| CTEs (Common Table Expressions) | `WITH` clauses for readability, recursive CTEs for hierarchical data | "SQL CTE recursive common table expression" |
| Subqueries | Correlated vs non-correlated, `EXISTS`, `IN` vs `JOIN` performance | "SQL subquery correlated vs non-correlated" |
| Transaction isolation levels | READ COMMITTED, REPEATABLE READ, SERIALIZABLE — dirty reads, phantom reads | "SQL transaction isolation levels explained" |
| Index fundamentals | B-tree, hash, composite indexes, `EXPLAIN ANALYZE` | "SQL indexes EXPLAIN ANALYZE tutorial" |
| Database seeding | Inserting test data, maintaining referential integrity, bulk inserts | "Database seeding test data strategy" |
| Database cleanup strategies | Truncate, transaction rollback, Docker reset, schema isolation | "Test database cleanup strategy" |

**Exercise 7.1 — [DEEPEN]:** Against a PostgreSQL database (use Docker): (a) Write a query using window functions to rank users by login count within each organization, (b) Write a recursive CTE to traverse a group membership hierarchy (groups containing groups), (c) Write a test data seeder that creates 100 users across 10 orgs with proper FK relationships, (d) Write a cleanup function using `TRUNCATE ... CASCADE`, (e) Use `EXPLAIN ANALYZE` to compare a subquery vs JOIN approach for the same result.

### 7.2 Test Data Generation [GAP]

| Micro-Topic | What to Know | Search Term |
|-------------|-------------|-------------|
| Faker library | Providers, locales, seeded generation for reproducibility | "Python Faker library advanced usage" |
| Factory Boy | Model factories with sequences, `SubFactory`, `LazyAttribute`, `Trait` | "Factory Boy Python tutorial" |
| Pairwise/combinatorial generation | `allpairspy` for reducing test matrix while maintaining coverage | "Pairwise testing Python allpairspy" |
| Boundary value generation | Systematic generation of edge cases (empty, null, max length, special chars, unicode) | "Boundary value analysis test data generation" |
| Test data lifecycle | Create → use → validate → cleanup — managing across test session | "Test data lifecycle management" |
| Data masking | Using production-like data without PII exposure | "Test data masking anonymization" |

**Exercise 7.2 — [GAP]:** Build a test data framework: (a) `UserFactory` using Factory Boy with `SubFactory` for organization, (b) `@lazy_attribute` that generates email from first/last name, (c) `Trait` for "admin_user" that sets role and permissions, (d) Seeded generation: `UserFactory.create_batch(50, seed=42)` produces identical users every run, (e) Pairwise generation: use `allpairspy` to generate minimal test combinations for `[3 roles] × [4 states] × [2 MFA settings] × [3 OS types]`.

### 7.3 JSON Schema Validation [GAP]

| Micro-Topic | What to Know | Search Term |
|-------------|-------------|-------------|
| JSON Schema specification | `type`, `properties`, `required`, `additionalProperties`, `$ref` | "JSON Schema specification tutorial" |
| `jsonschema` library | Validating Python dicts against schemas, custom validators | "Python jsonschema validation tutorial" |
| Schema generation from models | Pydantic `model_json_schema()`, auto-generating from API responses | "Generate JSON Schema from Pydantic" |
| Schema evolution | Adding fields (backward compatible), removing fields (breaking), versioning | "JSON Schema evolution versioning" |
| OpenAPI schema extraction | Extracting response schemas from OpenAPI specs for validation | "OpenAPI response schema validation" |

---

## Tier 8: Containerization & Orchestration Engineering

> **Goal:** Not just "use Docker" but understand it well enough to debug containerized test environments.

### 8.1 Docker — Engineering Depth [DEEPEN]

| Micro-Topic | What to Know | Search Term |
|-------------|-------------|-------------|
| Image layering | Union filesystem, layer caching, cache busting, `--no-cache` | "Docker image layers caching explained" |
| Multi-stage builds | Builder stage, production stage, `--target`, reducing image size | "Docker multi-stage build tutorial" |
| Build arguments and env vars | `ARG` vs `ENV`, build-time vs runtime, secrets in builds (BuildKit) | "Docker ARG vs ENV build secrets" |
| Networking | Bridge, host, overlay, custom networks, DNS resolution between containers | "Docker networking bridge custom DNS" |
| Volumes and bind mounts | Named volumes, bind mounts, tmpfs, volume drivers | "Docker volumes vs bind mounts" |
| Health checks | `HEALTHCHECK` instruction, health-check based orchestration | "Docker HEALTHCHECK instruction" |
| Debugging containers | `docker exec`, `docker logs`, `docker inspect`, `docker stats` | "Docker container debugging tutorial" |
| Image optimization | `.dockerignore`, minimal base images (alpine, distroless, slim), removing unnecessary layers | "Docker image optimization best practices" |
| Docker Compose advanced | `depends_on` with health checks, profiles, extending services, environment files | "Docker Compose advanced depends_on health" |
| BuildKit features | Secrets, SSH forwarding, cache mounts, parallel stage execution | "Docker BuildKit features tutorial" |

**Exercise 8.1 — [DEEPEN]:** Build a test environment in Docker: (a) `docker-compose.yml` with 3 services: test-runner (your framework), postgres (test database), wiremock (mock API), (b) Test-runner waits for both dependencies (health checks), (c) Multi-stage Dockerfile: build stage installs everything, final stage is slim, (d) Benchmark: compare build time with and without layer caching, compare image size with and without multi-stage.

### 8.2 Kubernetes for SDET [DEEPEN]

| Micro-Topic | What to Know | Search Term |
|-------------|-------------|-------------|
| Pod anatomy | Containers, init containers, sidecar pattern, resource requests/limits | "Kubernetes Pod anatomy init container" |
| Deployments and ReplicaSets | Rolling updates, rollback, scaling, update strategy | "Kubernetes Deployment rolling update" |
| Services | ClusterIP, NodePort, LoadBalancer, headless — when each is used | "Kubernetes Service types explained" |
| ConfigMaps and Secrets | Mounting as env vars or files, secret encryption at rest | "Kubernetes ConfigMap Secret tutorial" |
| Jobs and CronJobs | One-off tasks, scheduled tasks — perfect for test execution | "Kubernetes Job CronJob tutorial" |
| `kubectl` advanced | `kubectl run --rm -it`, `kubectl port-forward`, `kubectl cp`, `kubectl top` | "kubectl advanced commands tutorial" |
| Helm chart authoring | `values.yaml`, templates, `_helpers.tpl`, hooks, chart dependencies | "Helm chart authoring tutorial" |
| Debugging K8s | `kubectl describe`, events, `kubectl logs --previous`, ephemeral containers | "Kubernetes debugging pods tutorial" |
| Namespaces and RBAC | Namespace isolation, `Role`, `RoleBinding`, `ServiceAccount` | "Kubernetes namespace RBAC tutorial" |

**Exercise 8.2 — [DEEPEN]:** Deploy your test framework on Kubernetes: (a) Write a `Job` manifest that runs your pytest suite, (b) Use `ConfigMap` for test configuration (environment, tags to run), (c) Use `Secret` for API keys, (d) Write a `CronJob` that runs smoke tests every 6 hours, (e) Port-forward to view the Allure report from inside the cluster.

---

## Tier 9: CI/CD Pipeline Engineering

> **Goal:** Design pipelines, not just use them.

### 9.1 GitHub Actions — Engineering Level [DEEPEN]

| Micro-Topic | What to Know | Search Term |
|-------------|-------------|-------------|
| Workflow triggers | `push`, `pull_request`, `schedule`, `workflow_dispatch`, `workflow_call`, `repository_dispatch` | "GitHub Actions workflow triggers" |
| Reusable workflows | `workflow_call` for DRY pipelines, input/output definitions | "GitHub Actions reusable workflows" |
| Composite actions | Encapsulating steps into a reusable action | "GitHub Actions composite action tutorial" |
| Matrix strategies | Multi-dimensional matrices, `include`, `exclude`, `fail-fast` | "GitHub Actions matrix strategy include exclude" |
| Concurrency control | `concurrency` groups, cancel in-progress, queue behavior | "GitHub Actions concurrency control" |
| Artifact management | Upload/download artifacts, retention policies, cross-job sharing | "GitHub Actions artifacts cross-job" |
| Environment protection | Deployment environments, approval gates, environment secrets | "GitHub Actions environments protection rules" |
| Self-hosted runners | When/why, Docker-based runners, security considerations | "GitHub Actions self-hosted runners setup" |
| Caching strategies | `actions/cache`, dependency caching, Docker layer caching, cache keys | "GitHub Actions caching strategy" |
| Secret management | Organization secrets, environment secrets, `GITHUB_TOKEN` permissions | "GitHub Actions secrets management" |
| Status checks and branch protection | Required checks, auto-merge rules, CODEOWNERS | "GitHub branch protection required checks" |

**Exercise 9.1 — [DEEPEN]:** Build a production-grade CI pipeline: (a) Reusable workflow for "lint and test" callable from multiple repos, (b) Matrix build across Python 3.10/3.11/3.12 and OS ubuntu/macos, (c) Smart test selection: only run API tests if `tests/api/` changed, only run UI tests if `tests/ui/` changed (use `dorny/paths-filter`), (d) Concurrency: cancel stale runs on the same branch, (e) On merge to main: build Docker image, push to registry, deploy to staging.

### 9.2 Pipeline Design Patterns [GAP]

| Micro-Topic | What to Know | Search Term |
|-------------|-------------|-------------|
| Shift-left testing | Running tests as early as possible in the pipeline | "Shift left testing CI/CD" |
| Test stage ordering | Lint → Unit → Integration → Contract → E2E → Performance | "CI/CD test stage ordering strategy" |
| Flaky test quarantine | Auto-detecting and isolating flaky tests from the main pipeline | "Flaky test quarantine CI automation" |
| Feature flag testing | Testing with feature flags on/off, matrix of flag combinations | "Feature flag testing strategy CI" |
| Canary testing | Running a subset of tests against canary deployments | "Canary deployment testing strategy" |
| Pipeline as code | Treating CI config as first-class code — versioned, reviewed, tested | "Pipeline as code best practices" |
| Build artifact management | Versioning, retention, promotion (dev → staging → prod) | "Build artifact management strategy" |

---

## Tier 10: Observability & Monitoring Engineering

> **Goal:** Instrument your tests and infrastructure for complete visibility.

### 10.1 Structured Logging [GAP]

| Micro-Topic | What to Know | Search Term |
|-------------|-------------|-------------|
| Python `logging` module | Loggers, handlers, formatters, levels, propagation | "Python logging module complete tutorial" |
| Structured logging (JSON) | `python-json-logger`, consistent fields (`timestamp`, `level`, `message`, `correlation_id`) | "Python structured logging JSON tutorial" |
| Correlation IDs | Tracing a single request across logs — `X-Request-ID` propagation | "Correlation ID logging distributed systems" |
| Log levels discipline | DEBUG vs INFO vs WARNING vs ERROR vs CRITICAL — when to use each | "Logging levels best practices" |
| Log aggregation | Sending logs to ELK/Datadog/CloudWatch, structured vs unstructured | "Log aggregation ELK Datadog comparison" |

### 10.2 Datadog — Deep Integration [DEEPEN]

| Micro-Topic | What to Know | Search Term |
|-------------|-------------|-------------|
| APM concepts | Traces, spans, services, resources, latency distribution | "Datadog APM concepts traces spans" |
| `ddtrace` Python | `patch_all()`, manual spans, custom tags, trace context propagation | "ddtrace Python instrumentation tutorial" |
| Custom metrics | `DogStatsD`, counters, gauges, histograms, distributions | "Datadog custom metrics DogStatsD Python" |
| Dashboard design | Widgets, template variables, time series, heat maps, top lists | "Datadog dashboard design best practices" |
| Monitors and alerts | Metric monitors, log monitors, composite monitors, alert routing | "Datadog monitors alerts tutorial" |
| Log query syntax | Facets, filters, patterns, live tail, saved views | "Datadog log query syntax tutorial" |
| SLIs/SLOs | Service Level Indicators/Objectives, error budgets | "Datadog SLO SLI error budget" |

### 10.3 OpenTelemetry Awareness [GAP]

| Micro-Topic | What to Know | Search Term |
|-------------|-------------|-------------|
| OTEL concepts | Traces, metrics, logs — vendor-neutral standard | "OpenTelemetry concepts overview" |
| OTEL Python SDK | Auto-instrumentation, manual spans, exporters | "OpenTelemetry Python SDK tutorial" |
| OTEL Collector | Receiving, processing, exporting telemetry data | "OpenTelemetry Collector setup" |
| Vendor comparison | OTEL → Datadog, OTEL → Jaeger, OTEL → Grafana — the portability advantage | "OpenTelemetry vendor exporters comparison" |

---

## Tier 11: Cloud Infrastructure for SDET

> **Goal:** Provision and manage the infrastructure your tests run on.

### 11.1 AWS Core Services [DEEPEN]

| Micro-Topic | What to Know | Search Term |
|-------------|-------------|-------------|
| IAM deep | Policies, roles, trust relationships, OIDC federation, least privilege | "AWS IAM policies roles tutorial" |
| S3 for test artifacts | Bucket creation, lifecycle policies, presigned URLs, cross-account access | "AWS S3 test artifacts storage" |
| EC2 for test runners | Instance types, AMIs, user data scripts, spot instances for cost savings | "AWS EC2 spot instances CI runners" |
| Lambda for test triggers | Event-driven test execution (S3 upload triggers test, schedule triggers regression) | "AWS Lambda test automation trigger" |
| CloudWatch | Log groups, metrics, alarms, dashboards — for test infrastructure monitoring | "AWS CloudWatch monitoring tutorial" |
| ECS/ECR | Running test containers in ECS, storing images in ECR | "AWS ECS ECR container tutorial" |
| Secrets Manager | Storing and rotating test credentials | "AWS Secrets Manager tutorial" |

### 11.2 Terraform for SDET [DEEPEN]

| Micro-Topic | What to Know | Search Term |
|-------------|-------------|-------------|
| HCL basics | Resources, variables, outputs, data sources | "Terraform HCL basics tutorial" |
| State management | Remote state, state locking, `terraform import` | "Terraform state management remote" |
| Modules | Reusable infrastructure components | "Terraform modules tutorial" |
| Workspaces | Separate environments (dev/staging/prod) from same code | "Terraform workspaces environments" |
| `terraform plan` / `apply` | Understanding the plan, targeted apply, destroy | "Terraform plan apply workflow" |

**Exercise 11.2 — [DEEPEN]:** Write Terraform to provision a minimal test infrastructure: (a) S3 bucket for test reports (with lifecycle policy to auto-delete after 30 days), (b) IAM role for CI (with OIDC trust policy for GitHub Actions), (c) ECR repository for your test Docker image. All using modules for reusability.

---

## Tier 12: Architectural Framework Design

> **Goal:** The capstone. Design a complete test automation framework from scratch.

### 12.1 Framework Architecture Document

Before writing code, produce a Technical Design Document covering:

| Section | Content |
|---------|---------|
| Problem Statement | What does this framework solve? Who are the users? |
| Architecture Diagram | Layers: Configuration → Client → Model → Helper → Step → Feature |
| Technology Choices | With justification for each (why pytest-bdd over Behave, why Pydantic over dataclasses) |
| Test Data Strategy | Factories, cleanup, isolation, environment parity |
| CI Integration | Pipeline stages, parallelism, reporting, failure alerting |
| Extensibility | How new API domains are added, how new environments are onboarded |
| Observability | Logging, tracing, metrics, dashboards |
| Maintenance Plan | Dependency updates, flaky test management, documentation |

### 12.2 Capstone Project

Build a complete, production-grade API + UI test automation framework from scratch:

**Requirements:**

1. **Configuration Layer:** Pydantic `BaseSettings` for environment management. Support local/staging/production via env vars.
2. **API Client Layer:** Abstract `BaseClient` → concrete `ServiceClient`. Retry adapter, timeouts, structured logging, Pydantic response models.
3. **Authentication Layer:** Pluggable auth providers (API key, OAuth2, JWT). Strategy pattern.
4. **Test Data Layer:** Factory Boy factories with Faker. Seeded generation. Auto-cleanup via context managers.
5. **BDD Layer:** Feature files with proper tag taxonomy. Step definitions using parsers. Shared steps via conftest.
6. **UI Layer:** Playwright Page Objects. Visual regression. Network interception for hybrid tests.
7. **Reporting Layer:** Allure reporting with custom steps, attachments, environment info.
8. **Observability Layer:** `ddtrace` integration, custom spans, Datadog dashboard.
9. **CI Layer:** GitHub Actions with matrix build, smart test selection, parallel execution, artifact upload.
10. **Docker Layer:** Multi-stage Dockerfile, Docker Compose for local environment, `.dockerignore`.
11. **Documentation:** README with setup, architecture, contribution guide.

**Validation Criteria:**
- 50+ automated tests (mix of API, UI, BDD, parametrized)
- CI pipeline passes on every push
- Docker build completes in under 3 minutes
- Parallel execution with `pytest-xdist` (4 workers) shows >2x speedup
- Zero flaky tests across 5 consecutive runs
- Another engineer can set up and run the framework within 15 minutes by following the README

---

## Appendix A: Mastery Validation Exercises (Cross-Tier)

These exercises span multiple tiers and simulate real-world SDET challenges.

### A.1 The "Production Incident" Simulation

**Scenario:** Tests that passed yesterday are now failing with `500 Internal Server Error` on 30% of runs.

**Tasks:**
1. Add retry logic with exponential backoff to your API client (Tier 2, 4)
2. Add structured logging to capture request/response for failed calls (Tier 10)
3. Write a `pytest_runtest_makereport` hook that categorizes failures: infrastructure vs test defect vs product bug (Tier 3)
4. Build a Datadog dashboard showing failure rate over time, grouped by category (Tier 10)
5. Write a flaky test detection script that runs the suite 5 times and identifies tests with inconsistent results (Tier 2, 9)

### A.2 The "New Service Onboarding" Challenge

**Scenario:** A new microservice is deployed. You need to add acceptance tests.

**Tasks:**
1. Read the OpenAPI spec, generate Pydantic models (Tier 2, 7)
2. Build a client class for the service extending your `BaseClient` (Tier 4)
3. Write BDD features covering CRUD + edge cases (Tier 3)
4. Add factory for the new entity type (Tier 7)
5. Add CI pipeline stage for the new service (Tier 9)
6. Add Datadog tracing for the new service's API calls (Tier 10)

### A.3 The "Framework Migration" Exercise

**Scenario:** Migrate 20 tests from raw `requests` + `unittest` to your pytest-bdd framework.

**Tasks:**
1. Map each test to a Gherkin scenario (Tier 3)
2. Extract reusable step definitions (Tier 3)
3. Replace raw dicts with Pydantic models (Tier 2)
4. Add fixtures for setup/teardown (Tier 3)
5. Verify identical coverage with `pytest --co` comparison (Tier 3)
6. Run both suites in CI during transition period (Tier 9)

---

## Appendix B: Interview Simulation Bank

### B.1 System Design Questions

1. "Design a test automation framework for a microservices platform with 50 services, 3 environments, and 2000 test cases. How do you handle test data, parallelism, and reporting?"
2. "You're given 500 Selenium tests that take 8 hours to run. How do you reduce this to 30 minutes?"
3. "Design a CI pipeline that supports feature flags. Tests must verify behavior with each flag on and off."

### B.2 Coding Questions

1. Write a retry decorator with exponential backoff and jitter.
2. Write a parametrized fixture factory that creates users with varying roles and permissions.
3. Write a `pytest_runtest_makereport` hook that captures screenshots on UI test failure.
4. Write an API client that auto-paginates and returns a generator.
5. Write a context manager that creates and cleans up test data.

### B.3 Behavioral/Process Questions

1. "A developer says they don't need tests for their feature because they tested it manually. How do you respond?"
2. "Your test suite is 40% flaky. What's your 30-day plan to fix this?"
3. "How do you decide what to automate and what to keep manual?"
4. "A critical bug was missed by automation. How do you prevent this in the future?"

---

## Progress Tracking

| Tier | Status | Started | Completed | Notes |
|------|--------|---------|-----------|-------|
| 1: Foundational Software Engineering | Not Started | | | |
| 2: Python Engineering | Not Started | | | |
| 3: Testing Frameworks | Not Started | | | |
| 4: API & Protocol Engineering | Not Started | | | |
| 5: UI Automation Architecture | Not Started | | | |
| 6: Test Architecture & Design Patterns | Not Started | | | |
| 7: Data Engineering for Test | Not Started | | | |
| 8: Containerization & Orchestration | Not Started | | | |
| 9: CI/CD Pipeline Engineering | Not Started | | | |
| 10: Observability & Monitoring | Not Started | | | |
| 11: Cloud Infrastructure | Not Started | | | |
| 12: Architectural Framework Design | Not Started | | | |
| Appendix A: Cross-Tier Exercises | Not Started | | | |
| Appendix B: Interview Prep | Not Started | | | |

---

*This document is a living blueprint. Update the progress table weekly. Every completed exercise should result in committed code in your `qa-learning-journey` repository.*
