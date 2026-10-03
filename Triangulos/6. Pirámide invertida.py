"""
-------------------------------------------------------------------------------
                                    FIGURA 6
                               Pirámide invertida
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Imprime una pirámide al revés, centrada: la primera fila es la más ancha
(9 asteriscos si la altura es 5) y cada fila siguiente tiene 2 menos.

## IDEA CLAVE:
## -----------
Es la pirámide de la figura 5 con `i` bajando de `altura` a 1. En cada fila
van 2*i - 1 asteriscos y `altura - i` espacios a cada lado.

## ENTRADA:
## --------
Ninguna: cambia la variable `altura` dentro del código para probar otros tamaños.

## SALIDA ESPERADA (con altura = 5):
## ---------------------------------
*********
 *******
  *****
   ***
    *
-------------------------------------------------------------------------------
"""

# Pirámide invertida centrada
altura = 5

for i in range(altura, 0, -1):
    espacios = ' ' * (altura - i)
    estrellas = '*' * (2 * i - 1)
    print(espacios + estrellas + espacios)


"""
-------------------------------------------------------------------------------
## OTRAS FORMAS DE HACERLO (alternativas que producen el mismo resultado)
## ----------------------------------------------------------------------
Las funciones de abajo NO se ejecutan solas. Para probar una, quita el # de la
línea que la llama (al final del archivo) y ejecuta el programa.
-------------------------------------------------------------------------------
"""


def alternativa_1():
    # center() para centrar cada fila, igual que en la figura 5.
    # Conviene: es la forma más corta para figuras centradas.
    altura = 5
    ancho = 2 * altura - 1
    for i in range(altura, 0, -1):
        print(('*' * (2 * i - 1)).center(ancho))


def alternativa_2():
    # Armar la pirámide normal y recorrerla de atrás hacia adelante.
    # Conviene: cuando ya tienes la figura 5 y solo quieres darla vuelta.
    altura = 5
    filas = []
    for i in range(1, altura + 1):
        filas.append(' ' * (altura - i) + '*' * (2 * i - 1) + ' ' * (altura - i))
    for fila in reversed(filas):
        print(fila)


# alternativa_1()
# alternativa_2()
