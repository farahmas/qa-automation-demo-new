# Code Review Demo

This file contains example review comments for the demo project.

## What is code review?

Code review means another developer or QA engineer checks the code before it is merged into the main branch.

The goal is not to criticize the person.
The goal is to improve quality, readability, security, and maintainability.

---

## Example review comments

### 1. Naming issue

**File:** `app/bad_code_for_static_analysis.py`

```python
def BadFunctionName(x, y):
```

**Review comment:**

Function names in Python should use `snake_case`, for example:

```python
def add_numbers(x, y):
```

Clear naming makes the code easier to read and understand.

---

### 2. Duplicated code

**File:** `app/bad_code_for_static_analysis.py`

```python
def duplicated_logic_1(price):
    ...

def duplicated_logic_2(price):
    ...
```

**Review comment:**

These two functions contain the same discount logic.
Duplicated code is risky because if we change the discount rule later, we may forget to update both places.

Suggested improvement:

```python
def apply_discount(price):
    if price > 100:
        return price - price * 0.10
    return price
```

---

### 3. Missing test

**File:** `tests/test_calculator.py`

**Review comment:**

We test normal division, but we also need to test division by zero.

Missing edge-case tests are dangerous because bugs often happen in unusual situations.

Good test:

```python
def test_divide_by_zero_should_raise_error():
    with pytest.raises(ValueError):
        divide(10, 0)
```

---

### 4. Possible bug

**File:** `app/calculator_buggy.py`

```python
if b == 0:
    return 0
```

**Review comment:**

This is a possible bug.
Division by zero is not a valid mathematical operation.
Returning `0` hides the problem and can produce wrong business results.

Better behavior:

```python
if b == 0:
    raise ValueError("Cannot divide by zero")
```

---

### 5. Security or quality concern

**File:** `app/bad_code_for_static_analysis.py`

```python
import os
import sys
```

**Review comment:**

These imports are unused.
Unused imports make code messy and sometimes show that old logic was removed incorrectly.

In real projects, we also check for:
- hardcoded passwords
- unsafe user input handling
- missing validation
- unnecessary dependencies
- weak error handling

---

## How code review improves quality

Code review helps teams:

1. Find bugs before users see them.
2. Make code easier to read.
3. Share knowledge between team members.
4. Improve test coverage.
5. Reduce security and quality risks.
6. Keep the project consistent.

Code review is a human quality gate.
Static analysis and tests are automated quality gates.
Together, they make the project safer.
