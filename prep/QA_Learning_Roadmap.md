# QA/SDET Learning Roadmap — Market Skills & How to Learn Them

**Audience:** QE building from scratch by doing, not theory.  
**Constraints:** ~6 hours/week, interview-ready in 3–6 months.  
**Companion doc:** `QA_Roadmap_Deep_Acceptance_Mapping.md` has JumpCloud-specific repo references for every topic here.

---

## 1. Python environment & dependency management

### 1.1 `venv` (virtual environment)

**What it is:** A directory holding a **separate Python + pip + installed packages** per project, preventing system Python pollution.

**Why you need it:**

- Different projects need different `pytest`, `requests`, or `playwright` versions.
- CI runs in clean environments; local `venv` mirrors that.

**Market expectation:** Create/activate a venv, explain why `pip install` without one is risky, debug "wrong package version" issues.

**How to learn:** Read the Real Python article "Python Virtual Environments: A Primer" (free, 20 min), then immediately do it on your machine. Don't watch a video for this.

### 1.2 `requirements.txt`

**What it is:** A flat list of packages (often pinned) installed via `pip install -r requirements.txt`.

**Why it matters:**

- Ubiquitous in tutorials, older services, and small scripts.
- Many CI jobs still use it.
- Quick reproduction: `pip freeze > requirements.txt`.

**Market expectation:** Read a requirements file, explain pins (`==2.32.4`) vs ranges (`>=2.28`), split `requirements-dev.txt` vs prod.

**How to learn:** Same Real Python article covers this. Practice: freeze your venv, delete venv, recreate from file — does it reproduce?

### 1.3 Poetry (`pyproject.toml` + `poetry.lock`)

**What it is:** A project-aware tool: metadata, dependency groups (dev vs main), lockfile for reproducible installs, and CLI entry points — centered on `pyproject.toml`.

**Why teams use it:**

- Reproducible installs via `poetry.lock` (everyone gets the same versions).
- Groups for test tools (`pytest`, `pytest-bdd`, linters) vs runtime libs.
- Modern Python packaging standard.

**Market expectation:** Open `pyproject.toml`, explain `[tool.poetry.dependencies]` vs `[tool.poetry.group.dev.dependencies]`, explain why a lockfile exists.

**How to learn:** Poetry official docs "Basic Usage" page (15 min read). Then: `poetry init` → `poetry add requests pytest` → `poetry run pytest` on a tiny project. Compare the experience to venv+pip.

**Practical learning order:**

1. **`venv` + pip + `requirements.txt`** on a tiny project (mental model: isolation + pins).
2. **Poetry** on a second project (mental model: lockfile, groups, `pyproject.toml`).
3. At work, read your team's `pyproject.toml` and trace how test dependencies are declared.

---

## 2. Skills your resume does not stress (but market expects)

| Area | Why interviewers ask | Mini-outcome you need | Best way to learn |
|------|---------------------|----------------------|-------------------|
| **Git beyond merge** | Every senior QE interview tests this | Rebase, cherry-pick, bisect, resolve conflict | [Learn Git Branching](https://learngitbranching.js.org/) (interactive, free) → then "Pro Git" book chapters 1–3, 7 |
| **Shell / Linux** | CI runs on Linux; scripts glue everything | Write a script: clone → venv → install → run tests → archive logs | [Linux Journey](https://linuxjourney.com/) (free) → [OverTheWire Bandit](https://overthewire.org/wargames/bandit/) levels 1–10 |
| **SQL (joins, aggregates, window functions)** | Data validation, debugging, interview staple | Write 10 queries: joins, GROUP BY, HAVING, window functions | [SQLBolt](https://sqlbolt.com/) (free, interactive) → [Mode Analytics SQL Tutorial](https://mode.com/sql-tutorial/) for window functions |
| **GraphQL testing** | Many modern APIs use GraphQL | Build one test client, run queries + mutations | Official GraphQL docs "Introduction" → Apollo GraphQL tutorials (free) |
| **gRPC testing** | Microservices communication protocol | Build one test client with `grpcurl` or Python `grpcio` | gRPC official "Quick Start" for Python (free) → practice with sample .proto files |
| **Contract testing (Pact)** | Microservices; "how do you prevent breaking consumers?" | One consumer-driven contract demo | Pact official docs "Getting Started" (free) → [Pactflow University](https://docs.pactflow.io/docs/tutorials) (free) |
| **Performance testing (k6 or Locust)** | "Can you load test?" | One script + interpret p95, throughput, error rate | k6 official docs "Getting Started" (free) → YouTube: "k6 Load Testing Tutorial" by k6 team |
| **Security basics (OWASP API Top 10)** | API QE credibility | Name top 5 risks + how you'd test for them | OWASP API Security Top 10 page (free, 30 min read) → practice one injection test on a practice app |
| **Observability with Datadog** | Modern QE monitors test results, correlates failures with system behavior | Create dashboards, query logs/traces, set up alerts, understand APM | Datadog official docs "Getting Started" → Datadog Learning Center (free courses) → practice with free trial account |
| **IaC touch (Terraform)** | Environment provisioning | One module that creates an S3 bucket (nothing expensive) | HashiCorp Learn: "Get Started with Terraform" (free, interactive) |

---

## 3. Constraints & goals

| Input | Value |
|-------|--------|
| Time | ~6 hours/week |
| Docker / K8s comfort today | ~0–1 / 10 |
| Timeline | Interview-ready in 3–6 months |
| Style | Build projects yourself; AI for acceleration, **not** replacement |
| Weak area | Never shipped personal code end-to-end; inconsistency risk — mitigate with daily commits and one focus per week |

---

## 4. Phased roadmap

### Phase 0 — Habits & toolchain (Weeks 1–2)

| Topic | What to build | Best way to learn |
|-------|--------------|-------------------|
| Git | Create `qa-learning-journey` repo; practice branch → PR → merge → rebase → stash → resolve conflict | [Learn Git Branching](https://learngitbranching.js.org/) — do all "Main" + "Remote" sections. Interactive, visual, covers rebase. **Start here day 1.** |
| venv + requirements.txt | Create venv, install packages, freeze, destroy, recreate from file | Real Python "Virtual Environments" article — read once (20 min), then do it |
| Poetry | `poetry init` → `poetry add` → `poetry run pytest` on a second project | Poetry docs "Basic Usage" page — follow the tutorial end-to-end |
| Shell basics | Write a 20-line bash script that automates a simple task | [Linux Journey](https://linuxjourney.com/) — complete "Command Line" and "Text-Fu" modules |
| .gitignore | Create one for Python; verify `git status` hides `.venv`, `__pycache__` | [gitignore.io](https://gitignore.io) — generate for Python, read what each line does |

### Phase 1 — Python + OOP + practical DSA (Weeks 3–8)

| Topic | What to build | Best way to learn |
|-------|--------------|-------------------|
| Python basics | Task Manager CLI: add/list/complete/delete tasks, save to JSON | **Udemy: "100 Days of Code" by Angela Yu** — do days 1–30 only (~₹500 on sale). Project-per-day format. **OR** Real Python beginner tutorials (free) |
| OOP | Library System: `Book`, `Member`, `Library` classes; inheritance (`EBook`); encapsulation | Build first, then read Real Python "OOP in Python 3" article to fill gaps. **Do NOT** watch an OOP theory video before building. |
| DSA for QA | Log Parser: read file, regex, group errors by type, count occurrences | [Codewars](https://www.codewars.com/) 8kyu → 6kyu in Python — 1 problem/day, 15 min. **Plus** "Grokking Algorithms" book chapters 1–6 (optional, visual, excellent) |
| Type hints | Add type hints to all your functions | Real Python "Python Type Checking" article — read relevant sections as you go |
| Formatting / linting | Install `black` + `ruff`, auto-format your code | `pip install black ruff` → run on your code → see what changes. 10 min, no course needed. |

### Phase 2 — API automation, Pytest, BDD, CI/CD (Weeks 9–16)

| Topic | What to build | Best way to learn |
|-------|--------------|-------------------|
| HTTP fundamentals | Understand methods, status codes, headers, auth | MDN Web Docs "An overview of HTTP" — best single explanation, read once (30 min) |
| `requests` library | API Explorer CLI: takes URL + method, makes request, displays response | Real Python "Python's Requests Library (Guide)" — hands-on examples |
| Pytest foundations | Fixtures, parametrize, markers, conftest, hooks | **Test Automation University: "Introduction to Pytest"** by Andrew Knight (free, QA-focused, builds a project). Then official Pytest docs as reference. |
| pytest-bdd | Write `.feature` files + step definitions for your API framework | pytest-bdd official docs — no great course exists; docs are short and clear. Read them + build immediately. |
| API test framework | Full framework: client layer, config (env-based), models (Pydantic), fixtures, custom assertions, logging, Allure reporting, markers | **No single course covers this.** Build it piece by piece. For architecture ideas: read "Python Testing with pytest" book by Brian Okken (chapters on fixtures, plugins, parametrize). |
| GitHub Actions | CI pipeline: install deps → lint → run smoke tests on PR → full suite on schedule → upload artifacts | **GitHub official: "Understanding GitHub Actions"** tutorial (free, short, clear). **Optional:** Udemy "Complete GitHub Actions & Workflows Guide" if you prefer video. |
| Pre-commit hooks | Add `black` + `ruff` as pre-commit hooks to your framework | `pre-commit` official docs "Quick Start" — 10 min setup, works immediately |
| Allure reporting | Add Allure to your framework; generate HTML reports | Allure-pytest docs — install, add decorators, generate report. 30 min. |
| Datadog APM integration | Add `ddtrace` to your API framework; auto-instrument HTTP calls; add test metadata to traces | **ddtrace Python docs "Getting Started"** → **Datadog APM docs "Python"** → practice with free Datadog trial. Add to your framework after it's working. |

### Phase 3 — Playwright + AI in test automation (Weeks 17–22)

| Topic | What to build | Best way to learn |
|-------|--------------|-------------------|
| TypeScript basics | Just enough to write Playwright | **Official TS docs "TypeScript in 5 minutes"** (free). **OR** FreeCodeCamp TypeScript course if you want more depth. Don't spend > 1 week on TS alone. |
| Playwright foundations | Project with Page Objects, fixtures, auto-waiting, locators | **Test Automation University: "Introduction to Playwright"** (free, QA-authored). Then **official Playwright docs** — best-in-class documentation. |
| Playwright advanced | Network interception, API testing, trace viewer, visual comparisons | Official Playwright docs → "Guides" section. **YouTube: LambdaTest "Playwright Tutorial"** series (free) for video format. |
| Playwright + CI | GitHub Actions workflow for Playwright with HTML report upload | Playwright docs "CI" section — has exact GitHub Actions config ready to adapt |
| API + UI combined | Tests that set up data via API, verify via UI, clean up via API | Build yourself; no course teaches this well. Playwright `request` fixture makes it native. |
| AI in test automation | Reusable prompts for test generation, code review, failure analysis | No course. Practice: write prompts that describe your framework's patterns → ask AI to review your code → evaluate if the review is useful. Learn by doing. |
| MCP concepts | Understand what Model Context Protocol is and how it fits QA | Anthropic MCP docs: https://modelcontextprotocol.io/ — the source of truth. Read "Overview" + "Quickstart". |

### Phase 4 — Docker + AWS (Weeks 23–28)

| Topic | What to build | Best way to learn |
|-------|--------------|-------------------|
| Docker fundamentals | Dockerize your API test runner; understand images, containers, layers, volumes, networks | **YouTube: TechWorld with Nana "Docker Tutorial for Beginners"** (free, best single Docker video). Then **[Play with Docker](https://labs.play-with-docker.com/)** for hands-on in browser. |
| Dockerfile | Write Dockerfiles from scratch; multi-stage builds; layer caching optimization | **"Docker Deep Dive" by Nigel Poulton** (book). Read chapters on images + Dockerfiles. Practice immediately. |
| Docker Compose | `docker-compose.yml` with test container + mock API container | Docker Compose docs "Getting Started" tutorial (free, 20 min) |
| `.dockerignore` | Exclude `.venv`, `node_modules`, `.git` from build context | Docker docs — 5 min topic. Read, create, done. |
| AWS foundations | Understand core services: EC2, S3, IAM, Lambda, CloudWatch | **AWS Skill Builder: "AWS Cloud Practitioner Essentials"** (free, official). **OR** Udemy: Stephane Maarek "Ultimate AWS Certified Cloud Practitioner" (~₹500 on sale, best rated). |
| AWS hands-on | Deploy test runner on EC2; store reports in S3; Lambda test trigger; CloudWatch alerts | **AWS Free Tier** — build on real AWS, not simulators. Set billing alerts first. Focus on EC2, S3, IAM, Lambda, CloudWatch chapters only — skip the rest. |
| AWS CLI | `aws s3 cp`, `aws ec2 describe-instances` | AWS CLI docs "Getting Started" — install, configure, run 5 commands. 30 min. |

### Phase 5 — Kubernetes + GCP (Weeks 29–32)

| Topic | What to build | Best way to learn |
|-------|--------------|-------------------|
| Kubernetes fundamentals | Understand Pods, Deployments, Services, ConfigMaps, Secrets | **[Killercoda K8s playgrounds](https://killercoda.com/playgrounds/scenario/kubernetes)** (free, in-browser). Then **YouTube: TechWorld with Nana "Kubernetes Tutorial for Beginners"** (free). |
| kubectl | `get`, `describe`, `logs`, `exec`, `apply`, `port-forward` | Type commands in Killercoda first → then install minikube/kind locally and repeat |
| K8s YAML | Write Deployment, Service, ConfigMap manifests from scratch | **"Kubernetes Up & Running" book** — chapters on Pods, Deployments, Services. Write YAML yourself, don't copy. |
| Helm basics | Understand charts, `values.yaml`, `helm install` | Helm official docs "Getting Started" (free). Just understand what it is and install one chart. Don't go deep. |
| GCP foundations | Compute Engine, Cloud Storage, Cloud Functions, GKE | **GCP Qwiklabs** — "Kubernetes in Google Cloud" quest (free credits). Hands-on in real cloud. |

### Phase 6 — MCP, Cursor skills/agents, polish (Weeks 33–36)

| Topic | What to build | Best way to learn |
|-------|--------------|-------------------|
| MCP servers | Build one MCP tool that solves a narrow QA task (e.g. "summarize last pytest failure from log") | MCP docs "Building servers" tutorial — follow it, then adapt for your use case. You write the code. |
| Cursor rules + skills | `.cursorrules` for your project; one reusable skill | Study examples in open-source repos (many on GitHub now). Then write your own. No course exists. |
| Cursor agents | Automate a multi-step workflow (e.g. run tests → parse failures → create issue) | Cursor official docs + practice. This is learn-by-doing territory. |
| GraphQL testing | One test client; run queries + mutations against a public API | Apollo GraphQL tutorials (free) + practice against https://graphqlzero.almansi.me/ |
| gRPC testing | One test client with `grpcurl` or Python `grpcio` | gRPC Python "Quick Start" docs (free) |
| Contract testing | One Pact consumer-driven contract | Pact "Getting Started" docs (free) |
| Performance testing | One k6 load test script + results analysis | k6 "Getting Started" docs (free) + YouTube: k6 team tutorials |
| Datadog observability | Set up dashboards, alerts, log queries; integrate ddtrace with your test framework; query test results | **Datadog Learning Center** (free courses). **Datadog free trial** (14 days, no credit card). **Datadog docs "Getting Started with APM"** for test tracing. **ddtrace Python docs** for test instrumentation. |

---

## 5. Six hours per week — how to spend them

| Block | Time | Activity |
|-------|------|----------|
| A | 2h | New concept: read docs/article or watch ONE video segment |
| B | 3h | Hands-on coding in your personal repo only |
| C | 1h | Git commit, short README note, 1–3 interview-style questions you can now answer |

**Anti-pattern:** Re-reading the same tutorial without a commit. **Fix:** Ship a tiny change daily.

---

## 6. AI usage policy (helper, not replacement)

| OK | Not OK |
|----|--------|
| Explain a concept or error message | "Write my entire framework" |
| Review your code line-by-line | Generate tests you can't explain |
| Suggest pytest fixture **patterns** | Copy-paste without understanding |
| Draft a checklist for PR review | Let AI author code you submit blindly |
| Explain a Docker error | "Fix my Dockerfile" |

---

## 7. Interview readiness checkpoints

By end of **Month 3:** Explain your **own** API framework design, pytest fixtures, BDD structure, and one CI workflow.  
By end of **Month 5:** Demo Playwright repo + Docker image + AWS deployment.  
By end of **Month 6:** Whiteboard a minimal K8s deploy for a test Job + explain AWS pieces you used + demo one MCP tool.

---

## 8. How to actually start learning (platforms, format, and what to avoid)

### 8.1 Platform comparison (honest take)

| Platform | Best for | Weakness | Cost | Verdict |
|----------|----------|----------|------|---------|
| **Udemy** | Structured beginner courses with projects | Quality varies; many outdated | ₹400–600 on sale (never pay full price) | Good starting point for a topic you know zero about — only buy courses that make you build |
| **LinkedIn Learning** | Corporate soft skills, broad overview | Shallow on coding; rarely builds a real project | Free if employer provides | Skim for overview videos (30 min); do **not** rely on it for depth |
| **YouTube** | Free, latest content, specific topics | No structure; rabbit-hole risk | Free | Best for "how does X work in 10 min" — terrible for a full learning path |
| **Official docs** | Accurate, up-to-date, complete | Can be dry; assumes some knowledge | Free | **Primary source** once you have basics. Read docs → build → re-read docs |
| **FreeCodeCamp / The Odin Project** | Web fundamentals (JS/TS) | Less Python/QA specific | Free | Good for TypeScript before Playwright |
| **Codewars / Exercism** | DSA practice, language fluency | No project context | Free | Daily 15-min warm-up, not primary learning |
| **Real Python** | Python specifically | Subscription for advanced | Free tier is solid | **Best Python tutorials on the internet** for your level |
| **Test Automation University (Applitools)** | QA-specific courses (free!) | Some content aging | Free | **Hidden gem** — Pytest, Playwright, API testing by practitioners |
| **Killercoda / Play-with-Docker / labs.play-with-k8s.com** | Hands-on Docker/K8s in browser | Short exercises, not deep | Free | Perfect warm-up before building your own |
| **AWS Skill Builder / GCP Qwiklabs** | Cloud hands-on labs | Can be dry | Free tier | Use for AWS/GCP phases |
| **SQLBolt** | SQL basics, interactive | Limited advanced topics | Free | Best place to start SQL |
| **Books** | Deep understanding with permanence | Slower than video | ₹500–2000 | Best for Docker, K8s, Algorithms, Pytest — topics where depth matters |

### 8.2 When to use which platform (decision tree)

```
Is this your FIRST time touching the topic?
├─ YES → Is a good Udemy/TAU course available?
│        ├─ YES → Buy it (on sale). Do days/chapters that BUILD things.
│        └─ NO  → Read the official docs "Getting Started" + one YouTube video.
│
└─ NO (you've seen it before, need depth) →
   ├─ Is it a tool/library? → Official docs only. Build alongside.
   ├─ Is it a concept (OOP, DSA, HTTP)? → Book or Real Python article.
   └─ Is it a quick syntax question? → AI or Stack Overflow. 5 min max.
```

### 8.3 Best resource per topic (quick reference)

| Topic | #1 Resource | #2 Backup | Format | Time to cover |
|-------|------------|-----------|--------|---------------|
| Git | [Learn Git Branching](https://learngitbranching.js.org/) | "Pro Git" book ch. 1–3, 7 | Interactive + book | 3–4 hours |
| Shell / Linux | [Linux Journey](https://linuxjourney.com/) | OverTheWire Bandit levels 1–10 | Interactive | 3–4 hours |
| Python basics | Udemy: Angela Yu "100 Days" (days 1–30) | Real Python beginner path | Video + projects | 15–20 hours |
| OOP | Build Library project → Real Python "OOP in Python" | — | Build + article | 6–8 hours |
| DSA for QA | Codewars 8kyu→6kyu | "Grokking Algorithms" ch. 1–6 | Practice + book | Ongoing, 15 min/day |
| SQL | [SQLBolt](https://sqlbolt.com/) | Mode Analytics SQL tutorial | Interactive | 4–5 hours |
| HTTP | MDN "An overview of HTTP" | — | Article | 30 min |
| `requests` library | Real Python guide | — | Article | 1 hour |
| Pytest | TAU: "Intro to Pytest" (Andrew Knight) | Official pytest docs | Course + docs | 4–5 hours |
| pytest-bdd | Official pytest-bdd docs | — | Docs | 2–3 hours |
| API framework design | "Python Testing with pytest" (Brian Okken book) | — | Book | 8–10 hours (across weeks) |
| GitHub Actions | GitHub official tutorial | Udemy "Complete GitHub Actions" (optional) | Docs | 3–4 hours |
| TypeScript basics | Official "TS in 5 minutes" | FreeCodeCamp TS course | Docs / course | 3–5 hours |
| Playwright | TAU: "Intro to Playwright" | Official Playwright docs | Course + docs | 6–8 hours |
| Docker | YouTube: TechWorld with Nana | "Docker Deep Dive" book | Video + book | 8–10 hours |
| Docker hands-on | [Play with Docker](https://labs.play-with-docker.com/) | — | Lab | 2–3 hours |
| AWS | AWS Skill Builder: Cloud Practitioner | Udemy: Stephane Maarek CCP | Course | 10–15 hours |
| Kubernetes | [Killercoda playgrounds](https://killercoda.com/) | YouTube: TechWorld with Nana K8s | Lab + video | 8–10 hours |
| K8s deeper | "Kubernetes Up & Running" book | — | Book | 10–12 hours |
| GCP | GCP Qwiklabs: K8s in Google Cloud | — | Lab | 4–6 hours |
| MCP | Official MCP docs | — | Docs | 3–4 hours |
| Contract testing | Pact "Getting Started" docs | Pactflow University | Docs | 3–4 hours |
| Performance testing | k6 "Getting Started" docs | YouTube: k6 tutorials | Docs + video | 3–4 hours |
| Security basics | OWASP API Top 10 page | — | Article | 1–2 hours |
| Datadog observability | Datadog Learning Center courses | Datadog official docs "Getting Started" | Course + docs | 6–8 hours |
| Terraform | HashiCorp Learn "Get Started" | — | Interactive | 3–4 hours |

### 8.4 The learning loop (apply to every topic)

```
1. SKIM (15 min)
   Read docs/article or watch ONE short video.
   Understand the "what" and "why".

2. BUILD (45–60 min)
   Type code yourself. No copy-paste.
   Break it intentionally, then fix it.

3. RELATE (15 min)
   Open your team's real codebase.
   Find the same concept in production code.
   (See companion doc for exact file references.)

4. COMMIT (5 min)
   Push to your qa-learning-journey repo.
   One-line commit message of what you learned.

5. EXPLAIN (5 min, optional but high value)
   Write 2–3 lines in your README:
   "Today I learned X because Y."
   If you can't explain it, you don't know it yet.
```

### 8.5 What NOT to do (anti-patterns)

| Anti-pattern | Why it fails | Fix |
|-------------|-------------|-----|
| Buy 5 Udemy courses at once | You'll never finish any | **One course at a time.** Start next only after project is done |
| Watch 4-hour video without typing | Passive; zero retention | **Pause every 10 min, type what you saw** |
| Read docs end-to-end like a novel | You'll forget 90% | **Read only the section you need for your current build** |
| Start with K8s when Python is shaky | Skipping foundations causes loop-backs | **Follow the phase order** |
| Learn Docker theory without installing Docker | "I understand it conceptually" ≠ knowing it | **`docker run hello-world` on day 1** |
| Switch topics when stuck | Creates inconsistency (your weakness) | **20 min stuck → ask AI to explain the concept → try again** |
| Use LinkedIn Learning as main resource | Too shallow; won't build real skill | **Use it for 30-min topic overviews only** |
| Take notes without building | Notes rot; code lasts | **Every session ends with a commit** |

---

## 9. Minor topics that live inside each phase (don't skip these)

These are "small" things that trip people up in interviews and daily work. They don't deserve a separate phase but **must be learned when you encounter them naturally**.

### 9.1 Python ecosystem

| Topic | Learn when | What to know | How to learn | 5-min practice |
|-------|-----------|-------------|-------------|----------------|
| `venv` creation + activation | Phase 0, day 1 | `python3 -m venv .venv && source .venv/bin/activate`; `deactivate`; `.venv` in `.gitignore` | Real Python venv article | Create venv, install `requests`, verify `which python` |
| `requirements.txt` | Phase 0, day 2 | `pip freeze > requirements.txt`; pins vs ranges | Same article | Freeze → delete venv → recreate from file |
| `pyenv` (version manager) | Phase 0 | Switch between Python 3.10/3.11/3.12 per project | pyenv GitHub README | `pyenv install 3.11.9 && pyenv local 3.11.9` |
| Poetry basics | Phase 0, day 3 | `poetry init`, `add`, `install`, `run pytest`, `poetry.lock` | Poetry docs "Basic Usage" | Init project, add `pytest`, run test |
| Poetry groups | Phase 2 | `poetry add --group dev pytest` → `[tool.poetry.group.dev.dependencies]` | Poetry docs "Managing dependencies" | Add one dev dep, one main dep, compare |
| `__init__.py` | Phase 1 | Makes directory a Python package; can be empty | Python official tutorial "Packages" | Create package, import from it |
| `if __name__ == "__main__"` | Phase 1 | Lets file run as script AND be importable | Real Python article on this topic | Add to CLI, verify both modes work |
| `.env` + `python-dotenv` | Phase 2 | Store secrets outside code; load with `dotenv`; `.env` in `.gitignore` | python-dotenv README | Create `.env`, load in code |
| Type hints | Phase 1–2 | `def get_user(user_id: int) -> dict:` | Real Python "Type Checking" | Add hints, run `mypy` once |
| `logging` module | Phase 2 | `logging.getLogger(__name__)` > `print()` | Python docs logging HOWTO | Replace prints with logging |
| Decorators | Phase 2 | A function wrapping another; understand `@pytest.fixture`, `@pytest.mark` | Real Python "Primer on Decorators" | Write `@timer` decorator |
| Context managers (`with`) | Phase 2 | `with open(...) as f:` — auto-cleanup | Real Python article | Write custom context manager |
| Comprehensions | Phase 1 | `[x for x in items if x > 5]` — Pythonic, interview favorite | Real Python "List Comprehensions" | Rewrite 3 loops as comprehensions |
| `*args`, `**kwargs` | Phase 2 | Variable arguments; used in fixture factories | Real Python article | Write function using `**kwargs` |
| Pydantic / dataclasses | Phase 2 | Structured data > raw dicts; schema validation | Pydantic docs "Getting Started" | Model API response as `BaseModel` |

### 9.2 Observability

| Topic | Learn when | What to know | How to learn | 5-min practice |
|-------|-----------|-------------|-------------|----------------|
| Datadog APM basics | Phase 2 (when building API framework) | What traces, spans, logs, metrics are; how they connect | Datadog docs "APM Concepts" | Sign up for free trial, send one trace |
| Datadog dashboards | Phase 6 (polish) | Create widgets, time series, query syntax | Datadog docs "Dashboards" | Create dashboard with 2 widgets |
| Datadog log queries | Phase 2+ (when debugging) | Log search syntax, filters, facets | Datadog docs "Log Search Syntax" | Write query to find errors in last hour |
| Datadog alerts | Phase 6 (polish) | Set up monitors, notification channels | Datadog docs "Alerting" | Create alert for high error rate |
| ddtrace Python library | Phase 2 (API framework integration) | Auto-instrument HTTP calls, custom spans | ddtrace docs "Python" | Add tracing to one API call |

### 9.3 Tooling

| Topic | Learn when | What to know | How to learn |
|-------|-----------|-------------|-------------|
| `.gitignore` | Phase 0, day 1 | `.venv/`, `__pycache__/`, `.env`, `node_modules/`, `.pytest_cache/` | [gitignore.io](https://gitignore.io) |
| Pre-commit hooks | Phase 2 | Auto-run linters before commit | `pre-commit` docs "Quick Start" |
| `black` (formatter) | Phase 1 | Auto-format to consistent style | `pip install black && black .` |
| `ruff` (linter) | Phase 1 | Fast linter replacing flake8, isort | `pip install ruff && ruff check .` |
| `mypy` (type checker) | Phase 2 | Static type checking | `pip install mypy && mypy src/` |
| `Makefile` | Phase 2 | `make test`, `make lint`, `make install` | Write one with 3 targets |
| `pytest.ini` / `pyproject.toml [tool.pytest]` | Phase 2 | Default options, test paths, markers | Pytest docs "Configuration" |
| `conftest.py` scoping | Phase 2 | Root = global fixtures; directory = scoped | Pytest docs "conftest.py" |
| Allure reporting | Phase 2 end | Rich HTML reports with steps, history | allure-pytest docs |
| `.editorconfig` | Phase 0 | Consistent indentation across editors | editorconfig.org |

### 9.4 Playwright

| Topic | Learn when | What to know | How to learn |
|-------|-----------|-------------|-------------|
| `package.json` scripts | Phase 3, day 1 | `"test": "npx playwright test"` | npm docs "scripts" |
| `npx` vs `npm` | Phase 3, day 1 | `npx` runs binary; `npm` manages packages | npm docs |
| `tsconfig.json` | Phase 3 | TypeScript compiler config | TS docs "tsconfig" |
| Trace viewer | Phase 3 | `npx playwright show-trace trace.zip` | Playwright docs "Trace viewer" |

### 9.5 Docker

| Topic | Learn when | What to know | How to learn |
|-------|-----------|-------------|-------------|
| `.dockerignore` | Phase 4, day 1 | Exclude `.venv`, `node_modules`, `.git` from build | Docker docs |
| `COPY` vs `ADD` | Phase 4 | `COPY` for files; `ADD` can untar (prefer `COPY`) | Docker docs "Dockerfile reference" |
| `CMD` vs `ENTRYPOINT` | Phase 4 | `ENTRYPOINT` = what runs; `CMD` = default args | Same docs |
| Multi-stage builds | Phase 4, week 2 | Smaller images: build in one stage, copy to lean stage | Docker docs "Multi-stage builds" |
| Volume mounts | Phase 4 | `-v $(pwd):/app` → live code in container | Docker docs |
| `docker exec` | Phase 4 | `docker exec -it <id> bash` → inspect container | Practice on any container |

### 9.6 CI/CD

| Topic | Learn when | What to know | How to learn |
|-------|-----------|-------------|-------------|
| Secrets | Phase 2 CI | `${{ secrets.API_KEY }}` — never hardcode | GitHub Actions docs "Encrypted secrets" |
| Matrix builds | Phase 2 CI | Test across Python 3.10, 3.11, 3.12 in parallel | GitHub Actions docs "Using a matrix" |
| Caching | Phase 2 CI | `actions/cache` → faster builds | GitHub Actions docs "Caching" |
| Artifacts | Phase 2 CI | Upload test reports as build artifacts | GitHub Actions docs "Storing artifacts" |
| Branch protection | Phase 2 CI | Require passing checks before merge | GitHub docs "Branch protection rules" |

### 9.7 Cloud / K8s

| Topic | Learn when | What to know | How to learn |
|-------|-----------|-------------|-------------|
| `~/.aws/credentials` | Phase 4 | Local AWS config; never commit | AWS CLI docs "Configuration" |
| AWS CLI basics | Phase 4 | `aws s3 cp`, `aws ec2 describe-instances` | AWS CLI docs + practice |
| `kubectl config` | Phase 5 | Contexts, switching clusters | K8s docs "Configure Access" |
| `helm` basics | Phase 5 end | Charts, `values.yaml`, `helm install` | Helm docs "Getting Started" |
| Labels and selectors | Phase 5 | How K8s objects find each other | K8s docs "Labels and Selectors" |

### 9.8 Rule: when you encounter a "minor" topic

```
1. Stop for 15 minutes (no more).
2. Read the official docs section for that ONE thing.
3. Try it in your terminal / code.
4. If it works → commit and move on.
5. If it doesn't → ask AI to explain the error (not fix it).
6. Add one-line note to README: "Learned: venv activation syntax."
7. Never open a 2-hour YouTube video for a 15-minute topic.
```

---

## 10. Document maintenance

- Update this file when you **finish a phase** (date + link to your personal repo tag).
- This document is **market-generic** — safe to share externally.
- For JumpCloud-specific repo references, use the companion doc `QA_Roadmap_Deep_Acceptance_Mapping.md`.

---

*Market-specific QA/SDET learning roadmap with practical study resources for each topic.*
