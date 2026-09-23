import re
from .constants import number_mask, operator_mask


def tokenize(expression: str) -> list:
    tokens = re.findall(f'({number_mask}|{operator_mask})', expression)
    return tokens


def calc(tokens: str):
    parsed = []

    for token in tokens:
        if re.match(f'^{number_mask}$', token):
            parsed.append(float(token))
        else:
            parsed.append(token)

    i = 0
    while i < len(parsed):
        if parsed[i] in ('*', '/'):
            if parsed[i + 1] == 0 and parsed[i] == '/':
                raise ValueError('Деление на 0')
            else:
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
