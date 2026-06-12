"""
Business logic for a very small calculator app.

This file is intentionally simple so students can understand:
- where the application logic lives
- how unit tests check this logic
- how static analysis checks code quality
"""

from __future__ import annotations


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    """Divide two numbers.

    QA note:
    A previous version returned 0 when b == 0.
    That was a hidden bug because division by zero should not be silently ignored.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")

    return a / b


def calculate(operation: str, a: float, b: float) -> float:
    """Run a calculator operation by name."""
    if operation == "add":
        return add(a, b)

    if operation == "subtract":
        return subtract(a, b)

    if operation == "multiply":
        return multiply(a, b)

    if operation == "divide":
        return divide(a, b)

    raise ValueError(f"Unsupported operation: {operation}")
