import pytest
from toolkit.calculator import calc
from .errors import EmptyExpressionError, UnknownSymbolError, InvalidOperatorSequenceError


def test_addition():
    assert calc("2 + 3") == 5.0


def test_subtraction():
    assert calc("10 - 4") == 6.0


def test_multiplication():
    assert calc("6 * 7") == 42.0


def test_division():
    assert calc("8 / 2") == 4.0


def test_float_numbers():
    assert calc("2.5 + 1.5") == 4.0


def test_spaces_are_ignored():
    assert calc("  5   +   3  ") == 8.0


def test_operator_priority():
    assert calc("2 + 3 * 4") == 14.0


def test_operator_priority_with_division():
    assert calc("20 - 8 / 2") == 16.0


def test_negative_number_at_start():
    assert calc("-5 + 10") == 5.0


def test_negative_number_after_operator():
    assert calc("10 * -2") == -20.0


def test_complex_expression():
    assert calc("10 + 2 * 3 - 8 / 4") == 14.0



def test_empty_expression():
    with pytest.raises(EmptyExpressionError):
        calc("")


def test_unknown_symbol():
    with pytest.raises(UnknownSymbolError):
        calc("2 @ 3")


def test_missing_operator_between_numbers():
    with pytest.raises(InvalidOperatorSequenceError):
        calc("2 3")


def test_two_binary_operators():
    with pytest.raises(InvalidOperatorSequenceError):
        calc("2 + * 3")


def test_expression_ends_with_operator():
    with pytest.raises(InvalidOperatorSequenceError):
        calc("5 +")


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        calc("10 / 0")


def test_unary_minus_without_number():
    with pytest.raises(InvalidOperatorSequenceError):
        calc("-")


def test_invalid_unary_minus_position():
    with pytest.raises(InvalidOperatorSequenceError):
        calc("5 * -")
