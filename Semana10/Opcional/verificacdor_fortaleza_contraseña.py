"""
-------------------------------------------------------------------------------
                              PROYECTO OPCIONAL 01
                     Verificador de Fortaleza de Contraseña
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Crea una función que analice una contraseña ingresada por el usuario y
determine su fortaleza basada en algunos criterios simples:
- Longitud.
- Presencia de letras mayúsculas.
- Presencia de letras minúsculas.
- Presencia de números.
- Presencia de símbolos especiales.

La función debe retornar un mensaje indicando la fortaleza (ej: "Débil",
"Media", "Fuerte", "Muy Fuerte") y quizás algunas sugerencias.

## OBJETIVO:
## ---------
Recorrer un texto carácter por carácter, llevar un puntaje con condicionales
y construir un mensaje de respuesta que la función RETORNA.

## ENTRADA:
## --------
Una contraseña (texto). El programa prueba además 8 contraseñas de ejemplo.

## SALIDA ESPERADA (ejemplo de ejecución, para 'clave123'):
## --------------------------------------------------------
Analizando contraseña: 'clave123'
Fortaleza de la contraseña: Media. 🤔
Sugerencias para mejorar:
  - Incluir letras mayúsculas.
  - Incluir símbolos (ej: !@#$%).
--------------------

Cómo se calcula el puntaje (máximo 7):
    longitud >= 12: +2   |   longitud >= 8: +1
    minúsculas: +1  |  mayúsculas: +1  |  números: +1  |  símbolos: +2
    puntaje >= 6: Muy Fuerte  |  >= 4: Fuerte  |  >= 2: Media  |  menos: Débil
-------------------------------------------------------------------------------
"""


def verificar_fortaleza_contrasena(contrasena):
    """
    Analiza una contraseña y devuelve un mensaje sobre su fortaleza.

    Args:
        contrasena (str): La contraseña a analizar.

    Returns:
        str: Un mensaje describiendo la fortaleza de la contraseña.
    """
    longitud = len(contrasena)
    tiene_mayusculas = False
    tiene_minusculas = False
    tiene_numeros = False
    tiene_simbolos = False

    # Criterios y puntaje
    puntaje = 0
    sugerencias = []

    # 1. Verificar longitud
    if longitud >= 12:
        puntaje += 2
    elif longitud >= 8:
        puntaje += 1
    else:
        sugerencias.append("Hacerla más larga (mínimo 8 caracteres, idealmente 12+).")

    # Caracteres que contaremos como símbolos (puedes ampliar esta lista).
    # Las letras con tilde o ñ no entran en ningún criterio en esta versión.
    simbolos_especiales = "!@#$%^&*()-_=+[]{};:,.<>/?"

    # 2-5. Verificar tipos de caracteres
    for caracter in contrasena:
        if 'a' <= caracter <= 'z':
            tiene_minusculas = True
        elif 'A' <= caracter <= 'Z':
            tiene_mayusculas = True
        elif '0' <= caracter <= '9':
            tiene_numeros = True
        elif caracter in simbolos_especiales:
            tiene_simbolos = True

    if tiene_minusculas:
        puntaje += 1
    else:
        sugerencias.append("Incluir letras minúsculas.")

    if tiene_mayusculas:
        puntaje += 1
    else:
        sugerencias.append("Incluir letras mayúsculas.")

    if tiene_numeros:
        puntaje += 1
    else:
        sugerencias.append("Incluir números.")

    if tiene_simbolos:
        puntaje += 2  # Los símbolos suelen añadir más fortaleza
    else:
        sugerencias.append("Incluir símbolos (ej: !@#$%).")

    # Determinar fortaleza basada en el puntaje
    # Puntaje máximo posible aquí: 2(long) + 1(min) + 1(may) + 1(num) + 2(sim) = 7
    fortaleza_mensaje = ""
    if puntaje >= 6:  # Requiere buena longitud y varios tipos de caracteres
        fortaleza_mensaje = "¡Muy Fuerte! 👍"
    elif puntaje >= 4:
        fortaleza_mensaje = "Fuerte. 🙂"
    elif puntaje >= 2:
        fortaleza_mensaje = "Media. 🤔"
    else:
        fortaleza_mensaje = "Débil. 😟"

    resultado_final = f"Fortaleza de la contraseña: {fortaleza_mensaje}"
    if sugerencias:
        resultado_final += "\nSugerencias para mejorar:\n"
        for sug in sugerencias:
            resultado_final += f"  - {sug}\n"

    return resultado_final.strip()


# --- Programa Principal para Probar ---
def probar_verificador(verificar):
    """Prueba una función verificadora con varias contraseñas y con una escrita por el usuario."""
    print("--- Verificador de Fortaleza de Contraseña ---")

    contrasenas_prueba = [
        "clave123",  # Media
        "ClaveSegura",  # Media
        "ClaveSuperSegura123!",  # Muy Fuerte
        "abc",  # Débil
        "ABCDEFGHIJKL",  # Media (solo mayúsculas, pero larga)
        "1234567890",  # Media (solo números, pero larga)
        "aB1!cD2@",  # Muy Fuerte (corta pero con todos los tipos)
        "MiClaveSuperLargaConNumeros12345YSimbolos!@#$"  # Muy Fuerte
    ]

    for pwd in contrasenas_prueba:
        print(f"\nAnalizando contraseña: '{pwd}'")
        mensaje_fortaleza = verificar(pwd)
        print(mensaje_fortaleza)
        print("--------------------")

    print("\nPrueba con una contraseña ingresada por el usuario:")
    contrasena_usuario = input("Ingresa una contraseña para verificar su fortaleza: ")
    mensaje_usuario = verificar(contrasena_usuario)
    print(mensaje_usuario)


# Se ejecuta solo si corres este archivo directamente (no al importarlo)
if __name__ == "__main__":
    probar_verificador(verificar_fortaleza_contrasena)

"""
-------------------------------------------------------------------------------
## PUNTOS CLAVE Y PREGUNTAS GUÍA:
## --------------------------------
1.  **Lógica de Puntuación:** ¿Cómo funciona el sistema de "puntaje" para determinar
    la fortaleza? ¿Consideras que los pesos asignados a cada criterio (longitud,
    tipos de caracteres) son adecuados? ¿Cómo los cambiarías?
2.  **Iteración y Verificación de Caracteres:** Explica cómo el bucle `for caracter in contrasena:`
    y las condiciones `if` internas logran identificar la presencia de minúsculas,
    mayúsculas, números y símbolos.
3.  **Manejo de Strings:** ¿Qué métodos de string se utilizan o podrían ser útiles
    aquí (ej: `islower()`, `isupper()`, `isdigit()`) en lugar de las comparaciones
    de rango como `'a' <= caracter <= 'z'`? ¿Cuáles serían las ventajas o desventajas?
4.  **Modularidad:** La lógica principal está dentro de una función. ¿Qué ventajas
    ofrece esto si quisieras usar este verificador en otro programa más grande?
5.  **Sugerencias:** ¿Cómo se generan y presentan las sugerencias al usuario?
    ¿Podrías pensar en otros criterios o sugerencias para añadir (ej: evitar
    palabras comunes, secuencias, etc.)? Esto último sería más avanzado.
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
    # Métodos de texto en vez de comparaciones de rango ('a' <= c <= 'z').
    #   c.islower()  -> True si es letra minúscula     c.isupper() -> mayúscula
    #   c.isdigit()  -> True si es un dígito
    # Conviene: casi siempre; se lee mejor. Ojo: estos métodos también reconocen
    # letras con tilde y la ñ ('á'.islower() es True), mientras que el rango
    # 'a' <= c <= 'z' las ignora. Aquí el resultado es igual con contraseñas sin tildes.
    def verificar_con_metodos(contrasena):
        longitud = len(contrasena)
        puntaje = 0
        sugerencias = []
        simbolos_especiales = "!@#$%^&*()-_=+[]{};:,.<>/?"

        if longitud >= 12:
            puntaje += 2
        elif longitud >= 8:
            puntaje += 1
        else:
            sugerencias.append("Hacerla más larga (mínimo 8 caracteres, idealmente 12+).")

        tiene_minusculas = tiene_mayusculas = tiene_numeros = tiene_simbolos = False
        for caracter in contrasena:
            if caracter.islower():
                tiene_minusculas = True
            elif caracter.isupper():
                tiene_mayusculas = True
            elif caracter.isdigit():
                tiene_numeros = True
            elif caracter in simbolos_especiales:
                tiene_simbolos = True

        if tiene_minusculas:
            puntaje += 1
        else:
            sugerencias.append("Incluir letras minúsculas.")
        if tiene_mayusculas:
            puntaje += 1
        else:
            sugerencias.append("Incluir letras mayúsculas.")
        if tiene_numeros:
            puntaje += 1
        else:
            sugerencias.append("Incluir números.")
        if tiene_simbolos:
            puntaje += 2
        else:
            sugerencias.append("Incluir símbolos (ej: !@#$%).")

        if puntaje >= 6:
            fortaleza_mensaje = "¡Muy Fuerte! 👍"
        elif puntaje >= 4:
            fortaleza_mensaje = "Fuerte. 🙂"
        elif puntaje >= 2:
            fortaleza_mensaje = "Media. 🤔"
        else:
            fortaleza_mensaje = "Débil. 😟"
        resultado_final = f"Fortaleza de la contraseña: {fortaleza_mensaje}"
        if sugerencias:
            resultado_final += "\nSugerencias para mejorar:\n"
            for sug in sugerencias:
                resultado_final += f"  - {sug}\n"
        return resultado_final.strip()

    probar_verificador(verificar_con_metodos)


def alternativa_2():
    # any() con una expresión generadora: "¿se cumple para ALGÚN carácter?".
    #   any(c.isdigit() for c in texto)  -> True si al menos un carácter es dígito.
    # Reemplaza el for con banderas (tiene_numeros = True) por una línea por criterio.
    # Las sugerencias y los puntos se arman con una tabla de criterios (lista de tuplas).
    # Conviene: cuando los criterios son parejos y pueden crecer: agregar uno nuevo
    # es agregar una fila a la tabla (pregunta 5 de comprensión).
    def verificar_con_any(contrasena):
        simbolos_especiales = "!@#$%^&*()-_=+[]{};:,.<>/?"
        puntaje = 0
        sugerencias = []

        if len(contrasena) >= 12:
            puntaje += 2
        elif len(contrasena) >= 8:
            puntaje += 1
        else:
            sugerencias.append("Hacerla más larga (mínimo 8 caracteres, idealmente 12+).")

        criterios = [  # (¿se cumple?, puntos, sugerencia si no se cumple)
            (any(c.islower() for c in contrasena), 1, "Incluir letras minúsculas."),
            (any(c.isupper() for c in contrasena), 1, "Incluir letras mayúsculas."),
            (any(c.isdigit() for c in contrasena), 1, "Incluir números."),
            (any(c in simbolos_especiales for c in contrasena), 2, "Incluir símbolos (ej: !@#$%)."),
        ]
        for se_cumple, puntos, sugerencia in criterios:
            if se_cumple:
                puntaje += puntos
            else:
                sugerencias.append(sugerencia)

        if puntaje >= 6:
            fortaleza_mensaje = "¡Muy Fuerte! 👍"
        elif puntaje >= 4:
            fortaleza_mensaje = "Fuerte. 🙂"
        elif puntaje >= 2:
            fortaleza_mensaje = "Media. 🤔"
        else:
            fortaleza_mensaje = "Débil. 😟"
        resultado_final = f"Fortaleza de la contraseña: {fortaleza_mensaje}"
        if sugerencias:
            resultado_final += "\nSugerencias para mejorar:\n"
            for sug in sugerencias:
                resultado_final += f"  - {sug}\n"
        return resultado_final.strip()

    probar_verificador(verificar_con_any)


# alternativa_1()
# alternativa_2()
