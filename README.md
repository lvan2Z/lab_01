Лабораторная работа по программированию на языке Python №1

Пакет toolkit: калькулятор (calculator.py) и конвертер (converter.py).

# Как пользоваться?

Через CLI:

python -m src.toolkit calc "2 + 3 * 4"     # 14.0
python -m src.toolkit convert 1 --from km --to m   # 1000.0
python -m src.toolkit --help

Файлы
src/toolkit/calculator.py — tokenize, validate, calculate
src/toolkit/converter.py — convert
src/toolkit/constants.py — константы и маски
src/toolkit/validation.py — валидация
src/toolkit/errors.py — ошибки
src/toolkit/__main__.py — CLI
tests/tests.py — тесты

Калькулятор
Числа целые и дробные, операторы: + - * /
Унарный плюс/минус перед числом (-5 + 10 == 5)
Пробелы не важны

Конвертер
Длина: mm cm m km, масса: g kg, температура: c f k
Регистр не важен (KM = km)

Проверки
pytest tests.py::TestConverter
pytest tests.py::TestCalculator

