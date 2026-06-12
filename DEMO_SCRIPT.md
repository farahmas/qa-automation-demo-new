# Demo Script

## Presentation topic

**QA and Automation: Code Review / Static Code Analysis / CI/CD**

Audience: students and beginners.

Main goal: show how automated QA checks and code review improve software quality.

---

## Before the demo

Prepare the project:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

For Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

---

# Step 1: Show the application code

Open:

```text
app/calculator.py
```

Say:

> First, we have a very small calculator application. It has functions for addition, subtraction, multiplication, and division.
>
> In a real company, the application would be bigger, but the idea is the same: we write code, then we check its quality.

Point to:

```python
def divide(a: float, b: float) -> float:
```

Say:

> Division is interesting because it has an edge case: division by zero.

---

# Step 2: Show the unit tests

Open:

```text
tests/test_calculator.py
```

Say:

> Unit tests check small parts of the application. Here, each test checks one function.
>
> Tests are important because they can run automatically and quickly.

Point to:

```python
def test_divide_by_zero_should_raise_error():
```

Say:

> This test checks an edge case. It expects the application to raise an error when we divide by zero.

---

# Step 3: Run tests and show a failing test

For the demo, temporarily change `app/calculator.py`.

Replace:

```python
if b == 0:
    raise ValueError("Cannot divide by zero")
```

with:

```python
if b == 0:
    return 0
```

Run:

```bash
pytest -v
```

Expected result:

```text
FAILED tests/test_calculator.py::test_divide_by_zero_should_raise_error
```

Say:

> The test failed. This is good because the test found a real problem.
>
> The function returned zero, but mathematically division by zero is invalid.
>
> QA automation helps us catch this before users or customers see it.

---

# Step 4: Fix the bug

Change the code back:

```python
if b == 0:
    raise ValueError("Cannot divide by zero")
```

Run:

```bash
pytest -v
```

Say:

> Now all tests pass.
>
> This means our fix works and the previous bug is covered by an automated test.

---

# Step 5: Run static code analysis

Run:

```bash
ruff check .
```

Open:

```text
app/bad_code_for_static_analysis.py
```

Say:

> Static code analysis checks the code without running the application.
>
> It helps find code quality problems such as unused imports, bad naming, formatting issues, and simple mistakes.

Explain possible Ruff findings:

```text
F401 unused import
N802 function name should be lowercase
F841 local variable is assigned but never used
```

Say:

> These issues may not always break the program immediately, but they make the code harder to maintain.

Optional command:

```bash
ruff check . --fix
```

Say:

> Some problems can be fixed automatically, but not all. Design problems still need human thinking.

---

# Step 6: Show code review comments

Open:

```text
CODE_REVIEW.md
```

Say:

> Code review is a human quality check.
>
> Automated tools can find many problems, but humans can notice unclear logic, duplicated code, missing tests, and risky design choices.

Show these review categories:

- naming issue
- duplicated code
- missing test
- possible bug
- security or quality concern

Say:

> Good code review is not about blaming people. It is about improving the product and helping the team learn.

---

# Step 7: Show GitHub Actions CI pipeline

Open:

```text
.github/workflows/ci.yml
```

Say:

> This is the CI pipeline. CI means Continuous Integration.
>
> Every time we push code or create a pull request, GitHub Actions runs the checks automatically.

Point to these sections:

```yaml
- name: Install dependencies
```

```yaml
- name: Run static code analysis
```

```yaml
- name: Run unit tests
```

Say:

> The pipeline installs dependencies, runs static analysis, and runs tests.
>
> If any step fails, the pipeline becomes red.

---

# Step 8: Explain the final result

Say:

> Today we saw three quality gates.
>
> First, unit tests checked if the application behaves correctly.
>
> Second, static analysis checked code quality.
>
> Third, CI/CD ran these checks automatically in GitHub.
>
> Code review adds a human quality gate on top of automation.
>
> Together, these practices help teams find bugs earlier, improve code quality, and release software with more confidence.

---

# Terminal commands to run during demo

## Install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run app

```bash
uvicorn app.main:app --reload
```

## Run tests

```bash
pytest -v
```

## Run static analysis

```bash
ruff check .
```

## Auto-fix static analysis issues

```bash
ruff check . --fix
```

## Git commands

```bash
git init
git add .
git commit -m "Add QA automation demo project"
git branch -M main
git remote add origin YOUR_GITHUB_REPO_URL
git push -u origin main
```

---

# What to say on each demo stage

## When showing app code

> This is our application code. It is small, but the same QA process applies to bigger projects.

## When showing tests

> Tests describe what correct behavior means. If the behavior changes incorrectly, tests fail.

## When test fails

> A failed test is not bad. It gives us useful information. It tells us exactly where the behavior is wrong.

## When fixing the bug

> After fixing the code, we run the same test again. Passing tests give confidence that the bug is fixed.

## When running static analysis

> Static analysis checks style and quality automatically. It is like an automatic reviewer for common mistakes.

## When showing code review

> Code review catches things that tools may miss, such as duplicated logic, unclear design, or missing tests.

## When showing CI/CD

> CI/CD makes quality checks automatic. Developers do not need to remember to run everything manually.

## Final conclusion

> QA automation is not only testing. It is a full quality process: tests, static analysis, code review, and CI/CD working together.

---

# Screenshots for presentation

Add these screenshots:

1. VS Code project structure.
2. Calculator code in `app/calculator.py`.
3. Unit tests in `tests/test_calculator.py`.
4. Failed test output in terminal.
5. Fixed code.
6. Passed test output in terminal.
7. Ruff output in terminal.
8. Code review comments from `CODE_REVIEW.md`.
9. GitHub Actions workflow file.
10. GitHub Actions result page.
