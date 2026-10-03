"""
-------------------------------------------------------------------------------
                                    FIGURA 2
                         Triángulo rectángulo invertido
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Imprime una escalera invertida alineada a la izquierda: la primera fila
tiene `altura` asteriscos y cada fila siguiente tiene uno menos.

## IDEA CLAVE:
## -----------
Es la escalera anterior al revés: `i` baja desde `altura` hasta 1. Para contar
hacia atrás, `range` recibe un paso negativo: range(inicio, fin, -1).

## ENTRADA:
## --------
Ninguna: cambia la variable `altura` dentro del código para probar otros tamaños.

## SALIDA ESPERADA (con altura = 5):
## ---------------------------------
*****
****
***
**
*
-------------------------------------------------------------------------------
"""

# Triángulo rectángulo invertido alineado a la izquierda
altura = 5

# range(altura, 0, -1) entrega 5, 4, 3, 2, 1 (el 0 NO se incluye)
for i in range(altura, 0, -1):
    print('*' * i)


"""
-------------------------------------------------------------------------------
## OTRAS FORMAS DE HACERLO (alternativas que producen el mismo resultado)
## ----------------------------------------------------------------------
Las funciones de abajo NO se ejecutan solas. Para probar una, quita el # de la
línea que la llama (al final del archivo) y ejecuta el programa.
-------------------------------------------------------------------------------
"""


def alternativa_1():
    # Contar hacia adelante y calcular cuántos asteriscos van en cada fila.
    # Conviene: cuando no recuerdas cómo usar el paso negativo de range().
    altura = 5
    for fila in range(altura):
        print('*' * (altura - fila))     # fila 0 -> 5 asteriscos, fila 1 -> 4, ...


def alternativa_2():
    # reversed() recorre un range de atrás hacia adelante, sin paso negativo.
    # Conviene: cuando prefieres escribir un range normal y darlo vuelta aparte.
    altura = 5
    for i in reversed(range(1, altura + 1)):
        print('*' * i)


# alternativa_1()
# alternativa_2()
