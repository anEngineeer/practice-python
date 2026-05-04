# QA to Python Developer — Complete Transition Strategy

**Who this is for:** Prateek Mishra — Civil Engineering B.Tech, 4+ years in QA (manual QA → automation at JumpCloud using pytest/BDD), now learning both Python Development and SDET skills simultaneously.  
**Your actual starting point (be honest with yourself):**
- You can write simple Python scripts, call APIs with `requests`, use basic `pytest`
- You do NOT deeply understand OOP, decorators, generators, design patterns, or how to architect code
- You have never built an application from scratch — only test code
- You work in a codebase (jumpcloud-acceptance) that uses advanced patterns, but reading code ≠ writing code
- Your coding foundation is beginner-level because your degree is Civil Engineering and your career started in manual QA

**What this document does:** Teaches you to code like a developer from your actual starting point — not the idealized "I already know Python basics" starting point. Every topic, every exercise, every resource is here. You don't need another document for the developer path.  
**Time commitment:** 8 hours/week total — split 70% Developer (5.5 hrs) + 30% SDET (2.5 hrs)  
**Timeline:** 12 months to be interview-ready. First 4 months build shared foundations that serve BOTH paths.  
**Companion docs:** `Master_SDET_Implementation_Plan.md` (SDET-specific depth, 30% of your time), all other Prep docs (reference only)

---

## Table of Contents

- [Your Real Situation — No Sugarcoating](#your-real-situation--no-sugarcoating)
- [The Dual-Track Strategy](#the-dual-track-strategy)
- [Phase 1: Python Foundations — Think Like a Programmer (Weeks 1–8)](#phase-1-python-foundations--think-like-a-programmer-weeks-18)
- [Phase 2: Intermediate Python — Write Real Code (Weeks 9–16)](#phase-2-intermediate-python--write-real-code-weeks-916)
- [Phase 3: Web Development with FastAPI (Weeks 17–24)](#phase-3-web-development-with-fastapi-weeks-1724)
- [Phase 4: Databases — SQL and ORM (Weeks 25–32)](#phase-4-databases--sql-and-orm-weeks-2532)
- [Phase 5: Build a Full Application (Weeks 33–40)](#phase-5-build-a-full-application-weeks-3340)
- [Phase 6: Deployment, System Design, and Polish (Weeks 41–48)](#phase-6-deployment-system-design-and-polish-weeks-4148)
- [What to Build — Project Roadmap](#what-to-build--project-roadmap)
- [The Dual-Track Weekly Schedule](#the-dual-track-weekly-schedule)
- [Resources — Complete Reference](#resources--complete-reference)
- [What NOT to Waste Time On](#what-not-to-waste-time-on)
- [Interview Preparation](#interview-preparation)
- [Progress Tracker](#progress-tracker)

---

## Your Real Situation — No Sugarcoating

Read this section honestly. It calibrates everything that follows.

### Where You Actually Are

```
Civil Engineering degree (no CS background)
        ↓
Manual QA (2+ years: Postman, test cases, defect lifecycle)
        ↓
Automation QA at JumpCloud (1.5+ years: pytest, BDD, requests library)
        ↓
NOW: Learning to code properly for BOTH Developer and SDET careers
```

### What "Beginner Python" Actually Means for You

You can do these things:
- Write a pytest test that calls an API and asserts the response
- Use `requests.get()`, `requests.post()` with headers and JSON bodies
- Write step definitions for BDD scenarios
- Use `os.environ.get()` for config values
- Write basic `if/else`, `for` loops, work with lists and dicts

You CANNOT yet do these things (and that's okay — this plan teaches all of them):
- Design a class hierarchy from scratch and explain why you structured it that way
- Write a decorator and explain how it works internally
- Use generators, context managers, or `itertools` confidently
- Build anything beyond test scripts — no CLI tools, no web apps, no data pipelines
- Explain Big-O complexity, recursion, or common data structures
- Design a database schema or write SQL beyond basic SELECT/INSERT

### Why This Matters

The SDET plan (`Master_SDET_Implementation_Plan.md`) assumes you can write Python at an engineering level. You can't yet. Many of its exercises will be frustrating if you jump straight to Tier 2 (decorators, generators, metaclasses) without first building a solid coding foundation.

**This document fixes that.** It builds your coding foundation from where you actually are. The first 4 months (Phases 1–2) benefit BOTH your developer AND SDET goals. After that, the paths diverge: this document goes toward application building, while the Master Plan goes toward test framework engineering.

### The Mindset Shift You Need

| Your Current Thinking | The Thinking You Need |
|----------------------|----------------------|
| "I use Python to automate tests" | "I use Python to build things — applications, tools, systems" |
| "I call APIs" | "I build APIs" |
| "I read other people's code" | "I write code others will read" |
| "I copy patterns from the codebase" | "I design patterns for new problems" |
| "I know enough Python for my job" | "I want to master Python as my craft" |

---

## The Dual-Track Strategy

You are learning two things at once. This section explains how they fit together without overwhelming you.

### The Two Tracks

```
TRACK A: Python Developer (THIS DOCUMENT — 70% of time, 5.5 hrs/week)
  Goal: Build applications. Get hired as a Python developer.
  Path: Python foundations → Web APIs → Databases → Full app → Deploy

TRACK B: SDET (Master_SDET_Implementation_Plan.md — 30% of time, 2.5 hrs/week)
  Goal: Deepen test engineering. Get hired as a senior SDET.
  Path: Master Plan Tiers 1–4 → Portfolio → Innovation tools
```

### Why 70/30 and Not 50/50

Developer skills are harder to learn from your starting point. SDET skills build on what you already do daily at work. You get SDET practice 40 hours/week at JumpCloud. You get developer practice 0 hours/week unless you study. The 70/30 split compensates for this imbalance.

### How the Tracks Share Foundations (Months 1–4)

The first 16 weeks of this document (Phases 1–2) teach Python fundamentals that serve BOTH tracks. During these 16 weeks, you don't need the Master Plan at all — everything overlaps.

```
Months 1–4: SHARED FOUNDATION (this document only)
  Python OOP, functions, data structures, error handling, packaging
  ↓ serves both ↓

Month 5 onward: TRACKS DIVERGE
  ┌──────────────────────────────────┐  ┌──────────────────────────────────┐
  │ DEVELOPER (this doc, 70%)         │  │ SDET (Master Plan, 30%)           │
  │ FastAPI, databases, full app,     │  │ Tier 3: Pytest internals          │
  │ deployment, system design         │  │ Tier 4: API client architecture   │
  │                                    │  │ Tier 6: Test architecture         │
  │                                    │  │ Portfolio Blueprint projects      │
  └──────────────────────────────────┘  └──────────────────────────────────┘
```

### When to Start the Master Plan

- **Weeks 1–16:** Do NOT open the Master Plan. Focus 100% on Phases 1–2 here. They cover the same Python foundations but in a way that builds toward application development.
- **Week 17 onward:** Start the Master Plan at Tier 3 (Pytest Internals). Tiers 1–2 are already covered by Phases 1–2 of this document. Spend 2.5 hrs/week on the Master Plan alongside this document.

---

## Phase 1: Python Foundations — Think Like a Programmer (Weeks 1–8)

> **Goal:** Go from "I can write scripts that call APIs" to "I can design and build programs." This phase teaches you to think in code, not just use code.

### Week 1–2: Functions, Data Structures, and Control Flow (Properly)

You've used these before. Now understand them deeply enough to *design* with them, not just *use* them.

#### Functions — Beyond Calling Them

| Micro-Topic | What to Know | How Deep | Search Term |
|-------------|-------------|----------|-------------|
| Function as a building block | A function should do ONE thing. If you can't name it clearly, it does too much. | Refactor a 30-line function into 3 functions of 10 lines each | "Python functions clean code" |
| Parameters and arguments | Positional, keyword, default values, `*args`, `**kwargs` | Write a function that accepts flexible arguments | "Python *args **kwargs explained" |
| Return values | Always return something meaningful. `None` should be intentional, not accidental. | Return dicts, tuples, custom objects — not just `True/False` | "Python function return values" |
| Pure functions | Functions with no side effects — same input always gives same output | Write 5 pure functions (no global variables, no prints, no file writes) | "Python pure functions" |
| Scope and closures | `local` → `enclosing` → `global` → `built-in` (LEGB rule) | Understand why a variable inside a function isn't visible outside | "Python LEGB scope rule" |
| Lambda functions | Anonymous functions for `sorted(key=)`, `filter()`, `map()` | Use in sorting a list of dicts by a key | "Python lambda functions when to use" |
| Docstrings | Document every function you write | `"""One-line summary. Detailed description. Args. Returns."""` | "Python docstring conventions Google style" |

#### Data Structures — Think About When to Use What

| Micro-Topic | What to Know | When to Use It | Search Term |
|-------------|-------------|---------------|-------------|
| Lists | Ordered, mutable, allows duplicates | Collections where order matters (task list, log entries) | "Python list methods tutorial" |
| Tuples | Ordered, immutable | Fixed data (coordinates, RGB colors, function returning multiple values) | "Python tuples vs lists when to use" |
| Dictionaries | Key-value pairs, O(1) lookup | Mapping IDs to objects, configuration, counters | "Python dictionary advanced usage" |
| Sets | Unordered, unique elements, O(1) membership test | Deduplication, checking if item exists, set operations (intersection, union) | "Python sets practical examples" |
| List comprehensions | `[x for x in items if condition]` | Transforming/filtering lists in one line | "Python list comprehension tutorial" |
| Dict comprehensions | `{k: v for k, v in items}` | Building dicts from lists or transforming dicts | "Python dictionary comprehension" |
| Nested data structures | Lists of dicts, dicts of lists, dicts of dicts | Modeling API responses, configuration trees | "Python nested data structures" |
| `collections` module | `defaultdict`, `Counter`, `namedtuple`, `deque` | Counting, grouping, lightweight data objects, queues | "Python collections module practical" |

**Exercise 1 (Week 1):** Build a **Contact Book** CLI program in a single file:
- Store contacts as a list of dicts: `[{"name": "Prateek", "phone": "123", "email": "p@g.com", "group": "work"}]`
- Functions: `add_contact()`, `search_contacts(query)` (search by name or email), `delete_contact(name)`, `list_contacts(group=None)` (filter by group), `export_to_json(filepath)`, `import_from_json(filepath)`
- Use `input()` for a simple menu: 1. Add, 2. Search, 3. Delete, 4. List, 5. Export, 6. Import, 7. Quit
- Data validation: no duplicate emails, phone must be digits only, name must not be empty
- Save to JSON file on every change (persistence)

**Why this exercise:** It forces you to use functions, data structures, file I/O, validation, and user interaction — all in one small program. This is more than you've ever built from scratch.

**Exercise 2 (Week 2):** Build a **Log Analyzer** CLI:
- Read a log file (create a sample one with 100+ lines of mixed INFO, WARNING, ERROR entries with timestamps)
- Functions: `parse_log_line(line)` → returns a dict `{timestamp, level, message}`, `count_by_level(entries)` → `{"INFO": 45, "WARNING": 30, "ERROR": 25}`, `filter_by_level(entries, level)`, `filter_by_time_range(entries, start, end)`, `most_common_errors(entries, top_n=5)`
- Use `Counter` from `collections` for counting
- Use list comprehensions for filtering
- Print a formatted summary report

**Why this exercise:** Parsing, filtering, and aggregating data is what both developers and SDETs do daily. This builds the muscle.

### Week 3–4: Object-Oriented Programming (From Scratch)

This is where most self-taught developers struggle. You need to understand OOP deeply — not just "classes have methods."

#### Why OOP Matters for You

In your daily work, you read code like `Context()`, `SystemuserFactory(admin=admin)`, `BaseClient`. These are all OOP. Right now you use them. After this section, you can *design* them.

| Micro-Topic | What to Know | How Deep | Search Term |
|-------------|-------------|----------|-------------|
| Class and object | A class is a blueprint. An object is an instance of that blueprint. | Create 5 different classes with at least 3 attributes and 3 methods each | "Python class and object tutorial beginner" |
| `__init__` | The constructor. Runs when you create an object. Sets up initial state. | Every class must have a meaningful `__init__` | "Python __init__ method explained" |
| Instance vs class variables | Instance: unique to each object. Class: shared by all objects. | Know the difference and when to use each | "Python instance vs class variables" |
| Methods | Regular methods (`self`), `@classmethod` (`cls`), `@staticmethod` (no self/cls) | Write a `@classmethod` factory method: `User.from_dict(data)` | "Python classmethod staticmethod difference" |
| `__repr__` and `__str__` | `__repr__` for developers (debugging). `__str__` for users (display). | Every class you write must have `__repr__` at minimum | "Python __repr__ vs __str__" |
| Encapsulation | `_private` convention, `@property` for controlled access | Use `@property` to validate data on set (e.g., age can't be negative) | "Python property decorator encapsulation" |
| Inheritance | Child class inherits from parent. `super().__init__()` to call parent's init. | Build a 2-level hierarchy: `Vehicle` → `Car`, `Truck` | "Python inheritance super explained" |
| Composition | A class *has* another class as an attribute (not inherits from it) | `Library` has a list of `Book` objects. `Team` has a list of `Member` objects. | "Python composition vs inheritance" |
| `@dataclass` | Auto-generates `__init__`, `__repr__`, `__eq__` for data-holding classes | Use for any class that mainly holds data (models, configs, DTOs) | "Python dataclass tutorial" |
| `__eq__` and `__hash__` | Define when two objects are "equal". Needed for sets and dict keys. | Two books with the same ISBN are equal regardless of other fields | "Python __eq__ __hash__ explained" |

**Exercise 3 (Week 3):** Build an **Expense Tracker** using OOP:

Classes to build:
- `Expense` dataclass: `amount: float`, `category: str`, `description: str`, `date: datetime`
- `Category` (enum or class): FOOD, TRANSPORT, ENTERTAINMENT, UTILITIES, OTHER
- `ExpenseTracker`:
  - `add_expense(expense: Expense)` — adds an expense
  - `get_expenses(category=None, start_date=None, end_date=None)` — filtered list
  - `total_by_category()` → `{"FOOD": 2500, "TRANSPORT": 1200, ...}`
  - `monthly_summary(year, month)` → total, top category, count
  - `export_csv(filepath)` and `import_csv(filepath)`
- `Budget`:
  - `set_limit(category, amount)` — set monthly budget per category
  - `check_budget(tracker, year, month)` → list of categories over budget

Rules:
- Amount must be positive
- Category must be from the allowed list
- Use `@dataclass` for `Expense`
- Use `@property` where appropriate
- Write `__repr__` for all classes

**Exercise 4 (Week 4):** Build a **Library Management System** (first version — pure Python, no framework):

Classes:
- `Book`: isbn, title, author, total_copies, available_copies. Methods: `is_available()`, `borrow()` (decrements available), `return_copy()` (increments).
- `Member`: id, name, email, borrowed_books (list of ISBNs), max_books=3. Methods: `can_borrow()`, `borrow_book(isbn)`, `return_book(isbn)`.
- `Library`: books dict (isbn → Book), members dict (id → Member). Methods: `add_book()`, `register_member()`, `borrow_book(member_id, isbn)`, `return_book(member_id, isbn)`, `search(query)`.

Business rules to implement:
- Can't borrow if no copies available → raise `BookNotAvailableError`
- Can't borrow if member has 3 books → raise `BorrowLimitExceededError`
- Can't borrow same book twice → raise `AlreadyBorrowedError`
- Can't return a book you haven't borrowed → raise `NotBorrowedError`
- Search should work on title AND author (case-insensitive partial match)

Test with pytest:
- Test every business rule (at least 15 tests)
- Test happy paths AND error cases
- Use fixtures for common setup (library with books, registered members)

**This is the most important exercise in the entire document.** It teaches: class design, composition, business logic, error handling, and testing — all at once.

### Week 5–6: Error Handling, File I/O, and Modules

| Micro-Topic | What to Know | How Deep | Search Term |
|-------------|-------------|----------|-------------|
| `try/except/else/finally` | `try`: risky code. `except`: handle error. `else`: runs if NO error. `finally`: always runs. | Write code that uses all four | "Python try except else finally" |
| Custom exceptions | Define your own: `class AppError(Exception): pass` → `class NotFoundError(AppError): pass` | Build a 3-level hierarchy for your Library system | "Python custom exception hierarchy" |
| Exception chaining | `raise NewError() from original_error` — preserves the root cause | Use when wrapping low-level errors into domain errors | "Python exception chaining from" |
| `pathlib.Path` | Modern file path handling (better than `os.path`) | Use for ALL file operations | "Python pathlib tutorial" |
| JSON read/write | `json.load()` (file → dict), `json.dump()` (dict → file), `json.loads()` (string → dict) | Save and load application state to JSON files | "Python json file read write" |
| CSV read/write | `csv.reader()`, `csv.writer()`, `csv.DictReader()`, `csv.DictWriter()` | Export data to CSV (spreadsheet-friendly) | "Python csv DictReader DictWriter" |
| YAML | `pyyaml` library for configuration files | Read config from YAML (common in production apps) | "Python pyyaml tutorial" |
| Modules and imports | `import module`, `from module import func`, `__init__.py`, relative imports | Split your Library system into multiple files/modules | "Python modules packages imports" |
| `if __name__ == "__main__"` | Lets a file work as both a script AND an importable module | Add to every file that has a main function | "Python if name main explained" |

**Exercise 5 (Week 5):** Refactor your Library system into a proper multi-file project:

```
library_system/
├── library/
│   ├── __init__.py
│   ├── models.py          (Book, Member classes)
│   ├── services.py        (Library class — the business logic)
│   ├── exceptions.py      (all custom exceptions)
│   ├── storage.py         (save/load to JSON file)
│   └── cli.py             (command-line interface using input())
├── tests/
│   ├── __init__.py
│   ├── test_models.py     (test Book, Member individually)
│   ├── test_services.py   (test Library business rules)
│   └── conftest.py        (shared fixtures)
├── data/
│   └── library.json       (persistence file)
├── pyproject.toml
└── README.md
```

**Exercise 6 (Week 6):** Add these features:
- Persistence: Library state saves to `data/library.json` on every change, loads on startup
- Export: `library.export_report(filepath)` → CSV report of all borrowings
- Configuration: Read `max_books_per_member` and `data_file_path` from a YAML config file
- Logging: Replace all `print()` with `logging.getLogger(__name__)`. Log every borrow/return/error.
- CLI: Simple menu-driven CLI using `input()` that lets you interact with the library

### Week 7–8: Decorators, Generators, and Context Managers

These three topics are what separate "script writers" from "Python developers." Every Python job interview asks about them.

| Micro-Topic | What to Know | How Deep | Search Term |
|-------------|-------------|----------|-------------|
| Simple decorator (no args) | A function that wraps another function. `@wraps` to preserve metadata. | Write `@log_call` that prints function name and args before/after | "Python decorator tutorial beginner" |
| Decorator with arguments | Triple-nested: `def deco(arg)` → `def wrapper(func)` → `def inner(*args)` | Write `@retry(max_attempts=3)` | "Python decorator with arguments" |
| `@property` (you saw this already) | Getter/setter as attributes. `obj.name` instead of `obj.get_name()`. | Add `@property` with validation to your Library models | "Python property decorator" |
| Generators (`yield`) | Lazy evaluation — produces values one at a time, doesn't load all into memory | Write a generator that yields unique user IDs infinitely | "Python generators yield tutorial" |
| Generator expressions | `(x for x in range(10**9))` — like list comprehension but lazy | Compare memory usage: list comp vs generator | "Python generator expression vs list" |
| `itertools` basics | `chain`, `islice`, `groupby`, `product`, `combinations` | Use `islice` to get first 50 items from an infinite generator | "Python itertools practical examples" |
| Context managers (`with`) | `__enter__` and `__exit__` — guaranteed cleanup | Understand why `with open()` is safer than `open()`/`close()` | "Python context manager with statement" |
| `contextlib.contextmanager` | Turn a generator function into a context manager with `@contextmanager` | Write a `@contextmanager` that times a block of code | "Python contextlib contextmanager" |

**Exercise 7 (Week 7):** Build a small decorator library (`utils/decorators.py`):
- `@log_call` — logs function name, arguments, return value, and execution time
- `@retry(max_attempts=3, delay=1.0)` — retries on any exception, with configurable attempts and delay
- `@validate_types` — checks that arguments match type hints (use `inspect` module)
- `@cache_result` — caches return value based on arguments (simple dict-based cache)
- Write unit tests for each decorator

**Exercise 8 (Week 8):** Add to your Library system:
- A generator `unique_member_ids()` that yields unique member IDs forever (never repeats)
- A context manager `database_transaction(library)` that saves to JSON on exit (even if an error occurs)
- Apply `@log_call` to all Library service methods
- Apply `@retry` to the JSON save operation (simulate occasional write failures)

---

## Phase 2: Intermediate Python — Write Real Code (Weeks 9–16)

> **Goal:** Go from "I understand Python concepts" to "I can build non-trivial programs." This phase adds typing, async, testing depth, and packaging — the professional Python skills.

### Week 9–10: Type Hints, Pydantic, and Data Validation

| Micro-Topic | What to Know | How Deep | Search Term |
|-------------|-------------|----------|-------------|
| Basic type hints | `def greet(name: str) -> str:` | Add hints to every function you've written so far | "Python type hints beginner" |
| Complex types | `list[str]`, `dict[str, int]`, `Optional[str]`, `Union[str, int]` | Type-annotate your Library models completely | "Python typing module tutorial" |
| `TypeVar` and generics | `T = TypeVar('T')` for generic functions | Write a generic `find_by_id(items: list[T], id: int) -> T` | "Python TypeVar generics" |
| `mypy` | Static type checker — catches type errors before running | Run `mypy` on your Library project. Fix all errors. | "Python mypy getting started" |
| Pydantic `BaseModel` | Typed, validated data objects with automatic JSON serialization | Model your Library data as Pydantic models | "Pydantic v2 BaseModel tutorial" |
| Pydantic validators | `@field_validator`, `@model_validator` | Validate email format, ISBN format, positive numbers | "Pydantic v2 field_validator" |
| Pydantic `BaseSettings` | Config from environment variables with type coercion | Replace your YAML config with Pydantic BaseSettings | "Pydantic BaseSettings environment" |
| `model_dump()` and `model_validate()` | Convert to/from dicts and JSON | Use for serialization to JSON file | "Pydantic model_dump model_validate" |

**Exercise 9 (Week 9–10):** Rewrite your Library models using Pydantic:
- `BookModel(BaseModel)` with ISBN validation (regex), positive copies validation
- `MemberModel(BaseModel)` with email validation, name length constraint
- `LibraryConfig(BaseSettings)` loaded from environment variables
- `BorrowingRecord(BaseModel)` with date validation
- Run `mypy` on the entire project. Zero errors.

### Week 11–12: Async/Await, HTTP Deep, and `requests` Advanced

| Micro-Topic | What to Know | How Deep | Search Term |
|-------------|-------------|----------|-------------|
| `async def` and `await` | Functions that can pause while waiting for I/O (network, file) | Understand the concept; write 3 async functions | "Python async await beginner tutorial" |
| `asyncio.run()` | Entry point for running async code | Run an async function from `if __name__ == "__main__"` | "Python asyncio.run explained" |
| `asyncio.gather()` | Run multiple async tasks concurrently | Fetch 10 URLs concurrently (compare time vs sequential) | "Python asyncio gather tutorial" |
| `aiohttp` | Async HTTP client library | Make concurrent API calls | "Python aiohttp client tutorial" |
| `requests.Session()` | Persistent connection pooling, shared headers, cookies | Use Session for all API calls (better performance) | "Python requests Session advanced" |
| Retry with `urllib3` | `HTTPAdapter` + `Retry` for automatic retries | Configure retry on your Session: 3 retries, backoff, 500/502/503 | "Python requests retry HTTPAdapter" |
| Timeouts | `timeout=(connect_timeout, read_timeout)` — ALWAYS set timeouts | A request without timeout can hang forever | "Python requests timeout connect read" |
| Error handling for HTTP | Check `response.status_code`, `response.raise_for_status()`, handle `ConnectionError`, `Timeout` | Build a robust API caller that never crashes | "Python requests error handling best practices" |

**Exercise 10 (Week 11):** Build an **API Client** class:
- `BaseAPIClient` class with `__init__(base_url, timeout=10)`, `get(path, params)`, `post(path, json)`, `put(path, json)`, `delete(path)`
- Uses `requests.Session()` internally
- Retry adapter: 3 retries with exponential backoff on 500/502/503
- Timeout on every request
- Returns parsed JSON (dict), not `Response` object
- Raises custom exceptions: `APIError`, `NotFoundError(APIError)`, `ServerError(APIError)`, `TimeoutError(APIError)`
- Structured logging: logs every request (method, URL, status, duration)

**Exercise 11 (Week 12):** Build an async version and compare:
- Same client but using `aiohttp` and `async/await`
- Fetch 20 posts from JSONPlaceholder: sequential vs concurrent (`asyncio.gather`)
- Measure and print the time difference (sequential: ~4 seconds, concurrent: ~0.5 seconds)

### Week 13–14: Testing Like a Developer

You know pytest from QA. Now learn it from the developer side — testing YOUR OWN code, not someone else's API.

| Micro-Topic | What to Know | How Deep | Search Term |
|-------------|-------------|----------|-------------|
| Unit tests vs integration tests | Unit: test one function in isolation. Integration: test multiple components together. | Write both types for your Library system | "Unit test vs integration test Python" |
| Fixtures (deep) | `@pytest.fixture` with `scope`, `yield` (setup/teardown), `params` (parametrize fixtures), fixture factories | Write a fixture that creates and cleans up test data | "pytest fixtures scope yield params" |
| Parametrize | `@pytest.mark.parametrize` — run same test with different data | Parametrize validation tests (valid/invalid inputs × expected outcomes) | "pytest parametrize tutorial" |
| Mocking | `unittest.mock.patch`, `MagicMock`, `Mock` — replace real things with fakes | Mock file I/O in your storage tests (don't actually write files) | "Python unittest mock patch tutorial" |
| `conftest.py` | Shared fixtures across test files, automatic loading | Organize fixtures: one conftest per test directory | "pytest conftest.py tutorial" |
| Test organization | Group by feature (not by type). `test_book.py`, `test_member.py`, `test_library.py` | One test file per module/class | "pytest test organization best practices" |
| Coverage | `pytest-cov` — measure which lines your tests cover | Aim for 80%+ on your Library system | "pytest-cov coverage tutorial" |
| TDD basics | Write the test FIRST, then write the code to make it pass | Try TDD for 3 new features: test → code → refactor | "Test driven development Python tutorial" |

**Exercise 12 (Week 13–14):** Comprehensive test suite for your Library system:
- 40+ tests covering all business rules
- Fixtures: `sample_book`, `sample_member`, `populated_library` (library with 5 books and 3 members)
- Parametrized tests for validation (test 5 invalid ISBNs in one test function)
- Mocked tests for storage (test save/load without touching the filesystem)
- Coverage report: `pytest --cov=library --cov-report=html`
- Target: 85%+ line coverage

### Week 15–16: Packaging, CLI, and Project Polish

| Micro-Topic | What to Know | How Deep | Search Term |
|-------------|-------------|----------|-------------|
| `pyproject.toml` | Modern Python project configuration (PEP 621) | Write one from scratch for your Library project | "pyproject.toml PEP 621 tutorial" |
| Poetry | Dependency management, lockfile, build, publish | `poetry init`, `poetry add`, `poetry install`, `poetry build` | "Poetry Python tutorial" |
| Editable installs | `pip install -e .` — install your package in development mode | Your Library should be importable: `from library.services import Library` | "Python editable install development" |
| `typer` or `click` | Professional CLI frameworks | Replace your `input()` menu with `typer` CLI commands | "Python typer CLI tutorial" |
| `ruff` | Fast Python linter (replaces flake8, isort, pyflakes) | Run on your project. Fix all warnings. | "Python ruff linter setup" |
| `black` | Opinionated code formatter | Format all your code. Never argue about style again. | "Python black formatter" |
| Pre-commit hooks | Auto-run linters/formatters before every commit | Install `pre-commit`, add `ruff` + `black` hooks | "pre-commit Python setup" |
| README | Architecture, setup, usage, tech stack | Write a README that a stranger can follow to run your project | "Good README for Python project" |

**Exercise 13 (Week 15–16):** Polish your Library project into a professional package:
- `pyproject.toml` with Poetry
- CLI via `typer`: `library add-book --title "X" --author "Y" --isbn "Z" --copies 3`
- `ruff` + `black` + `pre-commit` configured
- README with: description, install instructions (3 commands), usage examples, project structure
- GitHub repo with CI (GitHub Actions: lint → test → coverage report)
- Tag: `v1.0.0`

**Milestone: You now have a complete Python project that would impress in an interview.** You've gone from "script writer" to "someone who can build, test, package, and ship Python software."

---

## Phase 3: Web Development with FastAPI (Weeks 17–24)

> **Goal:** Learn to build web APIs. You know how APIs work from testing them — now you build them. This is the most important developer skill.
>
> **SDET track note:** Starting from Week 17, spend 2.5 hrs/week on Master Plan Tier 3 (Pytest internals, hooks, plugin authoring). The Python foundations from Phases 1–2 make this accessible now.

### Why FastAPI

| Framework | Verdict |
|-----------|---------|
| **FastAPI** (chosen) | Uses Pydantic (you just learned it), type-hint driven (you just practiced), auto-generates API docs (you know Swagger from testing), async-native, fastest growing |
| Django | Too much hidden magic — you need to understand how things work first |
| Flask | Too minimal — you'd rebuild what FastAPI gives you free |

### Week 17–18: Your First API

| Micro-Topic | What to Know | How Deep | Search Term |
|-------------|-------------|----------|-------------|
| FastAPI hello world | `@app.get("/")` → `return {"message": "hello"}` | Run it. Visit `localhost:8000/docs`. See the auto-docs. | "FastAPI tutorial first steps" |
| Path parameters | `@app.get("/books/{isbn}")` → `def get_book(isbn: str)` | Build 3 endpoints with path params | "FastAPI path parameters" |
| Query parameters | `@app.get("/books?author=eric&page=1")` → `def list_books(author: str = None, page: int = 1)` | Build 2 endpoints with query params | "FastAPI query parameters" |
| Request body | `@app.post("/books")` → `def create_book(book: BookCreate)` | Pydantic model as input, validated automatically | "FastAPI request body Pydantic" |
| Response model | `@app.get("/books/{isbn}", response_model=BookResponse)` | Control what gets returned (hide internal fields) | "FastAPI response model" |
| Status codes | `status.HTTP_201_CREATED`, `status.HTTP_204_NO_CONTENT` | Return correct codes for each operation | "FastAPI status codes" |
| Error responses | `HTTPException(status_code=404, detail="Book not found")` | Return proper 4xx/5xx errors | "FastAPI HTTPException" |
| `uvicorn` | The server that runs FastAPI | `uvicorn app.main:app --reload` | "FastAPI uvicorn run" |

**Exercise 14 (Week 17–18):** Convert your Library system into a REST API:
- `POST /books` — create a book (201 Created)
- `GET /books` — list all books (with `?author=`, `?title=`, `?page=`, `?size=` query params)
- `GET /books/{isbn}` — get a single book (404 if not found)
- `PUT /books/{isbn}` — update a book
- `DELETE /books/{isbn}` — delete a book (204 No Content)
- `POST /members` — register a member
- `POST /borrow` — borrow a book (request body: `{member_id, isbn}`)
- `POST /return` — return a book
- In-memory storage (dict) for now — database comes in Phase 4
- Visit `/docs` — your auto-generated Swagger UI

### Week 19–20: Authentication and Middleware

| Micro-Topic | What to Know | How Deep | Search Term |
|-------------|-------------|----------|-------------|
| Password hashing | Never store plain passwords. `passlib` + `bcrypt`. | Hash on registration, verify on login | "FastAPI password hashing passlib bcrypt" |
| JWT tokens | `python-jose` library. Create token on login, verify on protected routes. | Understand: header.payload.signature, expiry, claims | "FastAPI JWT authentication tutorial" |
| OAuth2 password flow | FastAPI's built-in `OAuth2PasswordBearer` | Follow the FastAPI Security tutorial step by step | "FastAPI OAuth2 password bearer" |
| Dependency injection | `Depends()` — FastAPI's core pattern for shared logic | `get_current_user` dependency that validates JWT on every protected route | "FastAPI Depends dependency injection" |
| Role-based access | Admin vs regular user — different permissions | Admin can add/delete books. Regular users can only borrow/return. | "FastAPI role based access control" |
| Middleware | Code that runs on EVERY request (before and after) | Logging middleware: log method, path, status, duration for every request | "FastAPI middleware tutorial" |
| CORS | Cross-Origin Resource Sharing — needed when a frontend calls your API | Add `CORSMiddleware` with `allow_origins=["*"]` for development | "FastAPI CORS middleware" |
| `APIRouter` | Organize endpoints into separate files | `routers/books.py`, `routers/auth.py`, `routers/members.py` | "FastAPI APIRouter bigger applications" |

**Exercise 15 (Week 19–20):** Add to your Library API:
- Registration: `POST /auth/register` (email, password, name)
- Login: `POST /auth/login` → returns JWT token
- Protected routes: borrow/return require valid token
- Admin routes: add/delete books require admin role
- Logging middleware
- CORS middleware
- Routes organized with `APIRouter`

### Week 21–22: Testing FastAPI (Your Superpower)

| Micro-Topic | What to Know | How Deep | Search Term |
|-------------|-------------|----------|-------------|
| `TestClient` | `from fastapi.testclient import TestClient` — makes HTTP calls to your app without running the server | Test every endpoint | "FastAPI TestClient testing" |
| Dependency overrides | `app.dependency_overrides[get_db] = mock_db` — swap dependencies in tests | Mock the database, mock auth | "FastAPI testing dependency overrides" |
| Auth in tests | Get a token, pass in `headers={"Authorization": "Bearer <token>"}` | Test protected routes with and without valid tokens | "FastAPI testing authentication" |
| Error testing | Verify your API returns the correct error status and message | Test 404, 400, 401, 403, 409 responses | "FastAPI testing error responses" |

**Exercise 16 (Week 21–22):** Write 50+ tests for your Library API:
- CRUD tests for books (create, read, update, delete)
- CRUD tests for members
- Auth tests (register, login, bad credentials, expired token, missing token)
- Authorization tests (admin routes with non-admin user, protected routes without token)
- Business rule tests (borrow limits, duplicate borrow, return unowned book)
- Edge cases (empty title, negative copies, invalid ISBN, SQL injection strings in input)
- Pagination tests (page 1, page 2, out of range page)

### Week 23–24: Advanced FastAPI Patterns

| Micro-Topic | What to Know | How Deep | Search Term |
|-------------|-------------|----------|-------------|
| Background tasks | `BackgroundTasks` for work that doesn't need to block the response | Send email notification after borrowing | "FastAPI background tasks" |
| API versioning | Prefix routes with `/api/v1/` | Organize routes under versioned prefixes | "FastAPI API versioning" |
| Custom exception handlers | Catch your domain exceptions, return consistent error format | `@app.exception_handler(BookNotAvailableError)` → custom JSON response | "FastAPI custom exception handler" |
| Pagination pattern | Standard pagination response: `{items: [...], total: 42, page: 1, size: 10}` | Build a reusable `PaginatedResponse` model | "FastAPI pagination pattern" |
| Health check | `GET /health` → `{"status": "ok", "version": "1.0.0"}` | Every production API needs this | "FastAPI health check endpoint" |

---

## Phase 4: Databases — SQL and ORM (Weeks 25–32)

> **Goal:** Move from in-memory dicts to a real database. This is the biggest gap for QA-to-developer transitions.
>
> **SDET track note:** During these weeks, work on Master Plan Tier 4 (API & Protocol Engineering) in your 2.5 hrs/week SDET time.

### Week 25–26: PostgreSQL and SQL (Builder Perspective)

| Micro-Topic | What to Know | How Deep | Search Term |
|-------------|-------------|----------|-------------|
| Schema design | Tables, columns, types (VARCHAR, INTEGER, BOOLEAN, TIMESTAMP), PRIMARY KEY | Design 5 tables for your Library system | "PostgreSQL schema design tutorial" |
| Foreign keys | `REFERENCES other_table(id)` — enforces relationships | books ← borrowings → members | "PostgreSQL foreign key tutorial" |
| Constraints | `NOT NULL`, `UNIQUE`, `CHECK`, `DEFAULT` | Enforce data integrity at the database level | "PostgreSQL constraints tutorial" |
| 1:1, 1:N, N:M relationships | One-to-many (member has many borrowings), many-to-many (needs junction table) | Draw the ERD (Entity Relationship Diagram) for your Library | "Database relationships 1 to many many to many" |
| Normalization (1NF, 2NF, 3NF) | Don't repeat data. Each table represents one entity. | Understand why `member_name` should NOT be stored in `borrowings` table | "Database normalization explained simply" |
| Indexes | B-tree index for faster lookups. `CREATE INDEX idx_books_isbn ON books(isbn)` | Add indexes on columns you search frequently | "PostgreSQL indexes when to use" |
| `EXPLAIN ANALYZE` | See how PostgreSQL executes a query. Identify slow queries. | Run on a query with and without an index. See the difference. | "PostgreSQL EXPLAIN ANALYZE tutorial" |
| Docker for PostgreSQL | `docker run -p 5432:5432 -e POSTGRES_PASSWORD=dev postgres:16` | Run PostgreSQL locally without installing it | "PostgreSQL Docker tutorial" |

**Exercise 17 (Week 25–26):** Design and create your Library database:
- Write CREATE TABLE statements for: `users`, `books`, `borrowings`
- Add constraints: NOT NULL, UNIQUE, CHECK, DEFAULT
- Add indexes on frequently searched columns
- Insert 20 books and 5 users manually
- Write 10 queries: JOIN, GROUP BY, HAVING, subquery, window function
- All inside a PostgreSQL container

### Week 27–28: SQLAlchemy ORM

| Micro-Topic | What to Know | How Deep | Search Term |
|-------------|-------------|----------|-------------|
| SQLAlchemy 2.0 models | `class Book(Base)` with `Mapped[]` type annotations and `mapped_column()` | Map your Book, Member, Borrowing to SQLAlchemy models | "SQLAlchemy 2.0 ORM quickstart" |
| Session lifecycle | `Session()` → add/query/commit → close. One session per request in FastAPI. | Create a `get_db` dependency that yields a session | "SQLAlchemy session FastAPI" |
| CRUD operations | `session.add()`, `session.get()`, `session.execute(select(...))`, `session.delete()` | Rewrite all Library operations to use SQLAlchemy | "SQLAlchemy CRUD operations tutorial" |
| Relationships | `relationship()`, `back_populates`, `ForeignKey` | Navigate from Member → their Borrowings → those Books | "SQLAlchemy relationship back_populates" |
| Alembic migrations | Schema versioning. `alembic revision --autogenerate`. `alembic upgrade head`. | Set up Alembic. Create initial migration. Apply it. | "Alembic SQLAlchemy tutorial" |

**Exercise 18 (Week 27–28):** Replace in-memory storage with PostgreSQL:
- Define SQLAlchemy models for your Library
- `get_db` dependency for FastAPI
- Rewrite all CRUD operations
- Set up Alembic, generate and apply migrations
- Docker Compose: FastAPI app + PostgreSQL database

### Week 29–30: Advanced Database Patterns

| Micro-Topic | What to Know | How Deep | Search Term |
|-------------|-------------|----------|-------------|
| N+1 query problem | Loading 100 books + each book's borrowings = 101 queries (BAD) | Use `joinedload()` or `selectinload()` to load in 1-2 queries | "SQLAlchemy N+1 query problem" |
| Dynamic filtering | Build queries based on optional query params | `query = select(Book)` → conditionally add `.where()` clauses | "SQLAlchemy dynamic query building" |
| Offset vs cursor pagination | Offset: `LIMIT 10 OFFSET 20`. Simple but slow on large tables. Cursor: use last item's ID. | Implement both, compare | "Cursor pagination vs offset" |
| Transactions | `session.begin()`, `session.commit()`, `session.rollback()` | Understand atomic operations: borrow = (update book + create borrowing) in ONE transaction | "SQLAlchemy transaction management" |
| Seeding | Script that populates the database with test data | `seed.py` using Faker: 100 books, 30 members, 50 borrowings | "Database seeding Python Faker" |

### Week 31–32: Testing with a Real Database

| Micro-Topic | What to Know | How Deep | Search Term |
|-------------|-------------|----------|-------------|
| Test database | Separate database for tests (never test against production data) | `DATABASE_URL` switches to test DB via environment variable | "FastAPI testing database SQLAlchemy" |
| Transaction rollback per test | Each test runs in a transaction that rolls back — clean state for every test | Override the `get_db` dependency to use a transactional session | "pytest SQLAlchemy transaction rollback" |
| Fixtures for DB tests | Create test data in fixtures, clean up automatically | `@pytest.fixture` that creates a book, yields it, then the transaction rolls back | "pytest fixtures database testing" |
| Integration tests | Test the full stack: HTTP request → FastAPI → SQLAlchemy → PostgreSQL → response | Use `TestClient` with a real test database | "FastAPI integration testing PostgreSQL" |

---

## Phase 5: Build a Full Application (Weeks 33–40)

> **Goal:** Build a complete, real-world application from scratch. This is your portfolio piece.
>
> **SDET track note:** By now you should be working through Master Plan Tier 6 (Test Architecture) and starting the Portfolio Blueprint in your SDET time.

### The Project: Task Manager API

**Why this project:** Real-world complexity. Universally understood by interviewers. Has users, teams, tasks, statuses, comments, permissions.

**Database schema:**
```
users: id, email, password_hash, name, role (admin/member), created_at
teams: id, name, description, owner_id FK, created_at
team_members: id, team_id FK, user_id FK, role (admin/member), joined_at
tasks: id, title, description, status (todo/in_progress/review/done), priority (p0-p3),
       assignee_id FK, team_id FK, creator_id FK, due_date, created_at, updated_at
comments: id, task_id FK, author_id FK, content, created_at, updated_at
```

**Features (build in this order):**

| Week | Features | Skills Practiced |
|------|---------|-----------------|
| 33–34 | User registration, login, JWT auth. Team CRUD. Team membership (invite, remove). | Auth, RBAC, relationships |
| 35–36 | Task CRUD. Assignment. Status workflow (valid transitions only). Priority. Due dates. | State machines, business rules, validation |
| 37–38 | Comments on tasks. Task filtering (by status, assignee, priority, team). Sorting. Pagination. | Dynamic queries, nested resources |
| 39–40 | Activity log (audit trail). Background tasks (overdue notifications). Rate limiting. Docker Compose. CI pipeline. 60+ tests. README with architecture diagram. | Production patterns, deployment |

**Validation criteria:**
- 20+ API endpoints
- 60+ tests (unit + integration)
- JWT auth with role-based access
- PostgreSQL with Alembic migrations
- Docker Compose (app + database)
- GitHub Actions CI (lint → test → build)
- README with architecture diagram, tech stack, setup in 3 commands

---

## Phase 6: Deployment, System Design, and Polish (Weeks 41–48)

> **Goal:** Get your app live. Add production-grade patterns. Prepare for interviews.

### Week 41–42: Deployment

| Topic | What to Do | Resource |
|-------|-----------|----------|
| Multi-stage Dockerfile | Build stage (install deps) + production stage (slim image) | Docker docs: "Multi-stage builds" |
| Deploy to Railway or Render | Push your app to the internet. Free tier. | Railway docs / Render docs |
| CI/CD for deployment | GitHub Actions → push to main → auto-deploy | Platform-specific docs |
| Environment config | `.env.development`, `.env.production`, Pydantic BaseSettings | 12factor.net section III |

### Week 43–44: System Design Additions

| Topic | What to Do | Resource |
|-------|-----------|----------|
| Redis caching | Cache frequently read data (task list). TTL-based expiry. | Redis docs + `redis-py` library |
| Celery background tasks | Email notifications on task assignment. Scheduled overdue checks. | Celery docs: "Getting Started" |
| Repository pattern | Separate database queries into `repositories/` | cosmicpython.com (free) — Chapters 1–4 |
| Architecture diagram | Mermaid diagram in README: Client → API → Service → Repository → DB → Cache | Draw.io or Mermaid syntax |

### Week 45–46: Frontend Basics (Just Enough)

| Topic | How Deep | Time | Resource |
|-------|----------|------|----------|
| HTML + CSS basics | Build one page | 3 hours | FreeCodeCamp: first 2 sections |
| JavaScript basics | Variables, functions, fetch API | 4 hours | JavaScript.info Part 1 |
| React basics | Components, state, props, useEffect | 8 hours | React official docs: "Learn React" |

Build a simple frontend for your Task Manager: login page, task list, create task form. Use a component library (Material UI or Shadcn) to skip CSS.

### Week 47–48: Interview Prep

| Activity | How Much |
|----------|----------|
| LeetCode (Easy + Medium) | 2 problems/day, 30 min. Focus: arrays, strings, hashmaps, two pointers |
| Mock interviews | Practice explaining your Task Manager architecture (5 min pitch) |
| Resume update | Add Task Manager project with tech stack and link |
| GitHub polish | Profile README, pinned repos, commit history |

---

## What to Build — Project Roadmap

| # | Project | Weeks | Skills Proven | Portfolio? |
|---|---------|-------|--------------|-----------|
| 1 | Contact Book CLI | 1–2 | Functions, data structures, file I/O | No |
| 2 | Log Analyzer CLI | 2 | Parsing, filtering, aggregation | No |
| 3 | Expense Tracker (OOP) | 3 | Classes, composition, business logic | No |
| 4 | **Library System** (multi-file, packaged, tested, CLI) | 4–16 | Full Python project: OOP, Pydantic, testing, packaging | Optional |
| 5 | **Library API** (FastAPI + PostgreSQL) | 17–32 | Web APIs, auth, databases, ORM | Optional |
| 6 | **Task Manager API** (full application, deployed) | 33–48 | Complete application development | **Yes — main portfolio piece** |

---

## The Dual-Track Weekly Schedule

### Months 1–4 (Shared Foundation — Phases 1–2)

All 8 hours go to this document. No Master Plan yet.

| Day | Time | Activity |
|-----|------|----------|
| **Mon** | 2 hours | New concept: read docs/article, follow tutorial |
| **Wed** | 2.5 hours | Build: code your exercises, implement features |
| **Fri** | 2 hours | Test + refactor: write tests, run linters, polish |
| **Sat** | 1.5 hours | Review: commit, update README, 1 LeetCode problem (Easy) |

### Month 5 onward (Tracks Diverge — Phases 3–6)

| Day | Time | Track | Activity |
|-----|------|-------|----------|
| **Mon** | 2 hours | Developer | New concept from this document |
| **Wed** | 2.5 hours | Developer | Build: code, implement, test |
| **Fri** | 1 hour | Developer | Polish, commit, review |
| **Fri** | 1 hour | SDET | Master Plan current tier (read + exercise) |
| **Sat** | 1 hour | SDET | Master Plan continued (exercise completion) |
| **Sat** | 0.5 hours | Both | LeetCode (1 problem) + weekly review |

### Rules

1. Every session ends with a git commit. No exceptions.
2. Never spend more than 20 minutes stuck. Ask AI to *explain the concept* (not solve the problem).
3. One topic per week. Don't split attention within a track.
4. Build FIRST, read SECOND. Get confused → then docs make sense.
5. Developer track gets priority. If you're behind, skip SDET that week.
6. LeetCode is a warmup, not the main course. Never spend more than 30 min/day.

---

## Resources — Complete Reference

### Primary Resources (Use These)

| Topic | #1 Resource | Format | Cost |
|-------|------------|--------|------|
| Python fundamentals | Real Python tutorials (specific topic articles) | Articles | Free |
| Python beginner course | Udemy: Angela Yu "100 Days of Code" (days 1–40) | Video + projects | ₹500 on sale |
| OOP | Real Python: "OOP in Python 3" article | Article | Free |
| DSA warmup | Codewars: 8kyu → 6kyu Python (1 problem/day) | Practice | Free |
| Type hints | Real Python: "Python Type Checking" | Article | Free |
| Pydantic | Pydantic v2 official docs | Docs | Free |
| FastAPI | FastAPI official docs (best tutorial in Python ecosystem) | Docs + tutorial | Free |
| SQL | SQLBolt (interactive, in-browser) | Interactive | Free |
| SQLAlchemy | SQLAlchemy 2.0 official docs | Docs | Free |
| Alembic | Alembic official tutorial | Docs | Free |
| Testing (pytest) | TAU: "Intro to Pytest" by Andrew Knight | Course | Free |
| Docker | YouTube: TechWorld with Nana "Docker Tutorial" | Video | Free |
| React basics | React official docs: "Learn React" | Tutorial | Free |
| System design | cosmicpython.com (Architecture Patterns with Python) | Book (online) | Free |
| LeetCode | NeetCode 150 roadmap | Practice | Free |
| Git | Learn Git Branching (interactive) | Interactive | Free |

### Secondary Resources (When Stuck)

| Topic | Resource | Cost |
|-------|---------|------|
| FastAPI video course | Udemy: Sanjeev Thiyagarajan "Complete FastAPI" | ₹500 on sale |
| SQL deeper | Mode Analytics SQL Tutorial | Free |
| JavaScript | JavaScript.info | Free |
| Algorithms (if needed) | "Grokking Algorithms" book | ₹800 |
| System design interviews | YouTube: NeetCode "System Design for Beginners" | Free |

### How to Use Resources (Decision Tree)

```
Is this your FIRST time touching the topic?
├── YES → Is a good Udemy/TAU course available?
│        ├── YES → Take it. Do the projects. (But ONLY one course at a time.)
│        └── NO  → Official docs "Getting Started" + one YouTube video (<20 min).
│
└── NO (you need depth) →
    ├── Is it a tool/library? → Official docs. Build alongside.
    ├── Is it a concept (OOP, HTTP, SQL)? → Real Python article or book chapter.
    └── Is it a quick syntax question? → AI or Stack Overflow. 5 min max.
```

---

## What NOT to Waste Time On

| Don't | Why |
|-------|-----|
| Don't learn Django right now | FastAPI is transparent — you see how everything works. Django hides it. Learn Django later if a job requires it. |
| Don't learn multiple languages simultaneously | Python only. Depth beats breadth. JavaScript only when you reach Phase 6 (frontend). |
| Don't do competitive programming | LeetCode Easy + Medium is enough. Hard problems are rarely asked at your target level. |
| Don't buy 5 Udemy courses at once | You'll finish none. One course at a time. Move to docs after the basics. |
| Don't watch 4-hour YouTube videos without typing | Pause every 10 minutes. Type what you saw. Passive watching = zero retention. |
| Don't study Kubernetes or Terraform yet | You need these for SDET (later). For developer, Docker + a PaaS (Railway/Render) is enough. |
| Don't skip testing | Your QA background is your superpower. Every project must have tests. Most developers can't write good tests — you can. |
| Don't read docs end-to-end like a novel | Read the section you need for your current build. Come back for other sections later. |
| Don't start with system design before building a basic app | You need to build something before you can design systems. Phase 6, not Phase 1. |

---

## Interview Preparation

### Your Unique Pitch

> "I'm a developer who spent 4+ years in QA. I've seen hundreds of bugs in production — I know what bad code causes. Every application I build is tested from day one. I understand APIs from both sides: I've tested thousands of API calls, and I've built complete REST APIs with FastAPI. I bring a quality-first mindset that most developers learn only after years of production incidents."

### Python Questions You Must Be Able to Answer

| Category | Questions | When You'll Know This |
|----------|----------|----------------------|
| Basics | Mutable vs immutable. Pass by reference vs value. `is` vs `==`. | After Phase 1 |
| OOP | Explain SOLID. Inheritance vs composition. What are dunder methods? What is `self`? | After Phase 1 |
| Functions | What are decorators? Generators vs lists? What is a closure? `*args` and `**kwargs`? | After Phase 1 |
| Async | What is the GIL? When to use async? `asyncio.gather` vs sequential? | After Phase 2 |
| Web | How does HTTP work? What is REST? JWT auth flow? CORS? Status codes? | After Phase 3 |
| Database | Normalization. ORM pros/cons. N+1 problem. Indexes. Migrations. Transactions. | After Phase 4 |
| System design | Design a URL shortener. Design a task manager. Caching strategies. | After Phase 6 |
| Testing | Unit vs integration. Mocking. TDD. Coverage. How do you handle flaky tests? | After Phase 2 (your edge) |

### Coding Practice Strategy

| When | Platform | What | Time |
|------|----------|------|------|
| Month 1–4 | Codewars | 8kyu → 6kyu problems. Arrays, strings, dicts. | 15 min/day |
| Month 5–8 | LeetCode Easy | NeetCode 150 roadmap — Easy problems only | 20 min/day |
| Month 9–12 | LeetCode Easy + Medium | Two pointers, hashmaps, sliding window, BFS/DFS basics | 30 min/day |

---

## Progress Tracker

| Phase | Status | Started | Completed | Notes |
|-------|--------|---------|-----------|-------|
| 1: Python Foundations (Weeks 1–8) | Not Started | | | |
| 2: Intermediate Python (Weeks 9–16) | Not Started | | | |
| 3: FastAPI Web Development (Weeks 17–24) | Not Started | | | |
| 4: Databases — SQL and ORM (Weeks 25–32) | Not Started | | | |
| 5: Full Application — Task Manager (Weeks 33–40) | Not Started | | | |
| 6: Deployment, System Design, Polish (Weeks 41–48) | Not Started | | | |

### Monthly Milestones

| Month | Developer Track Milestone | SDET Track Milestone | Proof |
|-------|--------------------------|---------------------|-------|
| 1 | Contact Book + Log Analyzer CLIs done. Functions, data structures solid. | — (shared foundation) | Code committed to GitHub |
| 2 | Library System v1: OOP, multi-file, tested, custom exceptions | — (shared foundation) | 15+ pytest tests passing |
| 3 | Library System v2: decorators, generators, Pydantic, type hints, mypy clean | — (shared foundation) | `mypy` passes with zero errors |
| 4 | Library packaged with Poetry, CLI with typer, pre-commit, CI pipeline | — (shared foundation) | `v1.0.0` tag, green CI badge |
| 5 | Library API with FastAPI: CRUD, auth, middleware, 50+ tests | Master Plan Tier 3 started | Visit `/docs`, all endpoints work |
| 6 | Library API + PostgreSQL: SQLAlchemy, Alembic, real database | Master Plan Tier 3–4 | Docker Compose runs app + DB |
| 7 | Task Manager started: users, teams, tasks, auth | Master Plan Tier 4 | 15+ endpoints |
| 8 | Task Manager complete: all features, 60+ tests, CI | Master Plan Tier 6 started | All tests green |
| 9 | Task Manager deployed to Railway/Render. Live URL. | Portfolio Blueprint started | Shareable URL |
| 10 | Redis + Celery added. Frontend basics. Architecture diagram. | Portfolio repo in progress | Full-stack demo possible |
| 11 | LeetCode practice. Mock interviews. Resume updated. | SDET portfolio polished | 50+ LeetCode problems |
| 12 | Applying to jobs. Both portfolios ready. | SDET tools (Innovation Lab) started | GitHub profile complete |

### Exercise Completion Checklist

| # | Exercise | Phase | Status |
|---|----------|-------|--------|
| 1 | Contact Book CLI | 1 | [ ] |
| 2 | Log Analyzer CLI | 1 | [ ] |
| 3 | Expense Tracker (OOP) | 1 | [ ] |
| 4 | Library System (OOP, business rules, pytest) | 1 | [ ] |
| 5 | Library — multi-file refactor | 1 | [ ] |
| 6 | Library — persistence, config, logging | 1 | [ ] |
| 7 | Decorator library | 1 | [ ] |
| 8 | Library — generators, context managers | 1 | [ ] |
| 9 | Library — Pydantic models, mypy | 2 | [ ] |
| 10 | BaseAPIClient class | 2 | [ ] |
| 11 | Async API client comparison | 2 | [ ] |
| 12 | Library — comprehensive test suite (40+) | 2 | [ ] |
| 13 | Library — Poetry package, typer CLI, CI | 2 | [ ] |
| 14 | Library REST API (FastAPI) | 3 | [ ] |
| 15 | Library API — auth, middleware, routers | 3 | [ ] |
| 16 | Library API — 50+ tests | 3 | [ ] |
| 17 | PostgreSQL schema + queries | 4 | [ ] |
| 18 | Library API + PostgreSQL + Alembic | 4 | [ ] |
| 19 | Task Manager API (complete) | 5 | [ ] |
| 20 | Task Manager deployed + frontend | 6 | [ ] |

---

## How This Document Connects to Your Other Docs

```
THIS DOCUMENT (QA_to_Python_Developer_Transition.md)
│
├── Phases 1–2 (Python foundations)
│   └── Overlaps with: Master Plan Tiers 1–2
│       (Same topics, different angle: building apps vs building test frameworks)
│       DO NOT study both simultaneously. This doc covers it for both paths.
│
├── Phases 3–6 (Web dev, databases, deployment)
│   └── UNIQUE to developer path. Not covered in any other doc.
│
├── SDET track (30% of time, Month 5+)
│   └── Use: Master_SDET_Implementation_Plan.md (Tiers 3–6, 8–9)
│   └── Use: SDET_Portfolio_Blueprint.md (building showcase repo)
│   └── Use: SDET_Innovation_Lab.md (building custom tools)
│
├── Performance testing
│   └── Use: Practical_Performance_Guide.md (when Master Plan reaches Tier 6.4)
│
└── Work context
    └── Use: QA_Roadmap_Deep_Acceptance_Mapping.md (mapping learning to JumpCloud repo)

DO NOT open any other doc during Months 1–4.
Start with this document only. Add others when the schedule says to.
```

---

*You are not starting from zero — you are starting from a different angle. Your QA instinct for finding problems will make you a developer who builds robust systems. The coding ability you build here serves both your developer AND SDET ambitions. Start with Exercise 1. Build the Contact Book. Commit tonight. Everything else follows.*
