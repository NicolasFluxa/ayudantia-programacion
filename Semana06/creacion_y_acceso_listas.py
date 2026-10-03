"""
-------------------------------------------------------------------------------
                                  EJERCICIO 01
                       Creación y Acceso Básico a Listas
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Este ejercicio te introducirá a la creación de listas y cómo acceder a
sus elementos.

1.  Crea una lista llamada `frutas_favoritas` que contenga al menos 5 nombres
    de tus frutas favoritas como cadenas de texto.
2.  Imprime la lista completa `frutas_favoritas` en la consola.
3.  Imprime la primera fruta de la lista (pista: el primer elemento tiene índice 0).
4.  Imprime la tercera fruta de la lista.
5.  Imprime la última fruta de la lista (pista: puedes usar un índice negativo).
6.  Utiliza la función `len()` para obtener e imprimir la cantidad de frutas
    en tu lista.

## OBJETIVO:
## ---------
Crear una lista, acceder a sus elementos por índice (positivo y negativo)
y medir su largo con `len()`.

## ENTRADA:
## --------
Ninguna: la lista se escribe directamente en el código.

## SALIDA ESPERADA (con la lista de la solución):
## ----------------------------------------------
Mis frutas favoritas son: ['Manzana', 'Plátano', 'Frutilla', 'Mango', 'Cereza']
-----------------------------------------
La primera fruta de la lista es: Manzana
La tercera fruta de la lista es: Frutilla
La última fruta de la lista es: Cereza
-----------------------------------------
Tengo 5 frutas favoritas en mi lista.

Índices de la lista de ejemplo:
    posición:   Manzana  Plátano  Frutilla  Mango  Cereza
    índice +:      0        1        2        3      4
    índice -:     -5       -4       -3       -2     -1
-------------------------------------------------------------------------------
"""

# 1. Crear una lista de frutas favoritas
frutas_favoritas = ["Manzana", "Plátano", "Frutilla", "Mango", "Cereza"]

# 2. Imprimir la lista completa
print("Mis frutas favoritas son:", frutas_favoritas)
print("-----------------------------------------")

# 3. Imprimir la primera fruta
# Los índices de las listas comienzan en 0
primera_fruta = frutas_favoritas[0]
print(f"La primera fruta de la lista es: {primera_fruta}")

# 4. Imprimir la tercera fruta
# El tercer elemento tiene índice 2
tercera_fruta = frutas_favoritas[2]
print(f"La tercera fruta de la lista es: {tercera_fruta}")

# 5. Imprimir la última fruta
# El índice -1 se refiere al último elemento, -2 al penúltimo, y así sucesivamente.
ultima_fruta = frutas_favoritas[-1]
print(f"La última fruta de la lista es: {ultima_fruta}")
print("-----------------------------------------")

# 6. Imprimir la cantidad de frutas en la lista
cantidad_frutas = len(frutas_favoritas)
print(f"Tengo {cantidad_frutas} frutas favoritas en mi lista.")

# Intento de acceso a un índice que no existe (esto generaría un error)
# print(frutas_favoritas[10]) # Descomenta esta línea para ver el error IndexError

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  ¿Cuál es el índice del primer elemento en una lista de Python? ¿Y del quinto?
2.  Si una lista tiene `N` elementos, ¿cuál es el índice del último elemento
    usando numeración positiva? ¿Y usando numeración negativa?
3.  ¿Qué sucede si intentas acceder a un elemento de la lista usando un índice
    que está fuera del rango válido (por ejemplo, en una lista de 5 elementos,
    intentas acceder al índice 5 o al índice -6)?
4.  Crea una lista con diferentes tipos de datos (números, cadenas, booleanos).
    ¿Es esto posible en Python? Imprímela para verificar.
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
    # Calcular el índice del último elemento con len() en vez de usar -1.
    # El último índice siempre es len(lista) - 1 (si hay 5 elementos, es el 4).
    # Conviene: cuando necesitas ese número de índice para otra cosa. Para solo
    # leer el último elemento, `lista[-1]` es más corto y más claro.
    frutas_favoritas = ["Manzana", "Plátano", "Frutilla", "Mango", "Cereza"]
    cantidad_frutas = len(frutas_favoritas)
    print("Mis frutas favoritas son:", frutas_favoritas)
    print("-----------------------------------------")
    print(f"La primera fruta de la lista es: {frutas_favoritas[0]}")
    print(f"La tercera fruta de la lista es: {frutas_favoritas[2]}")
    print(f"La última fruta de la lista es: {frutas_favoritas[cantidad_frutas - 1]}")
    print("-----------------------------------------")
    print(f"Tengo {cantidad_frutas} frutas favoritas en mi lista.")


def alternativa_2():
    # Crear la lista a partir de un texto con .split(",").
    # .split(",") corta el texto en cada coma y entrega una lista con los pedazos.
    # Conviene: cuando los datos ya vienen en un solo texto (por ejemplo, lo que el
    # usuario escribe con input() separado por comas). Para pocas frutas fijas,
    # escribir la lista directo es más claro.
    frutas_favoritas = "Manzana,Plátano,Frutilla,Mango,Cereza".split(",")
    print("Mis frutas favoritas son:", frutas_favoritas)
    print("-----------------------------------------")
    print(f"La primera fruta de la lista es: {frutas_favoritas[0]}")
    print(f"La tercera fruta de la lista es: {frutas_favoritas[2]}")
    print(f"La última fruta de la lista es: {frutas_favoritas[-1]}")
    print("-----------------------------------------")
    print(f"Tengo {len(frutas_favoritas)} frutas favoritas en mi lista.")


def alternativa_3():
    # Asignar cada elemento a su propia variable ("desempaquetar" la lista).
    # Funciona solo si la cantidad de variables coincide con la de elementos.
    # Conviene: cuando la lista es corta y de largo conocido y quieres darle nombre
    # a cada posición. Si el largo cambia, da error: ahí usa índices.
    frutas_favoritas = ["Manzana", "Plátano", "Frutilla", "Mango", "Cereza"]
    primera, segunda, tercera, cuarta, quinta = frutas_favoritas
    print("Mis frutas favoritas son:", frutas_favoritas)
    print("-----------------------------------------")
    print(f"La primera fruta de la lista es: {primera}")
    print(f"La tercera fruta de la lista es: {tercera}")
    print(f"La última fruta de la lista es: {quinta}")
    print("-----------------------------------------")
    print(f"Tengo {len(frutas_favoritas)} frutas favoritas en mi lista.")


# alternativa_1()
# alternativa_2()
# alternativa_3()
