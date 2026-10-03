"""
-------------------------------------------------------------------------------
                                  EJERCICIO 01
                        Saludo y Presentación en Python
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Escribe un programa en Python que realice lo siguiente:
1. Muestre un mensaje de bienvenida al usuario.
2. Imprima tu nombre completo en la consola.
3. Imprima el nombre de esta asignatura y tu sección (si aplica).

## OBJETIVO:
## ---------
Practicar `print()`, los comentarios (#) y guardar texto en variables.

## ENTRADA:
## --------
Ninguna: el programa no pide datos, solo muestra información.

## SALIDA ESPERADA (ejemplo de ejecución):
## ---------------------------------------
¡Bienvenido/a al mundo de Python!
------------------------------------
Mi nombre es: Ana Pérez
Asignatura: Ayudantía de Programación
Sección: Sección 1
------------------------------------
¡Espero que disfrutes aprendiendo Python!
-------------------------------------------------------------------------------
"""

# Mensaje de bienvenida
print("¡Bienvenido/a al mundo de Python!")
print("------------------------------------") # Un separador para mejorar la lectura

# Imprimir tu nombre completo.
# Guardamos el texto en una variable; reemplaza "Ana Pérez" por tu nombre real.
nombre_completo = "Ana Pérez"  # Texto de ejemplo: pon el tuyo
# print() separa con un espacio cada cosa que le pasas separada por coma.
print("Mi nombre es:", nombre_completo)

# Imprimir nombre de la asignatura y sección
# Personaliza estos valores según corresponda (si no tienes sección, déjalo así).
asignatura = "Ayudantía de Programación"
seccion = "Sección 1"
print("Asignatura:", asignatura)
print("Sección:", seccion)

# Un mensaje final opcional
print("------------------------------------")
print("¡Espero que disfrutes aprendiendo Python!")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1. ¿Qué hace la función `print()` en Python?
2. Si quisieras que tu nombre apareciera entre comillas dobles en la salida
   (por ejemplo, "Ana Pérez"), ¿cómo modificarías la línea de código
   correspondiente? (Investiga sobre secuencias de escape o diferentes tipos de comillas).
3. ¿Por qué crees que se utilizan comentarios (líneas que empiezan con #) en el código?
   ¿El intérprete de Python ejecuta los comentarios?
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
    # Concatenación con +: se pegan los textos uno tras otro.
    # Ojo: el espacio después de los dos puntos lo pones tú, porque + no lo agrega.
    # Conviene: cuando quieres controlar cada espacio. Solo sirve con texto:
    # para pegar un número habría que convertirlo antes con str().
    nombre = "Ana Pérez"
    print("¡Bienvenido/a al mundo de Python!")
    print("------------------------------------")
    print("Mi nombre es: " + nombre)
    print("Asignatura: " + "Ayudantía de Programación")
    print("Sección: " + "Sección 1")
    print("------------------------------------")
    print("¡Espero que disfrutes aprendiendo Python!")


def alternativa_2():
    # f-string: una "f" antes de las comillas y las variables entre llaves {}.
    # Conviene: casi siempre. Es lo más legible y acepta números sin str().
    nombre = "Ana Pérez"
    asignatura = "Ayudantía de Programación"
    seccion = "Sección 1"
    print("¡Bienvenido/a al mundo de Python!")
    print("------------------------------------")
    print(f"Mi nombre es: {nombre}")
    print(f"Asignatura: {asignatura}")
    print(f"Sección: {seccion}")
    print("------------------------------------")
    print("¡Espero que disfrutes aprendiendo Python!")


def alternativa_3():
    # Un solo print() con saltos de línea (\n) dentro del texto.
    # Conviene: para mostrar un bloque de varias líneas de una sola vez.
    nombre = "Ana Pérez"
    print("¡Bienvenido/a al mundo de Python!\n"
          "------------------------------------\n"
          f"Mi nombre es: {nombre}\n"
          "Asignatura: Ayudantía de Programación\n"
          "Sección: Sección 1\n"
          "------------------------------------\n"
          "¡Espero que disfrutes aprendiendo Python!")


# alternativa_1()
# alternativa_2()
# alternativa_3()
