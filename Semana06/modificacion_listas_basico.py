"""
-------------------------------------------------------------------------------
                                  EJERCICIO 02
                         Modificación Básica de Listas
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Este ejercicio explora cómo modificar listas existentes utilizando métodos
básicos y asignación por índice.

1.  Crea una lista llamada `tareas_pendientes` con 3 tareas (strings).
    Ej: ["Lavar la loza", "Estudiar Python", "Hacer ejercicio"]
2.  Imprime la lista inicial.
3.  Supongamos que ya completaste la segunda tarea. Modifica el segundo
    elemento de la lista para que ahora diga (por ejemplo)
    "Estudiar Python (Completado)". Imprime la lista.
4.  Agrega una nueva tarea al FINAL de la lista usando el método `append()`.
    Ej: "Comprar pan". Imprime la lista.
5.  Agrega una tarea urgente al INICIO de la lista usando el método `insert()`.
    Ej: "Pasear al perro". Imprime la lista.
6.  Elimina la última tarea de la lista usando el método `pop()` e imprime
    la tarea eliminada y la lista resultante.
7.  Supongamos que quieres eliminar "Lavar la loza" (o la primera tarea que
    pusiste) por su valor. Usa el método `remove()`. Imprime la lista.

## OBJETIVO:
## ---------
Modificar una lista: cambiar un elemento por su índice, agregar con
`append()` e `insert()`, y quitar con `pop()` y `remove()`.

## ENTRADA:
## --------
Ninguna: todo está escrito en el código.

## SALIDA ESPERADA (la lista cambia paso a paso):
## ----------------------------------------------
Lista de tareas inicial: ['Lavar la loza', 'Estudiar Python', 'Hacer ejercicio']
Tarea modificada: ['Lavar la loza', 'Estudiar Python (Completado)', 'Hacer ejercicio']
Después de append('Comprar pan'): [..., 'Hacer ejercicio', 'Comprar pan']
Después de insert(0, 'Pasear al perro'): ['Pasear al perro', 'Lavar la loza', ...]
Tarea eliminada con pop(): 'Comprar pan'
Después de remove('Lavar la loza'):
    ['Pasear al perro', 'Estudiar Python (Completado)', 'Hacer ejercicio']
-------------------------------------------------------------------------------
"""

# 1. Crear lista de tareas pendientes
tareas_pendientes = ["Lavar la loza", "Estudiar Python", "Hacer ejercicio"]

# 2. Imprimir lista inicial
print("Lista de tareas inicial:", tareas_pendientes)
print("-----------------------------------------")

# 3. Modificar el segundo elemento (índice 1)
tareas_pendientes[1] = "Estudiar Python (Completado)"
print("Tarea modificada:", tareas_pendientes)
print("-----------------------------------------")

# 4. Agregar una nueva tarea al final con append()
tareas_pendientes.append("Comprar pan")
print("Después de append('Comprar pan'):", tareas_pendientes)
print("-----------------------------------------")

# 5. Agregar una tarea al inicio con insert()
# insert(indice, elemento)
tareas_pendientes.insert(0, "Pasear al perro")
print("Después de insert(0, 'Pasear al perro'):", tareas_pendientes)
print("-----------------------------------------")

# 6. Eliminar la última tarea con pop()
# pop() sin argumento elimina y devuelve el último elemento.
tarea_eliminada_pop = tareas_pendientes.pop()
print(f"Tarea eliminada con pop(): '{tarea_eliminada_pop}'")
print("Lista después de pop():", tareas_pendientes)
print("-----------------------------------------")

# 7. Eliminar una tarea específica por su valor con remove()
# remove() busca y elimina la primera ocurrencia del valor especificado.
# Si el elemento no existe, genera un ValueError.
tarea_a_remover = "Lavar la loza"
if tarea_a_remover in tareas_pendientes:
    tareas_pendientes.remove(tarea_a_remover)
    print(f"Después de remove('{tarea_a_remover}'):", tareas_pendientes)
else:
    print(f"La tarea '{tarea_a_remover}' no se encontró en la lista.")
print("-----------------------------------------")

print("Lista de tareas final:", tareas_pendientes)

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  ¿Cuál es la diferencia entre `append()` e `insert()` al agregar elementos
    a una lista?
2.  El método `pop()` puede usarse con o sin un índice. ¿Qué hace en cada caso?
    ¿Devuelve algún valor?
3.  ¿Qué sucede si intentas usar `remove()` para eliminar un elemento que no
    existe en la lista? ¿Cómo podrías evitar un error en ese caso?
4.  Si tienes una lista `mi_lista = [10, 20, 30, 20]` y ejecutas
    `mi_lista.remove(20)`, ¿cómo quedaría `mi_lista`? ¿Por qué?
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
    # Mismos cambios sin usar los métodos: con `+` (unir listas) y con `del`.
    #   lista + [x]    -> crea una lista nueva con x al final (como append).
    #   [x] + lista    -> crea una lista nueva con x al inicio (como insert(0, x)).
    #   del lista[-1]  -> borra el último elemento (como pop(), pero NO lo devuelve,
    #                     por eso lo guardamos antes).
    # Conviene: para entender que un método es una forma cómoda de hacer algo que
    # también puedes lograr con operadores. En la práctica, append/insert/pop son
    # mejores: modifican la lista en el lugar y no crean copias.
    tareas_pendientes = ["Lavar la loza", "Estudiar Python", "Hacer ejercicio"]
    print("Lista de tareas inicial:", tareas_pendientes)
    print("-----------------------------------------")

    tareas_pendientes[1] = "Estudiar Python (Completado)"
    print("Tarea modificada:", tareas_pendientes)
    print("-----------------------------------------")

    tareas_pendientes = tareas_pendientes + ["Comprar pan"]
    print("Después de append('Comprar pan'):", tareas_pendientes)
    print("-----------------------------------------")

    tareas_pendientes = ["Pasear al perro"] + tareas_pendientes
    print("Después de insert(0, 'Pasear al perro'):", tareas_pendientes)
    print("-----------------------------------------")

    tarea_eliminada_pop = tareas_pendientes[-1]
    del tareas_pendientes[-1]
    print(f"Tarea eliminada con pop(): '{tarea_eliminada_pop}'")
    print("Lista después de pop():", tareas_pendientes)
    print("-----------------------------------------")

    tarea_a_remover = "Lavar la loza"
    if tarea_a_remover in tareas_pendientes:
        del tareas_pendientes[tareas_pendientes.index(tarea_a_remover)]
        print(f"Después de remove('{tarea_a_remover}'):", tareas_pendientes)
    else:
        print(f"La tarea '{tarea_a_remover}' no se encontró en la lista.")
    print("-----------------------------------------")
    print("Lista de tareas final:", tareas_pendientes)


def alternativa_2():
    # Proteger remove() con try / except en vez de preguntar antes con `in`.
    #   try:    intenta hacer algo que podría fallar.
    #   except: si falla con ese error, ejecuta esto en lugar de detener el programa.
    # Conviene: cuando es más natural "intentar y, si no resulta, avisar". La versión
    # con `in` (la principal) es más fácil de leer cuando recién aprendes.
    tareas_pendientes = ["Lavar la loza", "Estudiar Python", "Hacer ejercicio"]
    print("Lista de tareas inicial:", tareas_pendientes)
    print("-----------------------------------------")

    tareas_pendientes[1] = "Estudiar Python (Completado)"
    print("Tarea modificada:", tareas_pendientes)
    print("-----------------------------------------")

    tareas_pendientes.append("Comprar pan")
    print("Después de append('Comprar pan'):", tareas_pendientes)
    print("-----------------------------------------")

    tareas_pendientes.insert(0, "Pasear al perro")
    print("Después de insert(0, 'Pasear al perro'):", tareas_pendientes)
    print("-----------------------------------------")

    tarea_eliminada_pop = tareas_pendientes.pop()
    print(f"Tarea eliminada con pop(): '{tarea_eliminada_pop}'")
    print("Lista después de pop():", tareas_pendientes)
    print("-----------------------------------------")

    tarea_a_remover = "Lavar la loza"
    try:
        tareas_pendientes.remove(tarea_a_remover)
        print(f"Después de remove('{tarea_a_remover}'):", tareas_pendientes)
    except ValueError:
        print(f"La tarea '{tarea_a_remover}' no se encontró en la lista.")
    print("-----------------------------------------")
    print("Lista de tareas final:", tareas_pendientes)


# alternativa_1()
# alternativa_2()
