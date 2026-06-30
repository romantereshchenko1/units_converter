# tests/conftest.py
import pytest
import unitsconverter
import math

NUMERIC = (int, float)

def is_numeric(v):
    return isinstance(v, NUMERIC)

@pytest.fixture(scope="module")
def units():
    """Повертає копію структури UNITS для використання у тестах."""
    return unitsconverter.UNITS