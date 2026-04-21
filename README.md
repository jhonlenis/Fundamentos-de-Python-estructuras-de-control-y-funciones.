# Fundamentos-de-Python-estructuras-de-control-y-funciones.

# Seccion 1 

# Laboratorio 1 "Hola Mundo"
Comando: print("¡Hola, Mundo!")
Uso de comillas simples y dobles:
Se verificó que print("Texto") y print('Texto') tienen el mismo comportamiento. En Python no hay diferencia funcional entre ambas formas.
Texto sin comillas:
Al ejecutar print(jhon), el programa genera un NameError. Esto ocurre porque, al no usar comillas, Python interpreta Samuel como una variable que no ha sido declarada previamente.
Ausencia de paréntesis:
Cuando se escribe print "Hola", aparece un SyntaxError. En Python 3 es obligatorio usar paréntesis, ya que print es una función y no una instrucción como lo era en versiones antiguas.
Diferencia entre mayúsculas y minúsculas:
Al usar Print() en lugar de print(), se produce un NameError. Esto confirma que Python distingue entre mayúsculas y minúsculas (es case-sensitive).

# Laboratorio 2 "a función print() y sus argumentos"
comando: Programming***Essentials***in...Python
print: es una funcion para mostrar el texto en pantalla 
"Programming", "Essentials", "in": Son cadenas de texto (strings).
Puedes poner varias separadas por comas, y print() las une.
sep="***": sep = separador
Indica qué se coloca entre cada palabra.
Por defecto es un espacio " ".
end="...": end = final de la línea
Define qué se imprime al final.
Por defecto es un salto de línea (\n), o sea, baja a la siguiente línea.

# Laboratio 3 "Dando formato a la salida"
comando:# 1. Minimizar print() usando \n
print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****")

print("-" * 30)  # Separador

2. Flecha doble de tamaño (manteniendo proporciones)
print("        *")
print("       * *")
print("      *   *")
print("     *     *")
print("    *       *")
print("   *         *")
print("  *           *")
print(" *             *")
print("*****       *****")
print("    *       *")
print("    *       *")
print("    *       *")
print("    *       *")
print("    *********")

print("-" * 30)  # Separador

3. Duplicar la flecha una al lado de la otra
print("\nUsando multiplicacion de strings:")
espacio = " " * 2
print(("    *" + espacio) * 2)
print(("   * *" + espacio) * 2)
print(("  *   *" + espacio) * 2)
print((" *     *" + espacio) * 2)
print(("***   ***" + espacio) * 2)
print(("  *   *" + espacio) * 2)
print(("  *   *" + espacio) * 2)
print(("  *****" + espacio) * 2)

print("-" * 30)  # Separador

4. Uso de apóstrofes en lugar de comillas
print('    *')
print('   * *')
print('  *   *')
print(' *     *')
print('***   ***')
print('  *   *')
print('  *   *')
print('  *****')
El problema es:
Escribiste Print con mayúscula
En Python las funciones son sensibles a mayúsculas y minúsculas Por eso el error:
NameError: name 'Print' is not defined
Significa: Python no reconoce esa función.
"texto" * 2 significa:
repetir el texto 2 veces
Cada print() dibuja una línea y va formando la figura de flechas lado a lado.
\n → salto de línea
"-"*30 → imprime 30 guiones Sirve para dividir las dos partes del programa.
\n para hacer saltos de línea dentro de un solo print
Primera parte → flechas duplicadas usando repetición (* 2)
Segunda parte → una sola flecha usando \n