"""
-------------------------------------------------------------------------------
                                  EJERCICIO 02
                              Clasificar un Número
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Desarrolla un programa que solicite al usuario ingresar un número entero
y clasifique dicho número como "Positivo", "Negativo" o "Cero".

El programa debe:
1. Pedir al usuario que ingrese un número entero.
2. Utilizar una estructura condicional `if-elif-else` para determinar
   si el número es:
    a. Mayor que cero (Positivo).
    b. Menor que cero (Negativo).
    c. Igual a cero (Cero).
3. Imprimir la clasificación correspondiente.

## OBJETIVO:
## ---------
Elegir entre más de dos caminos con `if-elif-else`.

## ENTRADA:
## --------
Un número entero (positivo, negativo o cero). Ejemplo: -3

## SALIDA ESPERADA (ejemplo de ejecución, con -3):
## -----------------------------------------------
Ingresa un número entero: -3
El número -3 es Negativo.
------------------------------------
-------------------------------------------------------------------------------
"""

# 1. Pedir al usuario un número entero
numero_str = input("Ingresa un número entero: ")
numero = int(numero_str) # Convertir a entero

# 2. Clasificar el número usando if-elif-else.
# Python revisa las condiciones de arriba hacia abajo y ejecuta SOLO la primera que se cumple.
# El else final atrapa todo lo demás: si no es > 0 ni < 0, solo puede ser 0.
if numero > 0:
    # 3a. Imprimir si es positivo
    clasificacion = "Positivo"
elif numero < 0:
    # 3b. Imprimir si es negativo
    clasificacion = "Negativo"
else:
    # 3c. Imprimir si es cero
    clasificacion = "Cero"

# Imprimir el resultado
print(f"El número {numero} es {clasificacion}.")
print("------------------------------------")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1. ¿Cuál es la diferencia fundamental entre usar múltiples `if` separados y usar
   una estructura `if-elif-else`? ¿Cuándo elegirías una sobre la otra?
2. ¿Qué sucedería en este programa si el usuario ingresa un texto como "hola"
   en lugar de un número? (Considera la línea donde se usa `int()`).
   Aunque aún no lo hemos visto en detalle, ¿cómo crees que se podría manejar este tipo de error?
3. Escribe una condición alternativa para verificar si un número es cero sin usar `else`
   directamente para esa condición (podrías usar un `elif numero == 0:` por ejemplo).
   ¿Cambiaría el comportamiento del programa si lo haces así y ajustas el `else` final?
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
    # Tres `if` separados, cada uno con su condición completa.
    # Diferencia: Python revisa los tres siempre, aunque ya haya encontrado la respuesta.
    # Conviene: solo si las condiciones son excluyentes (como aquí). Si no lo son,
    # un `if` separado puede pisar el resultado anterior: ahí corresponde `elif`.
    numero = int(input("Ingresa un número entero: "))
    if numero > 0:
        clasificacion = "Positivo"
    if numero < 0:
        clasificacion = "Negativo"
    if numero == 0:
        clasificacion = "Cero"
    print(f"El número {numero} es {clasificacion}.")
    print("------------------------------------")


def alternativa_2():
    # if-elif-else con la condición `== 0` explícita (pregunta 3 de comprensión)
    # y `else` reservado para un valor imposible.
    # Conviene: cuando quieres que cada caso quede escrito con su condición, para leer
    # el programa sin deducir nada. Es un poco más largo que el original.
    numero = int(input("Ingresa un número entero: "))
    if numero > 0:
        clasificacion = "Positivo"
    elif numero < 0:
        clasificacion = "Negativo"
    elif numero == 0:
        clasificacion = "Cero"
    else:
        clasificacion = "Desconocido"   # nunca ocurre con enteros
    print(f"El número {numero} es {clasificacion}.")
    print("------------------------------------")


def alternativa_3():
    # "if en línea" encadenado: elige el valor en una sola expresión.
    # Conviene: cuando solo quieres calcular un valor. Con más de 3 casos se vuelve
    # difícil de leer: ahí es mejor if-elif-else.
    numero = int(input("Ingresa un número entero: "))
    clasificacion = "Positivo" if numero > 0 else ("Negativo" if numero < 0 else "Cero")
    print(f"El número {numero} es {clasificacion}.")
    print("------------------------------------")


# alternativa_1()
# alternativa_2()
# alternativa_3()
