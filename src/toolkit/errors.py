class CalculatorError(Exception):
    pass


class EmptyExpressionError(CalculatorError):
    pass


class UnknownSymbolError(CalculatorError):
    pass


class InvalidOperatorSequenceError(CalculatorError):
    pass

class ConvertError(Exception):
    pass