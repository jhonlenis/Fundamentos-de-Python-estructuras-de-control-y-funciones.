# Seccion 3
# laboratorio 1 "Ejercicios de Operadores, Matematicos."
comando: 
# Comprobación de los 15 ejercicios de operadores
print("--- RESULTADOS DE LOS EJERCICIOS ---")

print("Ejercicio 1 (5 + 3 * 2):", 5 + 3 * 2)
print("Ejercicio 2 (8 / 2 + 4 * 3):", 8 / 2 + 4 * 3)
print("Ejercicio 3 ((7 + 3) * 2 - 5):", (7 + 3) * 2 - 5)
print("Ejercicio 4 (10 - 4 + 2 * 3):", 10 - 4 + 2 * 3)
print("Ejercicio 5 ((10 / 2) * (3 + 2) - 4):", (10 / 2) * (3 + 2) - 4)
print("Ejercicio 6 (2 + 3 * (4 - 1)):", 2 + 3 * (4 - 1))
print("Ejercicio 7 (5 * 2 ** 3):", 5 * 2 ** 3)
print("Ejercicio 8 (6 + 4 / 2 ** 2):", 6 + 4 / 2 ** 2)
print("Ejercicio 9 (10 % 3 + 2 * 5):", 10 % 3 + 2 * 5)
print("Ejercicio 10 ((8 + 2) * 3 ** 2):", (8 + 2) * 3 ** 2)
print("Ejercicio 11 (7 + 2 * (3 + 5) / 4):", 7 + 2 * (3 + 5) / 4)
print("Ejercicio 12 (2 ** 3 * 4 / 2):", 2 ** 3 * 4 / 2)
print("Ejercicio 13 (9 - 6 + 3 ** 2):", 9 - 6 + 3 ** 2)
print("Ejercicio 14 ((7 - 2) * 5 + 3 ** 2):", (7 - 2) * 5 + 3 ** 2)
print("Ejercicio 15 (4 * 2 ** 3 / 8 + 1):", 4 * 2 ** 3 / 8 + 1)
Estructura
- `src/`: Lógica principal del proyecto.
- `Seccion 1/` a `Seccion 3/`: Laboratorios y ejercicios prácticos.

Respuesta a la Pregunta de Lógica: Jerarquía de Operadores
Python evalúa las expresiones matemáticas siguiendo el orden de prioridad **PEMDAS**:
1. **P**aréntesis `()`
2. **E**xponentes `**` (Se resuelven de derecha a izquierda si hay varios seguidos).
3. **M**ultiplicación, **D**ivisión, **A**ritmética de módulo y división entera `*`, `/`, `%`, `//`.
4. **A**dición (Suma) y **S**ustracción (Resta) `+`, `-`.