"""
-------------------------------------------------------------------------------
                             EJERCICIO OPCIONAL 01
                         Adivina el Número con `while`
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Crea un juego simple donde el programa "piensa" un número secreto y el
usuario tiene que adivinarlo.

El programa debe:
1. Definir un número secreto (puedes "hardcodearlo", es decir, escribirlo
   directamente en el código, por ejemplo: `numero_secreto = 7`).
2. Inicializar una variable para el intento del usuario.
3. Usar un bucle `while` que continúe mientras el intento del usuario
   NO sea igual al número secreto.
4. Dentro del bucle:
    a. Solicitar al usuario que ingrese su intento (un número entero).
    b. Usar condicionales (`if-elif-else` o `if-if`) para indicar si el
       intento fue "muy alto", "muy bajo" o si adivinó correctamente.
5. Cuando el usuario adivine, imprimir un mensaje de felicitaciones
   y terminar el bucle.
(Opcional Avanzado): Contar cuántos intentos le tomó al usuario adivinar.

## OBJETIVO:
## ---------
Combinar `while` y `if-elif-else`: repetir hasta cumplir una condición y dar pistas.

## ENTRADA:
## --------
Un número entero por intento (se repite hasta acertar). El secreto es 42.

## SALIDA ESPERADA (ejemplo de ejecución, intentando 50, 20 y 42):
## ---------------------------------------------------------------
¡Bienvenido al juego 'Adivina el Número'!
He pensado un número entre 1 y 100. ¡Intenta adivinarlo!
----------------------------------------------------
Ingresa tu intento: 50
Tu intento es muy alto. ¡Sigue intentando!
Ingresa tu intento: 20
Tu intento es muy bajo. ¡Sigue intentando!
Ingresa tu intento: 42

¡Felicidades! 🎉 ¡Has adivinado el número secreto: 42!
Te tomó 3 intento(s).
----------------------------------------------------
¡Gracias por jugar!
-------------------------------------------------------------------------------
"""

# 1. Definir el número secreto
numero_secreto = 42
# (Para hacerlo más interesante, podrías usar el módulo `random` para generar un
# número aleatorio, pero por ahora lo dejaremos fijo. Ver la alternativa_2 de abajo.)

# 2. Inicializar variables
intento_usuario = 0 # Valor inicial distinto del secreto, para que el while entre la primera vez
intentos_realizados = 0 # Opcional: contador de intentos

print("¡Bienvenido al juego 'Adivina el Número'!")
print("He pensado un número entre 1 y 100. ¡Intenta adivinarlo!")
print("----------------------------------------------------")

# 3. Bucle `while` mientras no adivine
while intento_usuario != numero_secreto:
    # 4a. Solicitar intento al usuario
    intento_str = input("Ingresa tu intento: ")
    intento_usuario = int(intento_str)

    intentos_realizados = intentos_realizados + 1 # Opcional

    # 4b. Comparar y dar pistas
    if intento_usuario < numero_secreto:
        print("Tu intento es muy bajo. ¡Sigue intentando!")
    elif intento_usuario > numero_secreto:
        print("Tu intento es muy alto. ¡Sigue intentando!")
    else:
        # 5. Mensaje de felicitaciones al adivinar
        print(f"\n¡Felicidades! 🎉 ¡Has adivinado el número secreto: {numero_secreto}!")
        print(f"Te tomó {intentos_realizados} intento(s).") # Opcional

print("----------------------------------------------------")
print("¡Gracias por jugar!")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1. ¿Cuál es la condición principal que controla el bucle `while` en este juego?
2. Si el número secreto fuera 50 y el usuario ingresa 50 en el primer intento,
   ¿cuántas veces se ejecutaría el cuerpo del bucle `while`? ¿Por qué?
3. ¿Qué pasaría si inicializaras `intento_usuario = numero_secreto` antes de
   que comience el bucle `while`?
4. (Referente a la parte opcional) ¿Dónde y por qué se incrementa la variable
   `intentos_realizados`?
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
    # `while True` + `break`: no hace falta inicializar `intento_usuario` con un valor
    # "falso", porque la condición de salida se revisa dentro del bucle.
    # Conviene: cuando el primer paso (pedir el dato) ya es parte del bucle.
    numero_secreto = 42
    intentos_realizados = 0
    print("¡Bienvenido al juego 'Adivina el Número'!")
    print("He pensado un número entre 1 y 100. ¡Intenta adivinarlo!")
    print("----------------------------------------------------")
    while True:
        intento_usuario = int(input("Ingresa tu intento: "))
        intentos_realizados += 1
        if intento_usuario < numero_secreto:
            print("Tu intento es muy bajo. ¡Sigue intentando!")
        elif intento_usuario > numero_secreto:
            print("Tu intento es muy alto. ¡Sigue intentando!")
        else:
            print(f"\n¡Felicidades! 🎉 ¡Has adivinado el número secreto: {numero_secreto}!")
            print(f"Te tomó {intentos_realizados} intento(s).")
            break
    print("----------------------------------------------------")
    print("¡Gracias por jugar!")


def alternativa_2():
    # Número secreto aleatorio con el módulo `random` (novedad).
    # `import random` trae herramientas de azar; random.randint(1, 100) entrega un
    # entero entre 1 y 100, ambos incluidos. El juego es igual, pero cambia cada vez.
    # Conviene: para que el juego se pueda jugar más de una vez. No se compara con la
    # salida del programa original porque el secreto ya no es 42.
    import random
    numero_secreto = random.randint(1, 100)
    intento_usuario = 0
    intentos_realizados = 0
    print("¡Bienvenido al juego 'Adivina el Número'!")
    print("He pensado un número entre 1 y 100. ¡Intenta adivinarlo!")
    print("----------------------------------------------------")
    while intento_usuario != numero_secreto:
        intento_usuario = int(input("Ingresa tu intento: "))
        intentos_realizados += 1
        if intento_usuario < numero_secreto:
            print("Tu intento es muy bajo. ¡Sigue intentando!")
        elif intento_usuario > numero_secreto:
            print("Tu intento es muy alto. ¡Sigue intentando!")
        else:
            print(f"\n¡Felicidades! 🎉 ¡Has adivinado el número secreto: {numero_secreto}!")
            print(f"Te tomó {intentos_realizados} intento(s).")
    print("----------------------------------------------------")
    print("¡Gracias por jugar!")


# alternativa_1()
# alternativa_2()   # esta no se puede probar con entradas fijas: el secreto es al azar
