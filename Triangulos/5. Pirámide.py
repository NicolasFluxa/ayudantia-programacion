"""
-------------------------------------------------------------------------------
                                    FIGURA 5
                                    Pirámide
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Imprime una pirámide centrada: la primera fila tiene 1 asterisco y cada
fila siguiente tiene 2 más (1, 3, 5, 7, 9...), con espacios para centrarla.

## IDEA CLAVE:
## -----------
En la fila `i` van 2*i - 1 asteriscos (los números impares) y `altura - i`
espacios a cada lado. La fila más ancha mide 2*altura - 1 caracteres.

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
-------------------------------------------------------------------------------
"""

# Pirámide centrada
altura = 5

for i in range(1, altura + 1):
    espacios = ' ' * (altura - i)        # relleno a cada lado
    estrellas = '*' * (2 * i - 1)        # 1, 3, 5, 7, 9...
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
    # center(): centra el texto dentro de un ancho dado, rellenando con espacios.
    # Conviene: cuando solo necesitas centrar; no hay que calcular los espacios.
    altura = 5
    ancho = 2 * altura - 1               # ancho de la fila más grande
    for i in range(1, altura + 1):
        print(('*' * (2 * i - 1)).center(ancho))


def alternativa_2():
    # f-string con centrado: {texto:^ancho}.
    # Conviene: cuando ya estás armando el texto con f-strings.
    altura = 5
    ancho = 2 * altura - 1
    for i in range(1, altura + 1):
        print(f"{'*' * (2 * i - 1):^{ancho}}")


def alternativa_3():
    # Ciclo `while` en lugar de `for`.
    # Conviene: para practicar el while; aquí `for` es más compacto.
    altura = 5
    i = 1
    while i <= altura:
        espacios = ' ' * (altura - i)
        print(espacios + '*' * (2 * i - 1) + espacios)
        i += 1


# alternativa_1()
# alternativa_2()
# alternativa_3()
