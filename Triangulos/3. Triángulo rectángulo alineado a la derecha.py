"""
-------------------------------------------------------------------------------
                                    FIGURA 3
                   Triángulo rectángulo alineado a la derecha
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Imprime una escalera de asteriscos pegada al lado derecho: cada fila
se rellena a la izquierda con espacios para que todas terminen en la misma columna.

## IDEA CLAVE:
## -----------
En la fila `i` van `altura - i` espacios y luego `i` asteriscos. Cada fila
mide siempre `altura` caracteres.

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

# Triángulo rectángulo alineado a la derecha
altura = 5

for i in range(1, altura + 1):
    # espacios para empujar a la derecha + asteriscos de la fila
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
    # rjust(): el texto se alinea a la derecha dentro de un ancho dado.
    # '**'.rjust(5) agrega 3 espacios a la izquierda y da '   **'.
    # Conviene: cuando solo necesitas alinear; evita calcular los espacios a mano.
    altura = 5
    for i in range(1, altura + 1):
        print(('*' * i).rjust(altura))


def alternativa_2():
    # f-string con ancho y alineación: {texto:>ancho} alinea a la derecha.
    # Conviene: cuando ya estás armando el texto con f-strings.
    altura = 5
    for i in range(1, altura + 1):
        print(f"{'*' * i:>{altura}}")


# alternativa_1()
# alternativa_2()
