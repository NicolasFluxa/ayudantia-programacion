"""
-------------------------------------------------------------------------------
                                  EJERCICIO 02
                            Menú Simple con `while`
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Crea un programa que muestre un menú simple al usuario y le permita elegir
una opción. El menú debe repetirse hasta que el usuario elija la opción de salir.

El programa debe:
1. Mostrar un menú con al menos 3 opciones, por ejemplo:
    "Menú Principal:"
    "1. Ver Saludo"
    "2. Mostrar Despedida"
    "3. Salir"
2. Usar un bucle `while` para que el menú se muestre repetidamente.
3. Solicitar al usuario que ingrese su opción.
4. Usar estructuras `if-elif-else` para procesar la opción:
    - Si elige "1", imprimir un saludo (ej: "¡Hola! Gracias por elegir esta opción.").
    - Si elige "2", imprimir una despedida (ej: "¡Adiós! Vuelve pronto.").
    - Si elige "3", terminar el bucle y el programa (ej: "Saliendo del programa...").
    - Si elige cualquier otra cosa, imprimir "Opción no válida. Intente de nuevo."

## OBJETIVO:
## ---------
Repetir un menú con `while` hasta que el usuario elige salir (valor centinela).

## ENTRADA:
## --------
Una opción por vuelta del menú: "1", "2" o "3" (texto, no se convierte a número).

## SALIDA ESPERADA (ejemplo de ejecución, eligiendo 1 y luego 3):
## --------------------------------------------------------------
--- Menú Principal ---
1. Ver Saludo
2. Mostrar Despedida
3. Salir
----------------------
Selecciona una opción (1-3): 1

¡Hola! 😊 Gracias por elegir esta opción.

(el menú se muestra de nuevo)
Selecciona una opción (1-3): 3

Saliendo del programa...
Programa finalizado.
-------------------------------------------------------------------------------
"""

# Variable que guarda la última opción elegida; el bucle la usa para decidir si sigue.
# Parte vacía para que la primera vez la condición (!= "3") sea verdadera y entre al bucle.
opcion_elegida = ""

# 2. Bucle `while` para mostrar el menú
while opcion_elegida != "3": # Continuar mientras no se elija "3" (Salir)
    # 1. Mostrar el menú
    print("\n--- Menú Principal ---")
    print("1. Ver Saludo")
    print("2. Mostrar Despedida")
    print("3. Salir")
    print("----------------------")

    # 3. Solicitar opción al usuario
    opcion_elegida = input("Selecciona una opción (1-3): ")

    # 4. Procesar la opción
    if opcion_elegida == "1":
        print("\n¡Hola! 😊 Gracias por elegir esta opción.")
    elif opcion_elegida == "2":
        print("\n¡Adiós! 👋 Vuelve pronto.")
    elif opcion_elegida == "3":
        print("\nSaliendo del programa...")
    else:
        print("\nOpción no válida. Por favor, intente de nuevo.")

print("Programa finalizado.")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1. ¿Cuál es la condición que mantiene el bucle `while` en ejecución? ¿Cuándo se detiene?
2. ¿Qué es un "centinela" en el contexto de los bucles? ¿Podrías identificar
   un valor que actúa como centinela en este programa?
3. Modifica el programa para añadir una cuarta opción al menú, por ejemplo,
   "4. Mostrar un chiste", e implementa su funcionalidad.
   Asegúrate de actualizar la condición del `while` si es necesario.
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
    # `while True` + `break`: el menú se repite para siempre y se corta al elegir "3".
    # Conviene: cuando no quieres inventar un valor inicial para la variable
    # (aquí ya no hace falta el opcion_elegida = ""). Es el patrón más usado en menús.
    while True:
        print("\n--- Menú Principal ---")
        print("1. Ver Saludo")
        print("2. Mostrar Despedida")
        print("3. Salir")
        print("----------------------")
        opcion_elegida = input("Selecciona una opción (1-3): ")

        if opcion_elegida == "1":
            print("\n¡Hola! 😊 Gracias por elegir esta opción.")
        elif opcion_elegida == "2":
            print("\n¡Adiós! 👋 Vuelve pronto.")
        elif opcion_elegida == "3":
            print("\nSaliendo del programa...")
            break
        else:
            print("\nOpción no válida. Por favor, intente de nuevo.")
    print("Programa finalizado.")


def alternativa_2():
    # Una variable booleana (bandera) que dice si el programa sigue en marcha.
    # Conviene: cuando hay varias razones para terminar y quieres dar un nombre claro
    # a la condición (`while not salir` se lee casi como una frase).
    salir = False
    while not salir:
        print("\n--- Menú Principal ---")
        print("1. Ver Saludo")
        print("2. Mostrar Despedida")
        print("3. Salir")
        print("----------------------")
        opcion_elegida = input("Selecciona una opción (1-3): ")

        if opcion_elegida == "1":
            print("\n¡Hola! 😊 Gracias por elegir esta opción.")
        elif opcion_elegida == "2":
            print("\n¡Adiós! 👋 Vuelve pronto.")
        elif opcion_elegida == "3":
            print("\nSaliendo del programa...")
            salir = True
        else:
            print("\nOpción no válida. Por favor, intente de nuevo.")
    print("Programa finalizado.")


# alternativa_1()
# alternativa_2()
