"""
-------------------------------------------------------------------------------
                                    FIGURA 7
                          Diamante (combinando ambas)
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Imprime un diamante: una pirámide hacia arriba seguida de una pirámide
invertida. La fila más ancha (la del medio) se imprime una sola vez.

## IDEA CLAVE:
## -----------
Parte superior: la pirámide de la figura 5. Parte inferior: la pirámide
invertida SIN su primera fila (por eso empieza en `altura - 1`), para no
repetir la fila del medio.

## ENTRADA:
## --------
Ninguna: cambia la variable `altura` dentro del código para probar otros tamaños.

## SALIDA ESPERADA (con altura = 5):
## ---------------------------------
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
-------------------------------------------------------------------------------
"""

# Diamante completo
altura = 5

# Parte superior: de 1 a altura
for i in range(1, altura + 1):
    espacios = ' ' * (altura - i)
    estrellas = '*' * (2 * i - 1)
    print(espacios + estrellas + espacios)

# Parte inferior: de altura - 1 a 1 (sin repetir la fila del medio)
for i in range(altura - 1, 0, -1):
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
    # Un solo `for` que recorre las "alturas" de las filas: 1,2,3,4,5,4,3,2,1.
    # Conviene: cuando no quieres repetir el mismo bloque de código dos veces.
    altura = 5
    subida = list(range(1, altura + 1))              # [1, 2, 3, 4, 5]
    bajada = list(range(altura - 1, 0, -1))          # [4, 3, 2, 1]
    for i in subida + bajada:                         # + une las dos listas
        espacios = ' ' * (altura - i)
        print(espacios + '*' * (2 * i - 1) + espacios)


def alternativa_2():
    # Un solo `for` con valores absolutos: k va de -4 a 4 y abs(k) es la distancia
    # al centro. Así, i = altura - abs(k) sube hasta altura y vuelve a bajar.
    # Conviene: para ver que el diamante es una figura simétrica; es más corto,
    # pero más difícil de leer al principio.
    altura = 5
    for k in range(-(altura - 1), altura):           # -4, -3, ..., 0, ..., 3, 4
        i = altura - abs(k)                          # 1, 2, 3, 4, 5, 4, 3, 2, 1
        espacios = ' ' * (altura - i)
        print(espacios + '*' * (2 * i - 1) + espacios)


def alternativa_3():
    # center() para cada fila, con el ancho de la fila del medio.
    # Conviene: la forma más corta cuando todas las filas se centran igual.
    altura = 5
    ancho = 2 * altura - 1
    for i in list(range(1, altura + 1)) + list(range(altura - 1, 0, -1)):
        print(('*' * (2 * i - 1)).center(ancho))


# alternativa_1()
# alternativa_2()
# alternativa_3()
