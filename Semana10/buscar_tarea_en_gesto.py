"""
-------------------------------------------------------------------------------
                                  PROYECTO 02
                  Extensión: Buscar Tarea en Gestor de Tareas
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Este ejercicio es una extensión del "Gestor de Tareas Simple".
Se te pide agregar una nueva funcionalidad: buscar tareas por una palabra clave.

1.  Define una nueva función llamada `buscar_tareas_por_palabra(tareas, palabra_clave)`:
    a.  Debe recibir la lista de `tareas` y una `palabra_clave` (string) como parámetros.
    b.  Debe crear una nueva lista (ej: `encontradas`) que contenga todas las tareas
        cuya descripción contenga la `palabra_clave` (sin importar mayúsculas/minúsculas).
    c.  Si se encuentran tareas, la función debe imprimir estas tareas encontradas
        (puedes reutilizar o adaptar parte de la lógica de `ver_tareas` para mostrarlas).
    d.  Si no se encuentra ninguna tarea que coincida, debe imprimir un mensaje indicándolo.
    e.  Esta función NO debe modificar la lista original de tareas.

2.  Modifica la función `main()` y `mostrar_menu()` del "Gestor de Tareas Simple"
    para incluir esta nueva opción (por ejemplo, "Buscar tarea").
3.  Cuando el usuario elija la opción de buscar, el programa debe solicitarle
    la palabra clave y luego llamar a la función `buscar_tareas_por_palabra()`.

## OBJETIVO:
## ---------
Extender un programa que ya funciona sin romperlo: agregar una función nueva,
una opción al menú y reutilizar código existente. Aquí, la búsqueda ignora
mayúsculas/minúsculas y encuentra la palabra aunque sea parte de otra más larga.

## ENTRADA:
## --------
Opciones del menú (1 a 6) y, al buscar, una palabra clave.

## SALIDA ESPERADA (ejemplo: opción 5 y palabra "python", con las 4 tareas de ejemplo):
## ------------------------------------------------------------------------------------
Selecciona una opción (1-6): 5
Ingresa la palabra clave para buscar en las tareas: python

Resultados para 'python':
1. Preparar presentación de Python - [Pendiente]
2. Leer capítulo 5 del libro de Python - [Pendiente]
---------------------------------

Si no hay coincidencias:
No se encontraron tareas que contengan la palabra clave 'xyz'.

NOTA: este archivo ya incluye las funciones del Proyecto 01 (agregar, ver, marcar
y eliminar), así que se puede ejecutar solo, sin copiar nada desde otro archivo.
-------------------------------------------------------------------------------
"""

# Lista de tareas. Parte con cuatro tareas de ejemplo para probar la búsqueda;
# borra los elementos si prefieres empezar con la lista vacía: lista_de_tareas = []
lista_de_tareas = [
    {"descripcion": "Comprar leche y pan", "completada": False},
    {"descripcion": "Preparar presentación de Python", "completada": False},
    {"descripcion": "Llamar al electricista", "completada": True},
    {"descripcion": "Leer capítulo 5 del libro de Python", "completada": False},
]


def mostrar_menu_extendido():  # Nombre modificado para la nueva versión
    """Muestra el menú de opciones al usuario, incluyendo buscar."""
    print("\n--- Gestor de Tareas Extendido ---")
    print("1. Agregar nueva tarea")
    print("2. Ver todas las tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Buscar tarea por palabra clave")  # Nueva opción
    print("6. Salir")                           # Salir pasa a ser la opción 6
    print("----------------------------------")


# --- Funciones del Proyecto 01 (copiadas para que este archivo funcione solo) ---
def ver_tareas_filtradas(tareas, titulo="--- Lista de Tareas ---",
                         mensaje_vacio="¡No hay tareas que coincidan con los criterios!"):
    """
    Muestra una lista de tareas con su número y estado.

    Sirve tanto para mostrar TODAS las tareas como para mostrar solo las
    que resultaron de una búsqueda.

    Returns:
        bool: True si se imprimió alguna tarea, False si la lista estaba vacía.
    """
    print(f"\n{titulo}")
    if not tareas:
        print(mensaje_vacio)
        return False

    for indice, tarea in enumerate(tareas):
        estado = "Completada" if tarea["completada"] else "Pendiente"
        # En una lista filtrada el número es de esta lista, no de la lista completa.
        print(f"{indice + 1}. {tarea['descripcion']} - [{estado}]")
    print("---------------------------------")
    return True


def ver_todas_las_tareas(tareas):
    """Muestra todas las tareas (reutiliza ver_tareas_filtradas)."""
    ver_tareas_filtradas(tareas, "--- Lista de Tareas Pendientes ---",
                         "¡No hay tareas en la lista! Puedes agregar algunas.")


def agregar_tarea(tareas):
    """Solicita la descripción de una nueva tarea y la agrega a la lista."""
    descripcion = input("Introduce la descripción de la nueva tarea: ")
    if descripcion:  # Asegurarse de que no esté vacía
        tareas.append({"descripcion": descripcion, "completada": False})
        print(f"Tarea '{descripcion}' agregada con éxito.")
    else:
        print("La descripción de la tarea no puede estar vacía.")


def marcar_tarea_completa(tareas):
    """Permite al usuario marcar una tarea como completada por su número."""
    ver_todas_las_tareas(tareas)
    if not tareas:
        return

    try:
        num_tarea = int(input("Ingresa el número de la tarea a marcar como completada: "))
        indice_real = num_tarea - 1  # Convertir a índice de lista (base 0)

        if 0 <= indice_real < len(tareas):
            if not tareas[indice_real]["completada"]:
                tareas[indice_real]["completada"] = True
                print(f"Tarea '{tareas[indice_real]['descripcion']}' marcada como completada.")
            else:
                print(f"La tarea '{tareas[indice_real]['descripcion']}' ya estaba completada.")
        else:
            print("Número de tarea inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número.")


def eliminar_tarea(tareas):
    """Permite al usuario eliminar una tarea por su número."""
    ver_todas_las_tareas(tareas)
    if not tareas:
        return

    try:
        num_tarea = int(input("Ingresa el número de la tarea a eliminar: "))
        indice_real = num_tarea - 1

        if 0 <= indice_real < len(tareas):
            tarea_eliminada = tareas.pop(indice_real)
            print(f"Tarea '{tarea_eliminada['descripcion']}' eliminada con éxito.")
        else:
            print("Número de tarea inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número.")


# --- 1. Nueva función para buscar tareas ---
def buscar_tareas_por_palabra(tareas, palabra_clave):
    """
    Busca tareas que contengan una palabra clave en su descripción.

    No modifica la lista original: arma una lista nueva con las coincidencias.

    Args:
        tareas (list): La lista completa de tareas.
        palabra_clave (str): La palabra a buscar en las descripciones.
    """
    if not palabra_clave.strip():  # .strip() quita espacios: "   " cuenta como vacía
        print("La palabra clave para buscar no puede estar vacía.")
        return

    encontradas = []
    palabra_en_minusculas = palabra_clave.lower()  # Para que no importen las mayúsculas

    for tarea in tareas:
        # `in` entre textos pregunta "¿está este texto dentro del otro?"
        if palabra_en_minusculas in tarea["descripcion"].lower():
            encontradas.append(tarea)

    # c. / d. Mostrar resultados o avisar que no hay
    if encontradas:
        ver_tareas_filtradas(encontradas, f"Resultados para '{palabra_clave}':")
    else:
        print(f"No se encontraron tareas que contengan la palabra clave '{palabra_clave}'.")


# --- Bucle Principal de la Aplicación (modificado) ---
def main_extendido():  # Nombre modificado para la nueva versión
    """Función principal que ejecuta el gestor de tareas extendido."""
    opcion = ""

    while opcion != "6":  # Salir ahora es la opción 6
        mostrar_menu_extendido()
        opcion = input("Selecciona una opción (1-6): ")

        if opcion == "1":
            agregar_tarea(lista_de_tareas)
        elif opcion == "2":
            ver_todas_las_tareas(lista_de_tareas)
        elif opcion == "3":
            marcar_tarea_completa(lista_de_tareas)
        elif opcion == "4":
            eliminar_tarea(lista_de_tareas)
        elif opcion == "5":  # Nueva opción
            palabra_clave_buscar = input("Ingresa la palabra clave para buscar en las tareas: ")
            buscar_tareas_por_palabra(lista_de_tareas, palabra_clave_buscar)
        elif opcion == "6":
            print("Saliendo del Gestor de Tareas Extendido. ¡Hasta pronto!")
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar la aplicación extendida (solo si se ejecuta este archivo directamente)
if __name__ == "__main__":
    main_extendido()


"""
-------------------------------------------------------------------------------
## PUNTOS CLAVE Y PREGUNTAS GUÍA:
## --------------------------------
1.  **Reutilización y Adaptación:** ¿Cómo se podría reutilizar la función
    `ver_tareas` (o una versión modificada de ella) para mostrar los resultados
    de la búsqueda sin duplicar mucho código? (La solución usa `ver_tareas_filtradas`).
2.  **Búsqueda Case-Insensitive:** En la función `buscar_tareas_por_palabra`,
    ¿cómo se logra que la búsqueda no distinga entre mayúsculas y minúsculas
    tanto en la palabra clave como en la descripción de la tarea?
3.  **Lista de Resultados:** La función de búsqueda crea una nueva lista `encontradas`.
    ¿Por qué es esto una buena práctica en lugar de, por ejemplo, modificar
    directamente la lista original o solo imprimir los hallazgos?
4.  **Integración:** ¿Qué cambios fueron necesarios en `mostrar_menu()` y en el
    bucle `while` principal de `main()` para incorporar esta nueva funcionalidad?
5.  **Pruebas:** ¿Qué casos de prueba considerarías para la función de búsqueda
    (ej: palabra clave existe, no existe, palabra clave vacía, mayúsculas/minúsculas,
    palabra clave es parte de una palabra más larga en la descripción)?
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
    # Comprensión de listas: arma `encontradas` en una sola expresión.
    #   [t for t in tareas if condicion]  -> lista con los t que cumplen la condición.
    # Hace exactamente lo mismo que el for + append de la solución.
    # Conviene: cuando ya te acomodas con el for + append y quieres la versión corta.
    def buscar_con_comprension(tareas, palabra_clave):
        if not palabra_clave.strip():
            print("La palabra clave para buscar no puede estar vacía.")
            return
        palabra = palabra_clave.lower()
        encontradas = [t for t in tareas if palabra in t["descripcion"].lower()]
        if encontradas:
            ver_tareas_filtradas(encontradas, f"Resultados para '{palabra_clave}':")
        else:
            print(f"No se encontraron tareas que contengan la palabra clave '{palabra_clave}'.")

    buscar_con_comprension(lista_de_tareas, "PYTHON")
    buscar_tareas_por_palabra(lista_de_tareas, "PYTHON")   # la solución: misma salida


def alternativa_2():
    # .find() en lugar de `in`: entrega la posición donde empieza la palabra, o -1 si no está.
    #   "pan" in "Comprar pan"          -> True
    #   "Comprar pan".find("pan") != -1 -> True (equivalente)
    # Conviene: cuando además de saber si está necesitas DÓNDE aparece. Si solo
    # quieres saber si está, `in` es más claro.
    def buscar_con_find(tareas, palabra_clave):
        if not palabra_clave.strip():
            print("La palabra clave para buscar no puede estar vacía.")
            return
        encontradas = []
        for tarea in tareas:
            if tarea["descripcion"].lower().find(palabra_clave.lower()) != -1:
                encontradas.append(tarea)
        if encontradas:
            ver_tareas_filtradas(encontradas, f"Resultados para '{palabra_clave}':")
        else:
            print(f"No se encontraron tareas que contengan la palabra clave '{palabra_clave}'.")

    buscar_con_find(lista_de_tareas, "pan")
    buscar_tareas_por_palabra(lista_de_tareas, "pan")      # la solución: misma salida


# alternativa_1()
# alternativa_2()
