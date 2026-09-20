from constants import length_units, mass_units, temp_units, length_to_m, mass_to_g


def convert(value: float, unit1: str, unit2: str) -> float:
    unit1 = unit1.lower().strip()
    unit2 = unit2.lower().strip()

    if unit1 in length_units and unit2 in length_units:

        meters = value * length_to_m[unit1]
        result = meters / length_to_m[unit2]
        return float(result)

    elif unit1 in mass_units and unit2 in mass_units:

        grams = value * mass_to_g[unit1]
        result = grams / mass_to_g[unit2]
        return float(result)

    elif unit1 in temp_units and unit2 in temp_units:
        if unit1 == 'c':
            k = value + 273
        elif unit1 == 'f':
            k = (value - 32) * 5 / 9 + 273
        else:
            k = value

        if k < 0:
            raise ValueError('Температура ниже абсолютного нуля запрещена')

        if unit2 == 'c':
            result = k - 273
        elif unit2 == 'f':
            result = (k - 273) * 9 / 5 + 32
        else:
            result = k

        return float(result)

    else:
        raise ValueError(
            f'Конвертация между разными группами запрещена: '
            f"'{unit1}' -> '{unit2}'"
        )
