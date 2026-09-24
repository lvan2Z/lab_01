import re

from .constants import number_mask, operator_mask
from .errors import InvalidOperatorSequenceError, UnknownSymbolError


def tokenize(expression: str) -> list[str]:
    if re.findall(f'{number_mask}( )+{number_mask}', expression):
        raise InvalidOperatorSequenceError('Пропущен оператор между числами')

    no_space_expression = re.sub(r'\s+', '', expression)
    tokens = re.findall(f'({number_mask}|{operator_mask})', no_space_expression)

    if ''.join(tokens) != no_space_expression:
        raise UnknownSymbolError('Недопустимый символ в выражении')
    return tokens
