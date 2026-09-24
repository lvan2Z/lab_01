import pytest

from src.toolkit.calculator import calc
from src.toolkit.converter import convert
from src.toolkit.errors import (
    EmptyExpressionError,
    InvalidOperatorSequenceError,
    UnknownUnitError,
    NegativeUnitError,
    DifferentGroupsError, UnknownSymbolError
)


class TestCalculator:
    def test_simple_addition(self):
        assert calc("2 + 3") == 5.0

    def test_simple_subtraction(self):
        assert calc("10 - 4") == 6.0

    def test_simple_multiplication(self):
        assert calc("3 * 5") == 15.0

    def test_simple_division(self):
        assert calc("20 / 4") == 5.0

    def test_operator_priority(self):
        assert calc("2 + 3 * 4") == 14.0

    def test_complex_expression(self):
        assert calc("10 + 20 * 3 - 5 / 5") == 69.0

    def test_decimal_numbers(self):
        assert calc("1.5 + 2.5") == 4.0

    def test_spaces_between_tokens(self):
        assert calc("  2  +  3  ") == 5.0

    def test_unary_minus_at_start(self):
        assert calc("-5 + 10") == 5.0

    def test_unary_minus_after_operator(self):
        assert calc("10 + -5") == 5.0

    def test_multiple_unary_minus(self):
        assert calc("-5 + -3") == -8.0

    def test_empty_expression(self):
        with pytest.raises(EmptyExpressionError):
            calc("")

    def test_invalid_character(self):
        with pytest.raises(UnknownSymbolError):
            calc("2 + a")

    def test_missing_operand(self):
        with pytest.raises(InvalidOperatorSequenceError):
            calc("2 3")

    def test_two_binary_operators(self):
        with pytest.raises(InvalidOperatorSequenceError):
            calc("2 + * 3")

    def test_division_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            calc("10 / 0")

    def test_expression_ends_with_operator(self):
        with pytest.raises(InvalidOperatorSequenceError):
            calc("2 + 3 *")


class TestConverter:
    def test_meters_to_kilometers(self):
        assert convert(1000, "m", "km") == 1.0

    def test_centimeters_to_meters(self):
        assert convert(100, "cm", "m") == 1.0

    def test_millimeters_to_centimeters(self):
        assert convert(10, "mm", "cm") == 1.0

    def test_grams_to_kilograms(self):
        assert convert(1000, "g", "kg") == 1.0

    def test_kilograms_to_grams(self):
        assert convert(1, "kg", "g") == 1000.0

    def test_celsius_to_kelvin(self):
        assert convert(0, "c", "k") == 273.0

    def test_celsius_to_fahrenheit(self):
        assert convert(100, "c", "f") == 212.0

    def test_fahrenheit_to_celsius(self):
        assert convert(32, "f", "c") == 0.0

    def test_case_insensitive_units(self):
        assert convert(100, "CM", "M") == 1.0

    def test_unknown_unit(self):
        with pytest.raises(UnknownUnitError):
            convert(100, "m", "xyz")

    def test_different_groups(self):
        with pytest.raises(DifferentGroupsError):
            convert(100, "m", "kg")

    def test_negative_length(self):
        with pytest.raises(NegativeUnitError):
            convert(-10, "m", "km")

    def test_temperature_below_absolute_zero(self):
        with pytest.raises(NegativeUnitError):
            convert(-300, "c", "k")
