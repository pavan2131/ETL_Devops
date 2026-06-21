import sys
import os
import pytest

# Add src to the path so tests can import math_ops
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from math_ops import add, subtract  # noqa: E402


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0.1, 0.2) == pytest.approx(0.3)


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(1, 5) == -4
