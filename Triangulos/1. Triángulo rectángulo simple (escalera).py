"""
-------------------------------------------------------------------------------
                                    FIGURA 1
                     Triángulo rectángulo simple (escalera)
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Imprime una escalera de asteriscos (*) alineada a la izquierda: la primera
fila tiene 1 asterisco, la segunda 2, y así hasta llegar a `altura`.

## IDEA CLAVE:
## -----------
En la fila `i` se imprimen `i` asteriscos. Multiplicar un texto por un número
lo repite: '*' * 3 da '***'.

## ENTRADA:
## --------
Ninguna: cambia la variable `altura` dentro del código para probar otros tamaños.

## SALIDA ESPERADA (con altura = 5):
## ---------------------------------
*
**
***
****
*****
-------------------------------------------------------------------------------
"""

# Triángulo rectángulo alineado a la izquierda
altura = 5   # Cambia este valor para hacer la figura más grande o más pequeña

# i toma los valores 1, 2, ..., altura (el final de range NO se incluye, por eso el +1)
for i in range(1, altura + 1):
    print('*' * i)   # '*' * i repite el asterisco i veces


"""
-------------------------------------------------------------------------------
## OTRAS FORMAS DE HACERLO (alternativas que producen el mismo resultado)
## ----------------------------------------------------------------------
Las funciones de abajo NO se ejecutan solas. Para probar una, quita el # de la
línea que la llama (al final del archivo) y ejecuta el programa.
-------------------------------------------------------------------------------
"""


def alternativa_1():
    # Ciclo `while` en lugar de `for`. Hay que inicializar y avanzar el contador a mano.
    # Conviene: cuando no sabes de antemano cuántas filas habrá. Aquí, `for` es más corto.
    altura = 5
    i = 1
    while i <= altura:
        print('*' * i)
        i += 1


def alternativa_2():
    # Armar cada fila agregando UN asterisco a la fila anterior (sin multiplicar).
    # Conviene: para entender que '*' * i es lo mismo que repetir una suma de textos.
    altura = 5
    fila = ""
    for i in range(altura):
        fila = fila + '*'      # la fila crece de a un asterisco
        print(fila)


# alternativa_1()
# alternativa_2()
