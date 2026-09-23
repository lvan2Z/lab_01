import re

from .constants import number_mask, operator_mask
from .errors import *


def tokenize(expression: str) -> list[str]:
    if re.findall(f'{number_mask}( )+{number_mask}', expression):
        raise InvalidOperatorSequenceError('Пропущен оператор между числами')

    no_space_expression = re.sub(r'\s+', '', expression)
    tokens = re.findall(f'({number_mask}|{operator_mask})', no_space_expression)

    if ''.join(tokens) != no_space_expression:
        raise UnknownSymbolError('Недопустимый символ в выражении')
    return tokens


def validate(tokens: list[str]) -> list[str]:
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
                if (re.match(f'{number_mask}', next_token)) and float(next_token) == 0:
                    raise ZeroDivisionError('Деление на 0')

        if token == '-':
            is_unary = (i == 0) or (tokens[i - 1] in ('+', '-', '*', '/'))
            if is_unary:
                if i + 1 >= length or not (re.match(f'^{number_mask}', tokens[i + 1])):
                    raise InvalidOperatorSequenceError('Ожидалось число после унарного минуса')

    return tokens


def calc(expression: str) -> float:
    raw_tokens = tokenize(expression)
    tokens = validate(raw_tokens)

    parsed = []
    i = 0
    length = len(tokens)
    while i < length:
        token = tokens[i]
        if token == '-':
            is_unary = (i == 0) or (tokens[i - 1] in ('+', '-', '*', '/'))
            if is_unary:
                parsed.append(-float(tokens[i + 1]))
                i += 2
                continue

        if re.match(f'^{number_mask}$', token):
            parsed.append(float(token))
        else:
            parsed.append(token)
        i += 1

    i = 0
    while i < len(parsed):
        if parsed[i] in ('*', '/'):
            res = parsed[i - 1] * parsed[i + 1] if parsed[i] == '*' else parsed[i - 1] / parsed[i + 1]
            parsed[i - 1:i + 2] = [res]
            i -= 1
        i += 1

    i = 0
    while i < len(parsed):
        if parsed[i] in ('+', '-'):
            res = parsed[i - 1] + parsed[i + 1] if parsed[i] == '+' else parsed[i - 1] - parsed[i + 1]
            parsed[i - 1: i + 2] = [res]
            i -= 1
        i += 1

    return parsed[0]