"""
-------------------------------------------------------------------------------
                                  EJERCICIO 01
                           Verificar Mayoría de Edad
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Escribe un programa que solicite al usuario su edad y determine si es mayor
de edad o no. En Chile, se considera mayor de edad a partir de los 18 años.

El programa debe:
1. Solicitar al usuario que ingrese su edad (como un número entero).
2. Utilizar una estructura condicional `if-else` para verificar si la edad
   ingresada es mayor o igual a 18.
3. Mostrar un mensaje apropiado indicando si el usuario es "Mayor de edad"
   o "Menor de edad".

## OBJETIVO:
## ---------
Tomar una decisión con `if-else` a partir de una comparación (`>=`).

## ENTRADA:
## --------
Un número entero: la edad. Ejemplo: 20

## SALIDA ESPERADA (dos ejemplos de ejecución):
## --------------------------------------------
Con 20:
    Por favor, ingresa tu edad: 20
    Eres Mayor de edad. ¡Bienvenido/a!
    ------------------------------------
    Gracias por usar el verificador de edad.
Con 15:
    Por favor, ingresa tu edad: 15
    Eres Menor de edad.
    ------------------------------------
    Gracias por usar el verificador de edad.
-------------------------------------------------------------------------------
"""

# 1. Solicitar la edad al usuario
edad_str = input("Por favor, ingresa tu edad: ")
edad = int(edad_str) # Convertir la entrada a un número entero

# 2. Verificar si es mayor de edad usando if-else.
# Ojo con los dos puntos (:) y con la sangría: lo que está indentado pertenece al if/else.
if edad >= 18:
    # 3. Mostrar mensaje si es mayor de edad
    print("Eres Mayor de edad. ¡Bienvenido/a!")
else:
    # 3. Mostrar mensaje si es menor de edad
    print("Eres Menor de edad.")

# Mensaje final del programa (opcional)
print("------------------------------------")
print("Gracias por usar el verificador de edad.")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1. ¿Qué operador de comparación se utiliza para verificar si la edad es "mayor o igual a" 18?
   ¿Qué pasaría si solo usaras el operador `>` (mayor que)?
2. ¿Es obligatorio que un bloque `if` tenga siempre un bloque `else` asociado?
   ¿En qué situaciones podrías usar un `if` sin un `else`?
3. Modifica el programa para que, además de indicar si es mayor o menor de edad,
   si la persona tiene exactamente 18 años, imprima un mensaje adicional como
   "¡Felicitaciones, justo en la mayoría de edad!".
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
    # Guardar la decisión en una variable booleana y preguntar por ella.
    # Conviene: cuando vas a usar la misma decisión más de una vez en el programa.
    edad = int(input("Por favor, ingresa tu edad: "))
    es_mayor = edad >= 18
    if es_mayor:
        print("Eres Mayor de edad. ¡Bienvenido/a!")
    else:
        print("Eres Menor de edad.")
    print("------------------------------------")
    print("Gracias por usar el verificador de edad.")


def alternativa_2():
    # "if en línea" (operador ternario): elige entre dos valores en una sola línea.
    # Formato:  valor_si_cumple if condicion else valor_si_no_cumple
    # Conviene: cuando solo cambia un valor (aquí, el mensaje). Si cada rama
    # hace varias cosas, usa el if-else de siempre.
    edad = int(input("Por favor, ingresa tu edad: "))
    mensaje = "Eres Mayor de edad. ¡Bienvenido/a!" if edad >= 18 else "Eres Menor de edad."
    print(mensaje)
    print("------------------------------------")
    print("Gracias por usar el verificador de edad.")


def alternativa_3():
    # Preguntar primero por el caso contrario (edad < 18). Es equivalente a >= 18
    # con las ramas intercambiadas.
    # Conviene: cuando el caso "especial" (menor de edad) es el que quieres destacar.
    edad = int(input("Por favor, ingresa tu edad: "))
    if edad < 18:
        print("Eres Menor de edad.")
    else:
        print("Eres Mayor de edad. ¡Bienvenido/a!")
    print("------------------------------------")
    print("Gracias por usar el verificador de edad.")


# alternativa_1()
# alternativa_2()
# alternativa_3()
