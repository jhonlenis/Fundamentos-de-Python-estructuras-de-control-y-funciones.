kilometers = 12.25
miles = 7.38

# Lógica de conversión:
# 1 milla = 1.61 kilómetros
# Para pasar de Millas a KM: multiplicamos por 1.61
# Para pasar de KM a Millas: dividimos por 1.61

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")