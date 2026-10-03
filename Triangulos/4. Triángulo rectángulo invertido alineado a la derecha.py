"""
-------------------------------------------------------------------------------
                                    FIGURA 4
              Triángulo rectángulo invertido alineado a la derecha
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Imprime la escalera invertida pegada al lado derecho: la primera fila
tiene `altura` asteriscos y cada fila siguiente tiene uno menos, con espacios
a la izquierda.

## IDEA CLAVE:
## -----------
Combina las figuras 2 y 3: `i` baja de `altura` a 1 y cada fila lleva
`altura - i` espacios seguidos de `i` asteriscos.

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

# Triángulo rectángulo invertido alineado a la derecha
altura = 5

for i in range(altura, 0, -1):
    print(' ' * (altura - i) + '*' * i)


"""
-------------------------------------------------------------------------------
## OTRAS FORMAS DE HACERLO (alternativas que producen el mismo resultado)
## ----------------------------------------------------------------------
Las funciones de abajo NO se ejecutan solas. Para probar una, quita el # de la
línea que la llama (al final del archivo) y ejecuta el programa.
-------------------------------------------------------------------------------
"""


def alternativa_1():
    # rjust() para alinear a la derecha, sin calcular los espacios.
    # Conviene: es la forma más corta y se lee casi como el enunciado.
    altura = 5
    for i in range(altura, 0, -1):
        print(('*' * i).rjust(altura))


def alternativa_2():
    # Ciclo `while` con el contador bajando de a uno.
    # Conviene: para practicar la condición del while; aquí `for` es más compacto.
    altura = 5
    i = altura
    while i > 0:
        print(' ' * (altura - i) + '*' * i)
        i -= 1


# alternativa_1()
# alternativa_2()
