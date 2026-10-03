"""
-------------------------------------------------------------------------------
                                  EJERCICIO 01
                         Contador con `for` y `range()`
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Escribe un programa que utilice un bucle `for` y la función `range()` para
realizar diferentes tipos de conteos:

1.  Solicita al usuario un número entero positivo (`limite`).
    Imprime los números desde 0 hasta `limite - 1`.
2.  Utilizando el mismo `limite`, imprime los números desde 1 hasta `limite`.
3.  Utilizando el mismo `limite`, imprime solo los números pares desde 0
    hasta `limite` (incluido si `limite` es par).

## OBJETIVO:
## ---------
Dominar las tres formas de `range()`: range(fin), range(inicio, fin)
y range(inicio, fin, paso). Recuerda: el valor final NUNCA se incluye.

## ENTRADA:
## --------
Un número entero positivo (el límite). Ejemplo: 4

## SALIDA ESPERADA (ejemplo de ejecución, con 4):
## ----------------------------------------------
Ingresa un número entero positivo (límite): 4

--- Conteo 1: Números desde 0 hasta 3 ---
0
1
2
3

--- Conteo 2: Números desde 1 hasta 4 ---
1
2
3
4

--- Conteo 3: Números pares desde 0 hasta 4 ---
0
2
4

¡Conteos finalizados!
-------------------------------------------------------------------------------
"""

# 1. Solicitar el número límite
limite_str = input("Ingresa un número entero positivo (límite): ")
limite = int(limite_str)

if limite < 1:   # con 0 o un negativo no hay nada que contar
    print("Por favor, ingresa un número entero positivo.")
else:
    # Conteo desde 0 hasta limite - 1
    print(f"\n--- Conteo 1: Números desde 0 hasta {limite - 1} ---")
    for i in range(limite): # range(limite) genera números de 0 a limite-1
        print(i)

    # Conteo desde 1 hasta limite
    print(f"\n--- Conteo 2: Números desde 1 hasta {limite} ---")
    # range(inicio, fin) genera números desde inicio hasta fin-1
    # Por eso usamos limite + 1 para incluir el 'limite'
    for i in range(1, limite + 1):
        print(i)

    # Conteo de números pares desde 0 hasta limite
    print(f"\n--- Conteo 3: Números pares desde 0 hasta {limite} ---")
    # range(inicio, fin, paso) genera números desde inicio hasta fin-1,
    # incrementando en 'paso'
    # Para incluir 'limite' si es par, vamos hasta limite + 1
    for i in range(0, limite + 1, 2):
        print(i)

    print("\n¡Conteos finalizados!")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  Explica las tres formas de usar `range()` que viste en este ejercicio:
    a) `range(stop)`
    b) `range(start, stop)`
    c) `range(start, stop, step)`
2.  Si quisieras imprimir los números del 10 al 1 (en orden descendente) usando
    `for` y `range()`, ¿cómo lo harías? (Pista: el `step` puede ser negativo).
3.  ¿Qué sucede si el valor de `start` es mayor que `stop` y el `step` es positivo
    en `range(start, stop, step)`?
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
    # Los mismos conteos con `while` (Semana 4): hay que inicializar, comparar y sumar.
    # Conviene: cuando el paso no es regular o la condición de término es más
    # compleja que "llegar a un número". Para conteos simples, `for` es más corto.
    limite = int(input("Ingresa un número entero positivo (límite): "))
    if limite < 1:
        print("Por favor, ingresa un número entero positivo.")
    else:
        print(f"\n--- Conteo 1: Números desde 0 hasta {limite - 1} ---")
        i = 0
        while i < limite:
            print(i)
            i += 1

        print(f"\n--- Conteo 2: Números desde 1 hasta {limite} ---")
        i = 1
        while i <= limite:
            print(i)
            i += 1

        print(f"\n--- Conteo 3: Números pares desde 0 hasta {limite} ---")
        i = 0
        while i <= limite:
            print(i)
            i += 2

        print("\n¡Conteos finalizados!")


def alternativa_2():
    # Pares con `if i % 2 == 0` en lugar de usar el tercer argumento de range().
    # `%` entrega el resto de la división: un número es par si su resto al dividir
    # por 2 es 0. Recorre TODOS los números y se queda solo con los pares.
    # Conviene: cuando el criterio no es "saltar de a N" (por ejemplo, múltiplos de 3
    # que además terminan en 5). Para pares simples, range(0, n + 1, 2) es más eficiente.
    limite = int(input("Ingresa un número entero positivo (límite): "))
    if limite < 1:
        print("Por favor, ingresa un número entero positivo.")
    else:
        print(f"\n--- Conteo 1: Números desde 0 hasta {limite - 1} ---")
        for i in range(limite):
            print(i)

        print(f"\n--- Conteo 2: Números desde 1 hasta {limite} ---")
        for i in range(1, limite + 1):
            print(i)

        print(f"\n--- Conteo 3: Números pares desde 0 hasta {limite} ---")
        for i in range(limite + 1):
            if i % 2 == 0:
                print(i)

        print("\n¡Conteos finalizados!")


def alternativa_3():
    # Imprimir todo el rango de una vez con print(*range(...), sep="\n").
    # El `*` "desarma" el range en argumentos separados (como si escribieras
    # print(0, 1, 2, 3)) y sep="\n" pone un salto de línea entre cada uno.
    # Conviene: para mostrar rápido una secuencia, sin necesidad de un bucle escrito.
    limite = int(input("Ingresa un número entero positivo (límite): "))
    if limite < 1:
        print("Por favor, ingresa un número entero positivo.")
    else:
        print(f"\n--- Conteo 1: Números desde 0 hasta {limite - 1} ---")
        print(*range(limite), sep="\n")
        print(f"\n--- Conteo 2: Números desde 1 hasta {limite} ---")
        print(*range(1, limite + 1), sep="\n")
        print(f"\n--- Conteo 3: Números pares desde 0 hasta {limite} ---")
        print(*range(0, limite + 1, 2), sep="\n")
        print("\n¡Conteos finalizados!")


# alternativa_1()
# alternativa_2()
# alternativa_3()
