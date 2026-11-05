"""Regression tests for warehouse.quantity.parse_quantity."""
import pytest

from warehouse.quantity import parse_quantity


def test_positive_integer():
    assert parse_quantity("5") == 5


def test_positive_integer_with_whitespace():
    assert parse_quantity("  10  ") == 10


def test_zero_is_accepted():
    """Zero is a valid quantity (e.g. fully-picked line)."""
    assert parse_quantity("0") == 0


def test_negative_raises_value_error():
    """Negative quantities must be rejected."""
    with pytest.raises(ValueError, match="non-negative"):
        parse_quantity("-1")


def test_negative_large_raises_value_error():
    with pytest.raises(ValueError, match="non-negative"):
        parse_quantity("-100")


def test_non_numeric_raises():
    with pytest.raises(ValueError):
        parse_quantity("abc")
