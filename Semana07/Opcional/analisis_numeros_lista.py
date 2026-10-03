"""
-------------------------------------------------------------------------------
                             EJERCICIO OPCIONAL 01
                          Análisis de Números en Lista
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Dada una lista de números (por ejemplo, calificaciones de estudiantes),
realiza un análisis básico SIN usar las funciones incorporadas `sum()`, `min()`,
`max()` de Python para esos cálculos específicos (sí puedes usar `len()`).

1.  Crea una lista llamada `calificaciones` con al menos 8 números enteros
    (entre 10 y 70, simulando notas).
2.  Calcula e imprime la suma de todas las calificaciones usando un bucle `for`.
3.  Encuentra e imprime la calificación más alta (máxima) usando un bucle `for`
    y una variable para llevar el seguimiento del máximo actual.
4.  Encuentra e imprime la calificación más baja (mínima) usando un bucle `for`
    y una variable para llevar el seguimiento del mínimo actual.
5.  Calcula e imprime el promedio de las calificaciones (suma / cantidad).
6.  Muestra una porción (slice) de la lista: desde el segundo elemento hasta
    el quinto (índices 1 a 4).

## OBJETIVO:
## ---------
Practicar los patrones de acumulador, máximo y mínimo con `for`, y el
corte de listas (slicing).

## ENTRADA:
## --------
Ninguna: la lista está escrita en el código.

## SALIDA ESPERADA (con la lista de la solución):
## ----------------------------------------------
Calificaciones: [55, 70, 45, 62, 30, 50, 68, 40, 65]
-----------------------------------------
Suma de las calificaciones: 485
Calificación más alta: 70
Calificación más baja: 30
Promedio de calificaciones: 53.89
-----------------------------------------
Slice de calificaciones (del índice 1 al 4): [70, 45, 62, 30]
-----------------------------------------
-------------------------------------------------------------------------------
"""

# 1. Crear lista de calificaciones
calificaciones = [55, 70, 45, 62, 30, 50, 68, 40, 65]
print("Calificaciones:", calificaciones)
print("-----------------------------------------")

# Verificar que la lista no esté vacía antes de procesar
if len(calificaciones) > 0:
    # 2. Calcular la suma
    suma_calificaciones = 0
    for nota in calificaciones:
        suma_calificaciones += nota
    print(f"Suma de las calificaciones: {suma_calificaciones}")

    # 3. Encontrar la calificación más alta (máxima)
    # Inicializamos el máximo con el primer elemento de la lista (así funciona aunque todas sean negativas)
    calificacion_maxima = calificaciones[0]
    for nota in calificaciones:
        if nota > calificacion_maxima:
            calificacion_maxima = nota
    print(f"Calificación más alta: {calificacion_maxima}")

    # 4. Encontrar la calificación más baja (mínima)
    # Inicializamos el mínimo con el primer elemento de la lista
    calificacion_minima = calificaciones[0]
    for nota in calificaciones:
        if nota < calificacion_minima:
            calificacion_minima = nota
    print(f"Calificación más baja: {calificacion_minima}")

    # 5. Calcular el promedio
    cantidad_calificaciones = len(calificaciones)
    promedio = suma_calificaciones / cantidad_calificaciones
    print(f"Promedio de calificaciones: {promedio:.2f}") # Formateado a 2 decimales
    print("-----------------------------------------")

    # 6. Mostrar un slice de la lista (del segundo al quinto elemento)
    # Recordar que el slicing es [inicio:fin], donde 'fin' no se incluye.
    # Para elementos en índice 1, 2, 3, 4, el slice es [1:5]
    slice_calificaciones = calificaciones[1:5]
    print(f"Slice de calificaciones (del índice 1 al 4): {slice_calificaciones}")

else:
    print("La lista de calificaciones está vacía. No se puede realizar el análisis.")

print("-----------------------------------------")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  Al buscar el máximo y el mínimo, ¿por qué es una buena práctica inicializar
    `calificacion_maxima` y `calificacion_minima` con el primer elemento de la
    lista en lugar de un valor fijo como 0 o 100?
2.  Explica la sintaxis de "slicing" de listas en Python: `lista[inicio:fin:paso]`.
    ¿Qué representan `inicio`, `fin` y `paso`? ¿Qué sucede si omites alguno de ellos?
    Prueba algunos ejemplos: `calificaciones[:3]`, `calificaciones[4:]`, `calificaciones[::2]`.
3.  Si quisieras agregar todas las calificaciones de otra lista (`nuevas_calificaciones`)
    a la lista `calificaciones` existente, ¿qué método de lista usarías?
4.  (Desafío) ¿Cómo modificarías el código para contar cuántos estudiantes
    aprobaron, considerando que se aprueba con una calificación mayor o igual a 40?
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
    # Las funciones incorporadas sum(), max() y min().
    # Hacen exactamente lo que los tres bucles de la solución principal.
    # Conviene: SIEMPRE que puedas usarlas (el enunciado las prohíbe solo para que
    # practiques el patrón del acumulador, que se usa en muchos otros problemas).
    calificaciones = [55, 70, 45, 62, 30, 50, 68, 40, 65]
    print("Calificaciones:", calificaciones)
    print("-----------------------------------------")
    if len(calificaciones) > 0:
        suma_calificaciones = sum(calificaciones)
        print(f"Suma de las calificaciones: {suma_calificaciones}")
        print(f"Calificación más alta: {max(calificaciones)}")
        print(f"Calificación más baja: {min(calificaciones)}")
        promedio = suma_calificaciones / len(calificaciones)
        print(f"Promedio de calificaciones: {promedio:.2f}")
        print("-----------------------------------------")
        print(f"Slice de calificaciones (del índice 1 al 4): {calificaciones[1:5]}")
    else:
        print("La lista de calificaciones está vacía. No se puede realizar el análisis.")
    print("-----------------------------------------")


def alternativa_2():
    # Ordenar una copia y tomar los extremos: el menor queda primero y el mayor, último.
    # sorted() entrega una lista nueva y no toca la original.
    # Conviene: cuando además del máximo y el mínimo necesitas la lista ordenada.
    # Si solo quieres el máximo o el mínimo, un solo recorrido (o max()/min()) es más
    # rápido que ordenar todo.
    calificaciones = [55, 70, 45, 62, 30, 50, 68, 40, 65]
    print("Calificaciones:", calificaciones)
    print("-----------------------------------------")
    if len(calificaciones) > 0:
        suma_calificaciones = 0
        for nota in calificaciones:
            suma_calificaciones += nota
        print(f"Suma de las calificaciones: {suma_calificaciones}")

        ordenadas = sorted(calificaciones)
        print(f"Calificación más alta: {ordenadas[-1]}")
        print(f"Calificación más baja: {ordenadas[0]}")

        promedio = suma_calificaciones / len(calificaciones)
        print(f"Promedio de calificaciones: {promedio:.2f}")
        print("-----------------------------------------")
        print(f"Slice de calificaciones (del índice 1 al 4): {calificaciones[1:5]}")
    else:
        print("La lista de calificaciones está vacía. No se puede realizar el análisis.")
    print("-----------------------------------------")


def alternativa_3():
    # Un solo recorrido que calcula suma, máximo y mínimo a la vez.
    # Conviene: cuando la lista es muy grande y no quieres recorrerla tres veces.
    # El código es un poco más denso, pero hace 1 pasada en vez de 3.
    calificaciones = [55, 70, 45, 62, 30, 50, 68, 40, 65]
    print("Calificaciones:", calificaciones)
    print("-----------------------------------------")
    if len(calificaciones) > 0:
        suma_calificaciones = 0
        calificacion_maxima = calificaciones[0]
        calificacion_minima = calificaciones[0]
        for nota in calificaciones:
            suma_calificaciones += nota
            if nota > calificacion_maxima:
                calificacion_maxima = nota
            if nota < calificacion_minima:
                calificacion_minima = nota
        print(f"Suma de las calificaciones: {suma_calificaciones}")
        print(f"Calificación más alta: {calificacion_maxima}")
        print(f"Calificación más baja: {calificacion_minima}")
        promedio = suma_calificaciones / len(calificaciones)
        print(f"Promedio de calificaciones: {promedio:.2f}")
        print("-----------------------------------------")
        print(f"Slice de calificaciones (del índice 1 al 4): {calificaciones[1:5]}")
    else:
        print("La lista de calificaciones está vacía. No se puede realizar el análisis.")
    print("-----------------------------------------")


# alternativa_1()
# alternativa_2()
# alternativa_3()
