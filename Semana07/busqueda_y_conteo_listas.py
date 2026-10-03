"""
-------------------------------------------------------------------------------
                                  EJERCICIO 02
                          Búsqueda y Conteo en Listas
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Este ejercicio se centra en encontrar elementos y contar sus ocurrencias
dentro de una lista.

1.  Crea una lista de nombres donde algunos nombres se repitan. Por ejemplo:
    `invitados = ["Ana", "Luis", "Sofia", "Ana", "Carlos", "Ana", "Pedro"]`
2.  Imprime la lista de invitados.
3.  Pregunta al usuario qué nombre desea buscar en la lista de invitados.
4.  Utiliza el método `count()` para determinar cuántas veces aparece el
    nombre ingresado en la lista. Imprime este conteo.
5.  Si el nombre aparece al menos una vez (es decir, su conteo es > 0):
    a. Utiliza el método `index()` para encontrar el índice de la PRIMERA
       aparición del nombre en la lista. Imprime este índice.
    b. (Opcional) Explica verbalmente o con pseudocódigo cómo encontrarías
       TODOS los índices donde aparece el nombre, no solo el primero.
6.  Si el nombre no aparece en la lista, informa al usuario.

## OBJETIVO:
## ---------
Buscar y contar elementos con `count()` e `index()`, y recorrer una lista
con `range(len(...))` para juntar todas las posiciones de un valor.

## ENTRADA:
## --------
Un nombre (texto). Ojo: se distingue entre mayúsculas y minúsculas ("ana" no es "Ana").

## SALIDA ESPERADA (ejemplo de ejecución, buscando "Ana"):
## -------------------------------------------------------
Lista de invitados: ['Ana', 'Luis', 'Sofia', 'Ana', 'Carlos', 'Ana', 'Pedro']
-----------------------------------------
Ingresa el nombre que deseas buscar en la lista: Ana
El nombre 'Ana' aparece 3 vez/veces en la lista.
-----------------------------------------
La primera aparición de 'Ana' está en el índice: 0

Buscando todos los índices para: Ana
'Ana' se encuentra en los siguientes índices: [0, 3, 5]
-----------------------------------------

Si buscas un nombre que no está (por ejemplo "Zoe"):
El nombre 'Zoe' no se encuentra en la lista de invitados.
-------------------------------------------------------------------------------
"""

# 1. Crear lista de invitados con nombres repetidos
invitados = ["Ana", "Luis", "Sofia", "Ana", "Carlos", "Ana", "Pedro"]

# 2. Imprimir la lista
print("Lista de invitados:", invitados)
print("-----------------------------------------")

# 3. Preguntar al usuario qué nombre buscar
nombre_a_buscar = input("Ingresa el nombre que deseas buscar en la lista: ")

# 4. Usar count() para determinar cuántas veces aparece (devuelve 0 si no está)
conteo = invitados.count(nombre_a_buscar)
print(f"El nombre '{nombre_a_buscar}' aparece {conteo} vez/veces en la lista.")
print("-----------------------------------------")

# 5. Si el nombre aparece al menos una vez
if conteo > 0:
    # 5a. Usar index() para encontrar la primera aparición
    try:
        primer_indice = invitados.index(nombre_a_buscar)
        print(f"La primera aparición de '{nombre_a_buscar}' está en el índice: {primer_indice}")
    except ValueError:
        # Esto no debería ocurrir si conteo > 0, pero es buena práctica en general.
        print(f"Hubo un error inesperado al buscar el índice de '{nombre_a_buscar}'.")

    # 5b. (Opcional) Encontrar todos los índices
    print("\nBuscando todos los índices para:", nombre_a_buscar)
    indices_encontrados = []
    for i in range(len(invitados)):
        if invitados[i] == nombre_a_buscar:
            indices_encontrados.append(i)

    if indices_encontrados:
        print(f"'{nombre_a_buscar}' se encuentra en los siguientes índices: {indices_encontrados}")
    else: # Caso poco probable si conteo > 0, pero para completar la lógica
        print("No se encontraron más apariciones (esto es inesperado si el conteo fue > 0).")

else:
    # 6. Si el nombre no aparece
    print(f"El nombre '{nombre_a_buscar}' no se encuentra en la lista de invitados.")

print("-----------------------------------------")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  ¿Qué hace el método `count()` de las listas? ¿Qué tipo de valor devuelve?
2.  El método `index()` devuelve el índice de la primera ocurrencia de un elemento.
    ¿Qué sucede si intentas usar `index()` para buscar un elemento que NO está
    en la lista? ¿Cómo se llama el error que se produce?
3.  En la solución opcional para encontrar todos los índices, se usó un bucle `for`
    con `range(len(invitados))`. ¿Por qué se usa `len()` aquí? ¿Qué valores toma `i`?
4.  ¿Podrías usar el método `extend()` para agregar otra lista de invitados
    a la lista `invitados` existente? Crea una pequeña lista nueva y pruébalo.
    ¿Cuál es la diferencia entre `append()` y `extend()`?
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
    # `in` para saber SI está, en vez de preguntar si count() es mayor que 0.
    #   nombre in lista  -> True si el nombre aparece al menos una vez.
    # Conviene: cuando solo quieres saber si existe. Si además necesitas cuántas
    # veces aparece, count() ya te lo dice. Se quita también el try/except: si `in`
    # dio True, index() no puede fallar.
    invitados = ["Ana", "Luis", "Sofia", "Ana", "Carlos", "Ana", "Pedro"]
    print("Lista de invitados:", invitados)
    print("-----------------------------------------")
    nombre_a_buscar = input("Ingresa el nombre que deseas buscar en la lista: ")
    conteo = invitados.count(nombre_a_buscar)
    print(f"El nombre '{nombre_a_buscar}' aparece {conteo} vez/veces en la lista.")
    print("-----------------------------------------")

    if nombre_a_buscar in invitados:
        primer_indice = invitados.index(nombre_a_buscar)
        print(f"La primera aparición de '{nombre_a_buscar}' está en el índice: {primer_indice}")
        print("\nBuscando todos los índices para:", nombre_a_buscar)
        indices_encontrados = []
        for i in range(len(invitados)):
            if invitados[i] == nombre_a_buscar:
                indices_encontrados.append(i)
        print(f"'{nombre_a_buscar}' se encuentra en los siguientes índices: {indices_encontrados}")
    else:
        print(f"El nombre '{nombre_a_buscar}' no se encuentra en la lista de invitados.")
    print("-----------------------------------------")


def alternativa_2():
    # Todos los índices en una línea con una comprensión de listas y enumerate().
    #   enumerate(lista)  entrega pares (posición, valor).
    #   [i for i, n in enumerate(lista) if n == nombre]  arma la lista de posiciones.
    # Conviene: cuando ya te acomodas con el bucle `for` de la solución principal y
    # quieres lo mismo más corto. Es equivalente al for + append de la solución.
    invitados = ["Ana", "Luis", "Sofia", "Ana", "Carlos", "Ana", "Pedro"]
    print("Lista de invitados:", invitados)
    print("-----------------------------------------")
    nombre_a_buscar = input("Ingresa el nombre que deseas buscar en la lista: ")
    conteo = invitados.count(nombre_a_buscar)
    print(f"El nombre '{nombre_a_buscar}' aparece {conteo} vez/veces en la lista.")
    print("-----------------------------------------")

    indices_encontrados = [i for i, nombre in enumerate(invitados) if nombre == nombre_a_buscar]
    if indices_encontrados:   # lista con elementos = True; vacía = False
        print(f"La primera aparición de '{nombre_a_buscar}' está en el índice: {indices_encontrados[0]}")
        print("\nBuscando todos los índices para:", nombre_a_buscar)
        print(f"'{nombre_a_buscar}' se encuentra en los siguientes índices: {indices_encontrados}")
    else:
        print(f"El nombre '{nombre_a_buscar}' no se encuentra en la lista de invitados.")
    print("-----------------------------------------")


def alternativa_3():
    # Búsqueda "a mano" con un bucle: contar, y quedarse con la primera posición.
    # `break` detiene el bucle, pero aquí NO lo usamos porque también necesitamos contar
    # todas las apariciones; la primera posición se guarda solo la primera vez.
    # Conviene: para entender qué hacen count() e index() por dentro, o cuando la
    # condición de búsqueda es más compleja que "ser igual a" (ej.: empieza con "A").
    invitados = ["Ana", "Luis", "Sofia", "Ana", "Carlos", "Ana", "Pedro"]
    print("Lista de invitados:", invitados)
    print("-----------------------------------------")
    nombre_a_buscar = input("Ingresa el nombre que deseas buscar en la lista: ")

    conteo = 0
    primer_indice = -1          # -1 significa "todavía no lo encontré"
    indices_encontrados = []
    for i in range(len(invitados)):
        if invitados[i] == nombre_a_buscar:
            conteo += 1
            indices_encontrados.append(i)
            if primer_indice == -1:
                primer_indice = i
    print(f"El nombre '{nombre_a_buscar}' aparece {conteo} vez/veces en la lista.")
    print("-----------------------------------------")

    if conteo > 0:
        print(f"La primera aparición de '{nombre_a_buscar}' está en el índice: {primer_indice}")
        print("\nBuscando todos los índices para:", nombre_a_buscar)
        print(f"'{nombre_a_buscar}' se encuentra en los siguientes índices: {indices_encontrados}")
    else:
        print(f"El nombre '{nombre_a_buscar}' no se encuentra en la lista de invitados.")
    print("-----------------------------------------")


# alternativa_1()
# alternativa_2()
# alternativa_3()
