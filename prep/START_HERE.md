# START HERE — Your Command Center

**Last updated:** April 2026  
**Your situation:** Manual QA → Automation QA (JumpCloud) → NOW learning to code properly for both Developer and SDET careers  
**Python level:** Beginner (can write scripts and basic pytest, but not deep OOP/decorators/design)  
**Time:** 8 hours/week  
**Split:** 70% Developer / 30% SDET (Developer is primary goal, SDET is secondary)  
**Total documents:** 7

---

## The One Rule

**Follow ONE document at a time.** Do not open all 7 docs and try to study from all of them. This page tells you exactly which document to open, when, and why. Trust the sequence.

---

## Document Inventory

| # | Document | What It Does | When to Use |
|---|----------|-------------|-------------|
| 1 | `QA_to_Python_Developer_Transition.md` | **YOUR PRIMARY DOCUMENT.** Teaches Python from beginner → builds web apps → databases → full application → deployment. 48-week plan with exercises. | Months 1–12. Open this every study session. |
| 2 | `Master_SDET_Implementation_Plan.md` | SDET-specific depth — pytest internals, test architecture, API client patterns, CI/CD engineering. 12 tiers. | Month 5 onward. Start at Tier 3 (skip Tiers 1–2, covered by doc #1). |
| 3 | `SDET_Portfolio_Blueprint.md` | How to build a showcase GitHub repo that proves SDET skills. | Month 8 onward. When you have skills to showcase. |
| 4 | `QA_Learning_Roadmap.md` | Market skills overview, learning platforms, anti-patterns. | Reference only. Skim once, then use for resource lookup. |
| 5 | `QA_Roadmap_Deep_Acceptance_Mapping.md` | Maps every learning topic to exact files in jumpcloud-acceptance. | Reference only. Open when you want to relate a concept to your work codebase. |
| 6 | `Practical_Performance_Guide.md` | Performance testing from zero — concepts, tools, analysis, bottleneck diagnosis. | Month 9+. When Master Plan reaches Tier 6.4. |
| 7 | `SDET_Innovation_Lab.md` | 10 custom tools to build that solve real QA problems. | Month 10+. Pick 3 tools after you have strong Python. |

---

## What to Follow and When — The Exact Sequence

```
╔═══════════════════════════════════════════════════════════════════════════╗
║  MONTHS 1–4: SHARED PYTHON FOUNDATIONS                                   ║
║  All 8 hours/week → QA_to_Python_Developer_Transition.md (Phases 1–2)   ║
║                                                                           ║
║  DO NOT open any other document. These foundations serve BOTH paths.      ║
║  After this you can write real Python: OOP, decorators, generators,      ║
║  testing, packaging, type hints, Pydantic, async basics.                 ║
╚═══════════════════════════════════════════════════════════════════════════╝
         │
         ▼
╔═══════════════════════════════════════════════════════════════════════════╗
║  MONTHS 5–8: TRACKS DIVERGE                                              ║
║                                                                           ║
║  DEVELOPER (5.5 hrs/week) ──────────────────────────────────────────     ║
║  │ QA_to_Python_Developer_Transition.md (Phases 3–4)                     ║
║  │ FastAPI → PostgreSQL → SQLAlchemy → Alembic → Library API             ║
║  │                                                                        ║
║  SDET (2.5 hrs/week) ──────────────────────────────────────────────      ║
║  │ Master_SDET_Implementation_Plan.md (Tier 3: Pytest Internals)         ║
║  │ Then Tier 4: API & Protocol Engineering                               ║
║  │ Skip Tiers 1–2 (already covered by Phases 1–2 above)                 ║
╚═══════════════════════════════════════════════════════════════════════════╝
         │
         ▼
╔═══════════════════════════════════════════════════════════════════════════╗
║  MONTHS 9–12: BUILD AND POLISH                                           ║
║                                                                           ║
║  DEVELOPER (5.5 hrs/week) ──────────────────────────────────────────     ║
║  │ QA_to_Python_Developer_Transition.md (Phases 5–6)                     ║
║  │ Task Manager app → Deploy → System design → Frontend basics           ║
║  │                                                                        ║
║  SDET (2.5 hrs/week) ──────────────────────────────────────────────      ║
║  │ Master Plan Tier 6 (Test Architecture)                                ║
║  │ + SDET_Portfolio_Blueprint.md (start building showcase repo)          ║
║  │ + Practical_Performance_Guide.md (new skill domain)                   ║
║  │ + SDET_Innovation_Lab.md (pick 2–3 tools to build)                   ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

---

## 30-Day Quick Start Checklist

This is your first month. Every action comes from `QA_to_Python_Developer_Transition.md` Phases 1–2. No other document needed.

### Week 1: Setup + Functions + Data Structures

| Day | Action | Done |
|-----|--------|------|
| 1 | Create `dev-learning` GitHub repo. Initialize with README, `.gitignore` (Python), MIT license. Install Python 3.11, create `venv`. | [ ] |
| 2 | Install `pytest`, `requests`, `black`, `ruff`. Freeze to `requirements.txt`. Read Real Python venv article (20 min). | [ ] |
| 3 | Complete [Learn Git Branching](https://learngitbranching.js.org/) — all "Main" sections. Practice on your repo. | [ ] |
| 4 | Start Exercise 1: **Contact Book CLI** — add, search, delete contacts. Store as list of dicts. Save to JSON file. | [ ] |
| 5 | Continue Contact Book: add search by name/email, filter by group, export to JSON. | [ ] |
| 6 | Finish Contact Book: input validation (no duplicate emails, phone must be digits). Test manually. | [ ] |
| 7 | **Review:** Run `black` and `ruff` on all code. Commit. Write in README: "Week 1: Built Contact Book CLI." | [ ] |

### Week 2: More Functions + Start OOP

| Day | Action | Done |
|-----|--------|------|
| 8 | Start Exercise 2: **Log Analyzer CLI** — parse log file, count by level, filter by time range. | [ ] |
| 9 | Finish Log Analyzer: `most_common_errors(top_n=5)`, formatted summary report. Use `Counter`. | [ ] |
| 10 | Read Real Python "OOP in Python 3" article (45 min). | [ ] |
| 11 | Start Exercise 3: **Expense Tracker** — `Expense` dataclass, `ExpenseTracker` class with `add_expense()`, `total_by_category()`. | [ ] |
| 12 | Continue Expense Tracker: `monthly_summary()`, `export_csv()`, `Budget` class with `check_budget()`. | [ ] |
| 13 | Finish Expense Tracker: add `__repr__` to all classes, validate amounts are positive, categories from allowed list. | [ ] |
| 14 | **Review:** Run linters. Write 5 pytest tests for the Expense Tracker. Commit. | [ ] |

### Week 3–4: Library System (The Key Exercise)

| Day | Action | Done |
|-----|--------|------|
| 15 | Start Exercise 4: **Library System** — `Book` class with `is_available()`, `borrow()`, `return_copy()`. | [ ] |
| 16 | Add `Member` class with `can_borrow()`, `borrow_book()`, `return_book()`. Max 3 books rule. | [ ] |
| 17 | Add `Library` class: `add_book()`, `register_member()`, `borrow_book()`, `return_book()`, `search()`. | [ ] |
| 18 | Add custom exceptions: `BookNotAvailableError`, `BorrowLimitExceededError`, `AlreadyBorrowedError`, `NotBorrowedError`. | [ ] |
| 19 | Write pytest tests: 15+ tests covering every business rule (happy paths + error cases). | [ ] |
| 20 | Add fixtures in `conftest.py`: `sample_book`, `sample_member`, `populated_library`. | [ ] |
| 21 | **Review:** All tests green. Linters pass. Commit with message: "feat: library system with full test suite". | [ ] |
| 22–28 | Continue with Exercises 5–6 from the Transition doc: multi-file refactor, persistence, logging, config. | [ ] |
| 29 | Polish: ensure all tests pass, linters clean, README describes the project. | [ ] |
| 30 | **Month 1 Complete.** You have 3 working projects (Contact Book, Log Analyzer/Expense Tracker, Library System) committed to GitHub. | [ ] |

---

## Monthly Milestones — Dual Track

| Month | Developer Track (70%) | SDET Track (30%) | Proof |
|-------|----------------------|-------------------|-------|
| 1 | Contact Book + Log Analyzer + Expense Tracker CLIs | — (shared foundations) | 3 projects committed |
| 2 | Library System: OOP, multi-file, tested, exceptions | — (shared foundations) | 15+ tests passing |
| 3 | Library: decorators, generators, Pydantic, mypy clean | — (shared foundations) | `mypy` zero errors |
| 4 | Library packaged: Poetry, typer CLI, CI pipeline, `v1.0.0` | — (shared foundations) | Green CI badge |
| 5 | Library REST API with FastAPI: CRUD, auth, 50+ tests | Master Plan Tier 3 started | `/docs` Swagger live |
| 6 | Library API + PostgreSQL: SQLAlchemy, Alembic, Docker Compose | Master Plan Tier 3–4 | `docker compose up` works |
| 7 | Task Manager API started: users, teams, tasks, auth | Master Plan Tier 4 | 15+ endpoints |
| 8 | Task Manager complete: all features, 60+ tests, CI | Master Plan Tier 6 + Portfolio Blueprint started | All tests green |
| 9 | Task Manager deployed. Live URL. | Performance Guide started | Shareable URL |
| 10 | Redis + Celery + frontend basics added | Innovation Lab: pick 2 tools | Full-stack demo |
| 11 | LeetCode practice. Mock interviews. Resume updated. | SDET portfolio polished | 50+ LeetCode problems |
| 12 | Applying to jobs. Both portfolios ready. | SDET tools built | GitHub profile complete |

---

## Quick Reference: "I Need to Prepare for X"

### "I have a Python Developer interview next week"

| Focus | Read This | Section |
|-------|----------|---------|
| Python fundamentals | Transition doc | Phase 1–2 (review exercises you built) |
| Web APIs / FastAPI | Transition doc | Phase 3 (FastAPI patterns, auth, middleware) |
| Database / SQL | Transition doc | Phase 4 (schema design, ORM, migrations) |
| System design | Transition doc | Phase 6 (architecture patterns, caching, queues) |
| Coding challenges | LeetCode NeetCode 150 | Easy + Medium |
| "Walk me through a project you built" | Your Task Manager API | Explain architecture, tech choices, testing strategy |

### "I have an SDET interview next week"

| Focus | Read This | Section |
|-------|----------|---------|
| Python depth | Transition doc | Phase 1–2 (same foundations) |
| Pytest internals | Master Plan | Tier 3 (hooks, plugins, fixtures) |
| API testing design | Master Plan | Tier 4 (client architecture, auth, protocols) |
| "Design a test framework" | Master Plan | Tier 12.1 + Appendix B.1 |
| Flaky tests | Portfolio Blueprint | Part 5 (Retry-on-Failure) |
| CI pipeline | Portfolio Blueprint | Part 4 (CI/CD Pipeline) |
| Behavioral questions | Master Plan | Appendix B.3 |

### "I want to relate learning to my JumpCloud work"

| Focus | Read This |
|-------|----------|
| Map any topic to exact files in jumpcloud-acceptance | `QA_Roadmap_Deep_Acceptance_Mapping.md` |
| Understand the acceptance repo's tech stack | Deep Acceptance Mapping → "Cross-cutting: technology stack summary" |
| See how a concept is used in production test code | Deep Acceptance Mapping → find the Phase that matches your current study |

### "I want to find a learning resource for topic X"

| Focus | Read This |
|-------|----------|
| Platform comparison, best resource per topic | `QA_Learning_Roadmap.md` → Sections 8.1–8.5 |
| Resource table for developer topics | `QA_to_Python_Developer_Transition.md` → "Resources — Complete Reference" |
| Resource table for SDET topics | `QA_Learning_Roadmap.md` → Section 8.3 |

---

## How to Use This Knowledge Base Daily

```
Before each study session (2 min):
  1. Open START_HERE.md.
  2. Check which month you're in → find the row in the Monthly Milestones table.
  3. Open the document listed for that month.
  4. Find the exercise or topic you're currently on.

During the study session (1.5–2.5 hours):
  5. Read the micro-topic table. (10–15 min)
  6. Build the exercise. (45–90 min)
  7. Run tests and linters. (5 min)
  8. Commit with a descriptive message. (2 min)

If stuck (> 20 min on same problem):
  9. Copy the "Search Term" from the micro-topic table into Google/YouTube/AI.
  10. Ask AI to explain the CONCEPT (not solve your specific code).
  11. Try again. If still stuck after 20 more min, skip and revisit tomorrow.

Weekly review (15 min, Saturday):
  12. Update the progress tracker in QA_to_Python_Developer_Transition.md.
  13. Update the exercise checklist (check off completed exercises).
  14. Ask yourself: "What can I now explain that I couldn't last week?"
  15. If the answer is "nothing" — you drifted. Get back to the exercises.
```

---

## What NOT to Do

| Mistake | Why It Fails | Fix |
|---------|-------------|-----|
| Open all 7 docs and try to study from all | Overwhelm → paralysis → quit | Follow ONE doc per the sequence above |
| Start the Master Plan in Month 1 | It assumes intermediate Python — you'll get frustrated | Start Master Plan at Month 5, Tier 3 |
| Study SDET and Developer topics in the same session | Context switching kills depth | Monday/Wednesday = Developer. Friday/Saturday = SDET (after Month 5) |
| Skip the exercises and just read | Reading ≠ learning. Only building teaches. | Every session ends with a commit |
| Jump to FastAPI before finishing Phase 1–2 | You'll write bad code and learn bad habits | Trust the sequence. Foundations first. |
| Spend a full week only on LeetCode | LeetCode is dessert, not the main course | Max 30 min/day. Never skip project work for LeetCode. |

---

*This is your command center. It tells you exactly which document to open, when, and why. Don't think about the whole journey — just find today's row in the checklist, open the right document, and build.*
