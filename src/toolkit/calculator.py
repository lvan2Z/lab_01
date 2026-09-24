import re

from .constants import number_mask
from .tokenization import tokenize
from .validation import calc_validate


def calc(expression: str) -> float:
    tokens = calc_validate(tokenize(expression))

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