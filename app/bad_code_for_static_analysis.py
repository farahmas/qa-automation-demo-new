"""
This file is intentionally bad.

Use it to demonstrate Static Code Analysis.
Ruff will find problems here.

To make the project pass CI after the demo, either:
1. fix this file, or
2. exclude it in pyproject.toml, or
3. delete it.
"""

import os
import sys


def BadFunctionName(x, y):
    unused_variable = 123
    result=x+y
    return result


def duplicated_logic_1(price):
    if price > 100:
        discount = price * 0.10
        return price - discount
    return price


def duplicated_logic_2(price):
    if price > 100:
        discount = price * 0.10
        return price - discount
    return price
