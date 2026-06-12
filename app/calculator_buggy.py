"""
Buggy version for live demo.

Use this file to show what happens BEFORE QA catches the problem.
You can temporarily copy this code into app/calculator.py during the demo,
or just open this file and explain the bug.
"""

from __future__ import annotations


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    # BUG: division by zero should not return 0.
    # It should raise an error, because 10 / 0 is not a valid operation.
    if b == 0:
        return 0

    return a / b


def calculate(operation: str, a: float, b: float) -> float:
    if operation == "add":
        return add(a, b)

    if operation == "subtract":
        return subtract(a, b)

    if operation == "multiply":
        return multiply(a, b)

    if operation == "divide":
        return divide(a, b)

    raise ValueError(f"Unsupported operation: {operation}")
