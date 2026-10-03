"""
-------------------------------------------------------------------------------
                                  EJERCICIO 01
                       Funciones Simples y con Parámetros
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Este ejercicio te enseñará a definir y llamar funciones básicas, algunas de
ellas con parámetros.

1.  Define una función llamada `mostrar_saludo_simple()`:
    a. Esta función no debe recibir parámetros.
    b. Dentro de la función, simplemente imprime el mensaje "¡Hola, mundo desde una función!".
    c. Llama (ejecuta) esta función una vez.

2.  Define una función llamada `saludar_usuario(nombre_usuario)`:
    a. Esta función debe recibir un parámetro llamado `nombre_usuario`.
    b. Dentro de la función, imprime un saludo personalizado, por ejemplo:
       "¡Hola, [nombre_usuario]! Bienvenido/a."
    c. Solicita al usuario que ingrese su nombre usando `input()`.
    d. Llama a la función `saludar_usuario()` pasándole el nombre ingresado.

3.  Define una función llamada `sumar_tres_numeros(num1, num2, num3)`:
    a. Esta función debe recibir tres parámetros numéricos.
    b. Dentro de la función, calcula la suma de los tres números.
    c. Imprime el resultado de la suma desde dentro de la función.
    d. Incluye un docstring explicando brevemente qué hace la función.
    e. Llama a esta función con tres números de ejemplo (ej: 5, 10, 2).

## OBJETIVO:
## ---------
Aprender a definir (`def`) y llamar funciones, pasarles parámetros y
documentarlas con un docstring. En este ejercicio las funciones IMPRIMEN
el resultado; en el siguiente (funciones_con_retorno.py) lo DEVUELVEN con `return`.

## ENTRADA:
## --------
Un nombre (texto). Ejemplo: Pedro

## SALIDA ESPERADA (ejemplo de ejecución, con "Pedro"):
## ----------------------------------------------------
--- Llamando a mostrar_saludo_simple ---
¡Hola, mundo desde una función!
------------------------------------

--- Llamando a saludar_usuario ---
Por favor, ingresa tu nombre: Pedro
¡Hola, Pedro! Bienvenido/a.
¡Hola, Ana! Bienvenido/a.
------------------------------------

--- Llamando a sumar_tres_numeros ---
La suma de 5 + 10 + 2 es: 17
La suma de 100 + -50 + 25.5 es: 75.5
------------------------------------
-------------------------------------------------------------------------------
"""

# 1. Función de saludo simple
# `def` define la función, pero NO la ejecuta: el código de adentro (con sangría)
# solo corre cuando la llamamos escribiendo su nombre con paréntesis.
def mostrar_saludo_simple():
    """Imprime un saludo genérico."""
    print("¡Hola, mundo desde una función!")

print("--- Llamando a mostrar_saludo_simple ---")
mostrar_saludo_simple()  # Llamada a la función: aquí recién se ejecuta
print("------------------------------------")

# 2. Función de saludo con parámetro
def saludar_usuario(nombre_usuario):
    """Imprime un saludo personalizado usando el nombre proporcionado."""
    print(f"¡Hola, {nombre_usuario}! Bienvenido/a.")

print("\n--- Llamando a saludar_usuario ---")
nombre_ingresado = input("Por favor, ingresa tu nombre: ")
saludar_usuario(nombre_ingresado) # Llamada con el argumento del input
saludar_usuario("Ana") # Otra llamada con un argumento directo
print("------------------------------------")

# 3. Función para sumar tres números
def sumar_tres_numeros(num1, num2, num3):
    """
    Calcula la suma de tres números y muestra el resultado.

    Args:
        num1 (int or float): El primer número.
        num2 (int or float): El segundo número.
        num3 (int or float): El tercer número.
    """
    suma = num1 + num2 + num3
    print(f"La suma de {num1} + {num2} + {num3} es: {suma}")

print("\n--- Llamando a sumar_tres_numeros ---")
sumar_tres_numeros(5, 10, 2)
sumar_tres_numeros(100, -50, 25.5)
print("------------------------------------")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  ¿Cuál es la palabra clave utilizada en Python para definir una función?
2.  ¿Qué es un "parámetro" de una función? ¿Qué es un "argumento"?
    Usa el ejemplo de `saludar_usuario` para explicar.
3.  ¿Qué es un "docstring"? ¿Para qué sirve y cómo se define en una función?
4.  Si una función se define pero nunca se "llama", ¿se ejecutará el código
    dentro de ella? ¿Por qué?
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
    # Funciones que DEVUELVEN el resultado con `return` en vez de imprimirlo.
    # Quien llama a la función decide qué hacer con el valor: imprimirlo, guardarlo
    # o usarlo en otro cálculo.
    # Conviene: casi siempre, porque la función queda reutilizable. Una función que
    # solo imprime no sirve si luego quieres usar el resultado (ver funciones_con_retorno.py).
    def saludo_simple():
        return "¡Hola, mundo desde una función!"

    def saludo_usuario(nombre_usuario):
        return f"¡Hola, {nombre_usuario}! Bienvenido/a."

    def sumar_tres_numeros(num1, num2, num3):
        """Calcula y devuelve la suma de tres números."""
        return num1 + num2 + num3

    print("--- Llamando a mostrar_saludo_simple ---")
    print(saludo_simple())
    print("------------------------------------")

    print("\n--- Llamando a saludar_usuario ---")
    nombre_ingresado = input("Por favor, ingresa tu nombre: ")
    print(saludo_usuario(nombre_ingresado))
    print(saludo_usuario("Ana"))
    print("------------------------------------")

    print("\n--- Llamando a sumar_tres_numeros ---")
    print(f"La suma de 5 + 10 + 2 es: {sumar_tres_numeros(5, 10, 2)}")
    print(f"La suma de 100 + -50 + 25.5 es: {sumar_tres_numeros(100, -50, 25.5)}")
    print("------------------------------------")


def alternativa_2():
    # Mismas funciones, pero con concatenación (+) para el saludo y sum() para sumar.
    #   "¡Hola, " + nombre + "!"  -> pega textos (el nombre debe ser texto).
    #   sum([a, b, c])            -> suma los elementos de una lista.
    # Conviene: concatenar si lo que unes ya es texto; sum() cuando la cantidad de
    # números puede cambiar (ver *args en la Semana 9). En general, f-string.
    def mostrar_saludo_simple():
        print("¡Hola, mundo desde una función!")

    def saludar_usuario(nombre_usuario):
        print("¡Hola, " + nombre_usuario + "! Bienvenido/a.")

    def sumar_tres_numeros(num1, num2, num3):
        suma = sum([num1, num2, num3])
        print(f"La suma de {num1} + {num2} + {num3} es: {suma}")

    print("--- Llamando a mostrar_saludo_simple ---")
    mostrar_saludo_simple()
    print("------------------------------------")

    print("\n--- Llamando a saludar_usuario ---")
    nombre_ingresado = input("Por favor, ingresa tu nombre: ")
    saludar_usuario(nombre_ingresado)
    saludar_usuario("Ana")
    print("------------------------------------")

    print("\n--- Llamando a sumar_tres_numeros ---")
    sumar_tres_numeros(5, 10, 2)
    sumar_tres_numeros(100, -50, 25.5)
    print("------------------------------------")


# alternativa_1()
# alternativa_2()
