"""
Unit tests for calculator business logic.

These tests are small, fast, and easy to understand.
That is exactly what we want in a beginner-friendly QA demo.
"""

import pytest

from app.calculator import add, calculate, divide, multiply, subtract


def test_add_two_numbers():
    assert add(2, 3) == 5


def test_subtract_two_numbers():
    assert subtract(10, 4) == 6


def test_multiply_two_numbers():
    assert multiply(6, 7) == 42


def test_divide_two_numbers():
    assert divide(10, 2) == 5


def test_divide_by_zero_should_raise_error():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)


def test_calculate_unknown_operation_should_raise_error():
    with pytest.raises(ValueError, match="Unsupported operation"):
        calculate("power", 2, 3)
