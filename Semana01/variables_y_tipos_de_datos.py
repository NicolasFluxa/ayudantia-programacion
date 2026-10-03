"""
-------------------------------------------------------------------------------
                                  EJERCICIO 02
                           Variables y Tipos de Datos
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Crea un programa que declare variables para almacenar los siguientes datos:
1. Tu edad (como un número entero).
2. Tu estatura en metros (como un número decimal).
3. Tu comida favorita (como texto).
4. Si te gusta programar (como un valor booleano: verdadero o falso).

Luego, imprime cada una de estas variables con un mensaje descriptivo
y también imprime el tipo de dato de cada variable usando la función `type()`.

## OBJETIVO:
## ---------
Distinguir los cuatro tipos de datos básicos: int, float, str y bool.

## ENTRADA:
## --------
Ninguna: los valores se escriben directamente en el código.

## SALIDA ESPERADA (primeras líneas de la ejecución):
## --------------------------------------------------
--- Información Personal ---
Mi edad es: 25
El tipo de dato de mi_edad es: <class 'int'>
--------------------------
Mi estatura es: 1.75 metros.
El tipo de dato de mi_estatura es: <class 'float'>
--------------------------
(... y lo mismo para el texto, con <class 'str'>, y el booleano, con <class 'bool'>)
-------------------------------------------------------------------------------
"""

# Declaración de variables
mi_edad = 25  # Tipo entero (int): números sin decimales
mi_estatura = 1.75  # Tipo decimal (float): se escribe con punto, no con coma
mi_comida_favorita = "Pizza"  # Tipo texto (str, de "string"): va entre comillas
me_gusta_programar = True  # Tipo booleano (bool): solo True o False, con mayúscula inicial

# Imprimir las variables y sus tipos
print("--- Información Personal ---")

# Edad
print("Mi edad es:", mi_edad)
print("El tipo de dato de mi_edad es:", type(mi_edad))
print("--------------------------")

# Estatura
print("Mi estatura es:", mi_estatura, "metros.")
print("El tipo de dato de mi_estatura es:", type(mi_estatura))
print("--------------------------")

# Comida Favorita
print("Mi comida favorita es:", mi_comida_favorita)
print("El tipo de dato de mi_comida_favorita es:", type(mi_comida_favorita))
print("--------------------------")

# Gusto por la programación
print("¿Me gusta programar?:", me_gusta_programar)
print("El tipo de dato de me_gusta_programar es:", type(me_gusta_programar))
print("--------------------------")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1. ¿Cuáles son los cuatro tipos de datos básicos que utilizaste en este ejercicio?
   Describe brevemente cada uno.
2. Si intentaras sumar la variable `mi_edad` con `mi_comida_favorita`,
   ¿qué crees que pasaría? Pruébalo y explica el resultado.
3. ¿Cómo se representa un valor Falso en un tipo de dato booleano en Python?
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
    # f-string en lugar de la coma: el texto y la variable van en un solo bloque.
    # Conviene: cuando quieres controlar el formato exacto del mensaje.
    mi_edad = 25
    mi_estatura = 1.75
    mi_comida_favorita = "Pizza"
    me_gusta_programar = True

    print("--- Información Personal ---")
    print(f"Mi edad es: {mi_edad}")
    print(f"El tipo de dato de mi_edad es: {type(mi_edad)}")
    print("--------------------------")
    print(f"Mi estatura es: {mi_estatura} metros.")
    print(f"El tipo de dato de mi_estatura es: {type(mi_estatura)}")
    print("--------------------------")
    print(f"Mi comida favorita es: {mi_comida_favorita}")
    print(f"El tipo de dato de mi_comida_favorita es: {type(mi_comida_favorita)}")
    print("--------------------------")
    print(f"¿Me gusta programar?: {me_gusta_programar}")
    print(f"El tipo de dato de me_gusta_programar es: {type(me_gusta_programar)}")
    print("--------------------------")


def alternativa_2():
    # Novedad (adelanto de las clases de listas y de for): una lista de datos
    # y un `for` que repite el mismo bloque de prints para cada uno.
    # Conviene: cuando son muchos datos y no quieres copiar y pegar el mismo print.
    mi_edad = 25
    mi_estatura = 1.75
    mi_comida_favorita = "Pizza"
    me_gusta_programar = True

    datos = [
        ("Mi edad es:", "mi_edad", mi_edad, ""),
        ("Mi estatura es:", "mi_estatura", mi_estatura, " metros."),
        ("Mi comida favorita es:", "mi_comida_favorita", mi_comida_favorita, ""),
        ("¿Me gusta programar?:", "me_gusta_programar", me_gusta_programar, ""),
    ]
    print("--- Información Personal ---")
    for descripcion, nombre, valor, sufijo in datos:
        print(f"{descripcion} {valor}{sufijo}")
        print("El tipo de dato de", nombre, "es:", type(valor))
        print("--------------------------")


# alternativa_1()
# alternativa_2()
