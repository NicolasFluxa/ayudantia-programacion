"""
-------------------------------------------------------------------------------
                                  EJERCICIO 01
                       Operaciones Aritméticas con Input
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Escribe un programa que realice lo siguiente:
1. Salude al usuario.
2. Solicite al usuario que ingrese un primer número entero.
3. Solicite al usuario que ingrese un segundo número entero.
4. Calcule y muestre:
    a. La suma de los dos números.
    b. La resta del primer número menos el segundo.
    c. La multiplicación de los dos números.
    d. La división del primer número entre el segundo (asegúrate de que sea división real).
5. Utiliza f-strings para mostrar los resultados de forma clara.

## OBJETIVO:
## ---------
Leer datos con `input()`, convertirlos con `int()`, usar los operadores
aritméticos (+, -, *, /) y proteger la división contra el divisor cero.

## ENTRADA:
## --------
Dos números enteros, uno por línea. Ejemplo: 10 y 4.

## SALIDA ESPERADA (ejemplo de ejecución, con 10 y 4):
## ---------------------------------------------------
¡Hola! Bienvenido/a a la calculadora básica.
---------------------------------------------
Por favor, ingresa el primer número entero: 10
Ahora, ingresa el segundo número entero: 4
---------------------------------------------
Números ingresados: 10 y 4
---------------------------------------------
La suma de 10 + 4 es: 14
La resta de 10 - 4 es: 6
La multiplicación de 10 * 4 es: 40
La división de 10 / 4 es: 2.50
---------------------------------------------
¡Cálculos completados!

Si el segundo número es 0, en vez de dividir se muestra un aviso.
-------------------------------------------------------------------------------
"""

# 1. Saludar al usuario
print("¡Hola! Bienvenido/a a la calculadora básica.")
print("---------------------------------------------")

# 2. Solicitar el primer número entero
numero1_str = input("Por favor, ingresa el primer número entero: ")
numero1 = int(numero1_str) # Convertir la entrada a entero

# 3. Solicitar el segundo número entero
numero2_str = input("Ahora, ingresa el segundo número entero: ")
numero2 = int(numero2_str) # Convertir la entrada a entero

print("---------------------------------------------")
print(f"Números ingresados: {numero1} y {numero2}")
print("---------------------------------------------")

# 4. Calcular y mostrar los resultados
# a. Suma
suma = numero1 + numero2
print(f"La suma de {numero1} + {numero2} es: {suma}")

# b. Resta
resta = numero1 - numero2
print(f"La resta de {numero1} - {numero2} es: {resta}")

# c. Multiplicación
multiplicacion = numero1 * numero2
print(f"La multiplicación de {numero1} * {numero2} es: {multiplicacion}")

# d. División
# Dividir entre cero provoca un error (ZeroDivisionError) y el programa se detiene.
# Por eso comprobamos antes que el divisor no sea cero.
# `/` siempre entrega un decimal (10 / 5 da 2.0); `//` sería división entera.
if numero2 != 0:
    division = numero1 / numero2
    print(f"La división de {numero1} / {numero2} es: {division:.2f}") # Mostrando con 2 decimales
else:
    print(f"No se puede dividir {numero1} entre {numero2} (división por cero).")

print("---------------------------------------------")
print("¡Cálculos completados!")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1. ¿Qué hace la función `input()` por defecto con la información que ingresa
   el usuario? ¿Por qué es necesario usar `int()` en este ejercicio?
2. ¿Qué pasaría si el usuario ingresara "hola" o "3.5" cuando se le pide un
   número entero? ¿Cómo reaccionaría el programa?
3. En la parte de la división, se incluyó una verificación `if numero2 != 0:`.
   ¿Por qué es importante esta verificación antes de intentar dividir?
   ¿Qué tipo de error se previene?
-------------------------------------------------------------------------------
"""


"""
-------------------------------------------------------------------------------
## OTRAS FORMAS DE HACERLO (alternativas que producen el mismo resultado)
## ----------------------------------------------------------------------
Las funciones de abajo NO se ejecutan solas. Para probar una, quita el # de la
línea que la llama (al final del archivo) y ejecuta el programa.
-------------------------------------------------------------------------------
"""


def alternativa_1():
    # Calcular dentro del f-string, sin variables intermedias, y pedir los números
    # con int(input(...)) en una sola línea.
    # Conviene: programas cortos. Si vas a usar la suma más adelante, guárdala en una variable.
    print("¡Hola! Bienvenido/a a la calculadora básica.")
    print("---------------------------------------------")
    numero1 = int(input("Por favor, ingresa el primer número entero: "))
    numero2 = int(input("Ahora, ingresa el segundo número entero: "))
    print("---------------------------------------------")
    print(f"Números ingresados: {numero1} y {numero2}")
    print("---------------------------------------------")
    print(f"La suma de {numero1} + {numero2} es: {numero1 + numero2}")
    print(f"La resta de {numero1} - {numero2} es: {numero1 - numero2}")
    print(f"La multiplicación de {numero1} * {numero2} es: {numero1 * numero2}")
    if numero2 != 0:
        print(f"La división de {numero1} / {numero2} es: {numero1 / numero2:.2f}")
    else:
        print(f"No se puede dividir {numero1} entre {numero2} (división por cero).")
    print("---------------------------------------------")
    print("¡Cálculos completados!")


def alternativa_2():
    # Mismo programa con .format() (forma anterior a los f-strings) y con
    # `if numero2 == 0` primero, para dejar el caso especial al comienzo.
    # Conviene: .format() para entenderlo en código antiguo; el `if` invertido,
    # cuando el caso de error es corto y prefieres descartarlo primero.
    print("¡Hola! Bienvenido/a a la calculadora básica.")
    print("---------------------------------------------")
    numero1 = int(input("Por favor, ingresa el primer número entero: "))
    numero2 = int(input("Ahora, ingresa el segundo número entero: "))
    print("---------------------------------------------")
    print("Números ingresados: {} y {}".format(numero1, numero2))
    print("---------------------------------------------")
    print("La suma de {} + {} es: {}".format(numero1, numero2, numero1 + numero2))
    print("La resta de {} - {} es: {}".format(numero1, numero2, numero1 - numero2))
    print("La multiplicación de {} * {} es: {}".format(numero1, numero2, numero1 * numero2))
    if numero2 == 0:
        print("No se puede dividir {} entre {} (división por cero).".format(numero1, numero2))
    else:
        print("La división de {} / {} es: {:.2f}".format(numero1, numero2, numero1 / numero2))
    print("---------------------------------------------")
    print("¡Cálculos completados!")


# alternativa_1()
# alternativa_2()
