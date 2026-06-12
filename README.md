# QA Automation Demo Project

## Topic

**QA and Automation: Code Review / Static Code Analysis / CI/CD**

This is a small Python demo project for students.
It shows how QA automation works in a real development workflow.

The project includes:

- simple application code
- unit tests
- API tests
- one intentional bug for demo
- static code analysis with Ruff
- code review examples
- GitHub Actions CI pipeline

---

## Project idea

The application is a mini calculator API.

It supports:

- addition
- subtraction
- multiplication
- division

The app has two layers:

1. **Business logic** in `app/calculator.py`
2. **API layer** in `app/main.py`

This is useful for teaching because students can see that tests can check both:

- normal Python functions
- API endpoints

---

## Project structure

```text
qa-automation-demo/
├── app/
│   ├── __init__.py
│   ├── calculator.py
│   ├── calculator_buggy.py
│   ├── main.py
│   └── bad_code_for_static_analysis.py
├── tests/
│   ├── test_calculator.py
│   └── test_api.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── CODE_REVIEW.md
├── DEMO_SCRIPT.md
├── README.md
├── pyproject.toml
└── requirements.txt
```

---

## What each file does

### `app/calculator.py`

Contains the main calculator logic.

Example:

```python
def add(a: float, b: float) -> float:
    return a + b
```

This file is the main code that unit tests check.

---

### `app/calculator_buggy.py`

Contains a buggy version of the calculator logic.

Bug:

```python
if b == 0:
    return 0
```

This is wrong because division by zero should not return zero.
It should raise an error.

Use this file during the live demo to show how a test can catch a bug.

---

### `app/main.py`

Contains a small FastAPI application.

You can run it and open Swagger UI in the browser.

---

### `tests/test_calculator.py`

Contains unit tests for calculator functions.

Example:

```python
def test_add_two_numbers():
    assert add(2, 3) == 5
```

---

### `tests/test_api.py`

Contains tests for the API endpoint.

---

### `app/bad_code_for_static_analysis.py`

This file intentionally contains bad code.

It has:

- unused imports
- bad function name
- formatting problem
- unused variable
- duplicated logic

The goal is to show what static analysis can find automatically.

---

### `CODE_REVIEW.md`

Contains example code review comments.

---

### `.github/workflows/ci.yml`

Contains the GitHub Actions CI pipeline.

The pipeline runs automatically on:

- push to `main`
- pull request to `main`

It runs:

1. install dependencies
2. static code analysis
3. unit tests

---

## How to install dependencies

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it.

On macOS or Linux:

```bash
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## How to run the application

Run:

```bash
uvicorn app.main:app --reload
```

Open in browser:

```text
http://127.0.0.1:8000/docs
```

You will see FastAPI Swagger UI.

Try this request:

```json
{
  "operation": "add",
  "a": 2,
  "b": 3
}
```

Expected response:

```json
{
  "result": 5
}
```

---

## How to run unit tests

Run:

```bash
pytest -v
```

Expected result after the bug is fixed:

```text
tests/test_calculator.py::test_add_two_numbers PASSED
tests/test_calculator.py::test_subtract_two_numbers PASSED
tests/test_calculator.py::test_multiply_two_numbers PASSED
tests/test_calculator.py::test_divide_two_numbers PASSED
tests/test_calculator.py::test_divide_by_zero_should_raise_error PASSED
tests/test_calculator.py::test_calculate_unknown_operation_should_raise_error PASSED
tests/test_api.py::test_health_check PASSED
tests/test_api.py::test_calculate_add_endpoint PASSED
tests/test_api.py::test_calculate_divide_by_zero_endpoint PASSED
```

---

## How to demonstrate a failing test

During the live demo, replace the correct `divide` function in `app/calculator.py` with this buggy version:

```python
def divide(a: float, b: float) -> float:
    if b == 0:
        return 0

    return a / b
```

Then run:

```bash
pytest -v
```

The test `test_divide_by_zero_should_raise_error` should fail.

Why?

Because the test expects a `ValueError`, but the function returns `0`.

This shows how QA can catch hidden bugs automatically.

---

## How to fix the bug

Change the function back to:

```python
def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")

    return a / b
```

Run tests again:

```bash
pytest -v
```

Now the tests should pass.

---

## How to run static code analysis

Run:

```bash
ruff check .
```

Ruff will check the code and report quality issues.

It should find problems in:

```text
app/bad_code_for_static_analysis.py
```

Example issues:

- unused import
- bad function name
- unused variable
- formatting/style issue

This shows that static analysis can find problems before the code is run.

---

## How to auto-fix some static analysis issues

Run:

```bash
ruff check . --fix
```

Ruff can automatically fix some problems, for example unused imports.

However, it cannot fix every design problem.
For example, duplicated logic usually needs a human review.

---

## How CI/CD works in this project

CI/CD means **Continuous Integration / Continuous Delivery**.

In this demo, GitHub Actions runs checks automatically.

When a developer pushes code or opens a pull request, GitHub Actions will:

1. download the repository
2. install Python
3. install dependencies
4. run Ruff static analysis
5. run Pytest tests

If something fails, the pipeline becomes red.

This means the team knows the code is not ready to merge.

If everything passes, the pipeline becomes green.

This means the code passed the automated quality checks.

---

## What to show during live demo

### 1. Show the app code

Open:

```text
app/calculator.py
```

Say:

> This is the main business logic. It is simple, but it represents real production code.

---

### 2. Show tests

Open:

```text
tests/test_calculator.py
```

Say:

> These tests verify expected behavior. Tests are automated checks that help QA find bugs faster.

---

### 3. Show a failing test

Temporarily add the bug to `divide`.

Run:

```bash
pytest -v
```

Say:

> The test failed because the function returned zero instead of raising an error. This is exactly how QA automation catches hidden problems.

---

### 4. Fix the bug

Change the function to raise `ValueError`.

Run:

```bash
pytest -v
```

Say:

> After the fix, the same test passes. This gives us confidence that the bug is solved.

---

### 5. Show static analysis

Run:

```bash
ruff check .
```

Say:

> Static analysis checks code quality without running the application. It can catch unused imports, naming problems, formatting issues, and other quality problems.

---

### 6. Show code review

Open:

```text
CODE_REVIEW.md
```

Say:

> Automated tools are helpful, but human review is also important. Code review can catch design issues, duplicated logic, missing tests, and unclear code.

---

### 7. Show CI/CD pipeline

Open:

```text
.github/workflows/ci.yml
```

Say:

> This file tells GitHub Actions what to run automatically on every push or pull request.

---

### 8. Show GitHub Actions result

After pushing to GitHub, open the Actions tab.

Say:

> Green means all checks passed. Red means at least one quality gate failed.

---

## Screenshots to add to presentation

Good screenshots:

1. Project structure in VS Code.
2. `app/calculator.py` with the calculator functions.
3. `tests/test_calculator.py` with the failing test.
4. Terminal output with failed Pytest test.
5. Terminal output after bug fix, showing tests passed.
6. Terminal output from `ruff check .`.
7. `CODE_REVIEW.md` review comments.
8. `.github/workflows/ci.yml`.
9. GitHub Actions page with failed pipeline.
10. GitHub Actions page with successful pipeline.

---

## Final terminal command list

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
pytest -v
ruff check .
ruff check . --fix
git add .
git commit -m "Add QA automation demo project"
git push
```

On Windows PowerShell, activation is:

```powershell
.\.venv\Scripts\Activate.ps1
```

---

## Main lesson

This demo shows three quality gates:

1. **Unit tests** check if the code works correctly.
2. **Static code analysis** checks if the code is clean and follows standards.
3. **CI/CD pipeline** runs checks automatically before code is merged.

Together, they help teams build better software faster and with fewer bugs.
