length_units = {"mm", "cm", "m", "km"}
mass_units = {"g", "kg"}
temp_units = {"c", "f", "k"}

length_to_m = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1.0,
    "km": 1000.0,
}

mass_to_g = {
    "g": 1.0,
    "kg": 1000.0,
}
number_mask = '(?:[1-9]+[0-9]*|0)'
operator_mask = '[+*/-]'
