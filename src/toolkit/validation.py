import re

from .constants import number_mask, mass_units, length_units, temp_units
from .errors import EmptyExpressionError, InvalidOperatorSequenceError, UnknownUnitError, NegativeUnitError, \
    DifferentGroupsError


def calc_validate(tokens: list[str]) -> list[str]:
    if not tokens:
        raise EmptyExpressionError('Пустое выражение')

    length = len(tokens)

    for i in range(length):
        token = tokens[i]

        if token in ('+', '-', '*', '/'):
            if i == 0:
                if token != '-':
                    raise InvalidOperatorSequenceError('Выражение не может начинаться с оператора')
            else:
                prev_token = tokens[i - 1]
                if prev_token in ('+', '-', '*', '/'):
                    if token != '-':
                        raise InvalidOperatorSequenceError('Недопустимая последовательность операторов')

            if i == length - 1:
                raise InvalidOperatorSequenceError('Выражение не может заканчиваться оператором')

            if token == '/':
                next_token = tokens[i + 1]
                if re.match(f'^{number_mask}$', next_token) and float(next_token) == 0:
                    raise ZeroDivisionError('Деление на 0')

        if token == '-':
            is_unary = (i == 0) or (tokens[i - 1] in ('+', '-', '*', '/'))
            if is_unary:
                if i + 1 >= length or not re.match(f'^{number_mask}$', tokens[i + 1]):
                    raise InvalidOperatorSequenceError('Ожидалось число после унарного минуса')

    return tokens


def convert_validate(value: float, unit1: str, unit2: str) -> None:
    all_units = mass_units | length_units | temp_units

    if unit1 not in all_units or unit2 not in all_units:
        raise UnknownUnitError('Неизвестная единица')

    if value < 0 and (unit1 not in temp_units and unit2 not in temp_units):
        raise NegativeUnitError('Единица не предусматривает отрицательного значения')

    same_length = unit1 in length_units and unit2 in length_units
    same_mass = unit1 in mass_units and unit2 in mass_units
    same_temp = unit1 in temp_units and unit2 in temp_units

    if not (same_length or same_mass or same_temp):
        raise DifferentGroupsError(
            f'Конвертация между разными группами запрещена: '
            f"'{unit1}' -> '{unit2}'"
        )

    if same_temp:
        if unit1 == 'c':
            k = value + 273
        elif unit1 == 'f':
            k = (value - 32) * 5 / 9 + 273
        else:
            k = value

        if k < 0:
            raise NegativeUnitError('Температура ниже абсолютного нуля запрещена')
