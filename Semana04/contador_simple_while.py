"""
-------------------------------------------------------------------------------
                                  EJERCICIO 01
                          Contador Simple con `while`
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Escribe un programa que utilice un bucle `while` para contar y mostrar
los números desde 1 hasta un número ingresado por el usuario.

El programa debe:
1. Solicitar al usuario que ingrese un número entero positivo (el límite).
2. Inicializar una variable contador en 1.
3. Usar un bucle `while` que continúe mientras el contador sea menor o igual
   al número límite ingresado.
4. Dentro del bucle, imprimir el valor actual del contador.
5. Incrementar el contador en 1 en cada iteración.

## OBJETIVO:
## ---------
Conocer las tres partes de un `while`: inicializar, condición y actualización.

## ENTRADA:
## --------
Un número entero positivo (el límite). Ejemplo: 5

## SALIDA ESPERADA (ejemplo de ejecución, con 5):
## ----------------------------------------------
Ingresa un número entero positivo para contar hasta él: 5
Contando desde 1 hasta 5:
1
2
3
4
5
¡Conteo finalizado!

Si el número es menor que 1, solo se muestra un aviso y no se cuenta.
-------------------------------------------------------------------------------
"""

# 1. Solicitar el número límite al usuario
limite_str = input("Ingresa un número entero positivo para contar hasta él: ")
limite = int(limite_str)

# Validar que el límite sea positivo (opcional, pero buena práctica)
if limite < 1:
    print("Por favor, ingresa un número entero positivo.")
else:
    # 2. Inicializar el contador
    contador = 1
    print(f"Contando desde 1 hasta {limite}:")

    # 3. Usar un bucle `while`: se repite MIENTRAS la condición sea verdadera.
    # Si olvidas actualizar el contador, la condición nunca cambia y el bucle no termina.
    while contador <= limite:
        # 4. Imprimir el valor actual del contador
        print(contador)
        # 5. Incrementar el contador
        contador = contador + 1 # También puede ser contador += 1

    print("¡Conteo finalizado!")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1. ¿Qué tres partes principales identificas en la estructura de este bucle `while`
   (inicialización, condición, actualización)?
2. ¿Qué pasaría si olvidaras la línea `contador = contador + 1` dentro del bucle?
   ¿Cómo se comportaría el programa? (Esto se conoce como bucle infinito).
3. Modifica el programa para que cuente hacia atrás, desde el número ingresado
   por el usuario hasta 1.
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
    # Ciclo `for` con range(): Python lleva el contador por ti.
    # range(1, limite + 1) entrega 1, 2, ..., limite (el final NO se incluye, por eso el +1).
    # Conviene: cuando sabes de antemano cuántas veces repetir. Es más corto y no
    # puedes olvidar el incremento (el error del bucle infinito).
    limite = int(input("Ingresa un número entero positivo para contar hasta él: "))
    if limite < 1:
        print("Por favor, ingresa un número entero positivo.")
    else:
        print(f"Contando desde 1 hasta {limite}:")
        for contador in range(1, limite + 1):
            print(contador)
        print("¡Conteo finalizado!")


def alternativa_2():
    # `while True` con `break`: el bucle "no termina nunca" salvo que tú lo cortes.
    # Conviene: cuando la condición de salida se descubre a mitad del bucle (menús,
    # juegos, validar datos). Aquí es innecesario, pero sirve para practicar el patrón.
    limite = int(input("Ingresa un número entero positivo para contar hasta él: "))
    if limite < 1:
        print("Por favor, ingresa un número entero positivo.")
    else:
        print(f"Contando desde 1 hasta {limite}:")
        contador = 1
        while True:
            print(contador)
            if contador == limite:
                break
            contador += 1   # `+=` es la forma corta de contador = contador + 1
        print("¡Conteo finalizado!")


# alternativa_1()
# alternativa_2()
