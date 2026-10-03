"""
-------------------------------------------------------------------------------
                                  EJERCICIO 02
                Argumentos por Palabra Clave (Keyword Arguments)
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Este ejercicio se enfoca en cómo llamar a funciones utilizando argumentos
por palabra clave, lo que puede hacer que las llamadas a funciones con muchos
parámetros sean más claras y flexibles.

1.  Define una función llamada `crear_perfil_usuario(nombre, email, edad, pais="Chile")`:
    a. `nombre`, `email`, `edad` son parámetros posicionales.
    b. `pais` es un parámetro con un valor por defecto.
    c. La función debe imprimir los detalles del perfil del usuario.

2.  Llama a la función `crear_perfil_usuario` de las siguientes maneras:
    a. Usando solo argumentos posicionales para `nombre`, `email` y `edad`.
    b. Usando argumentos por palabra clave para todos los parámetros,
       incluido `pais`, y en un orden diferente al de la definición
       (ej: `email` primero, luego `pais`, etc.).
    c. Usando una mezcla: los primeros dos argumentos (`nombre`, `email`)
       como posicionales y los siguientes (`edad`, `pais`) como argumentos
       por palabra clave.
    d. Intenta llamar a la función proporcionando un argumento por palabra clave
       antes de un argumento posicional (ej: `crear_perfil_usuario(nombre="Ana", "ana@mail.com", edad=30)`).
       Observa y explica el error.

## OBJETIVO:
## ---------
Llamar funciones por posición o por nombre (`parametro=valor`), mezclar
ambas formas respetando la regla de orden, y entender el error que se
produce al romperla.

## ENTRADA:
## --------
Ninguna: todos los valores están escritos en el código.

## SALIDA ESPERADA (extracto de la ejecución):
## -------------------------------------------
--- Perfil de Usuario ---
Nombre: Juan Pérez
Email : juan.perez@example.com
Edad  : 28 años
País  : Chile        <- valor por defecto, porque no se indicó
-------------------------
(... y lo mismo para las otras tres llamadas, y al final el mensaje del error de la llamada 4)
-------------------------------------------------------------------------------
"""

# 1. Definir la función crear_perfil_usuario
def crear_perfil_usuario(nombre, email, edad, pais="Chile"):
    """Crea e imprime un perfil de usuario con los datos proporcionados."""
    print("\n--- Perfil de Usuario ---")
    print(f"Nombre: {nombre}")
    print(f"Email : {email}")
    print(f"Edad  : {edad} años")
    print(f"País  : {pais}")
    print("-------------------------")

print("--- Llamadas a crear_perfil_usuario ---")

# 2a. Usando solo argumentos posicionales
print("\nLlamada 1 (argumentos posicionales):")
crear_perfil_usuario("Juan Pérez", "juan.perez@example.com", 28)

# 2b. Usando argumentos por palabra clave para todos, en orden diferente
print("\nLlamada 2 (argumentos por palabra clave, orden alterado):")
crear_perfil_usuario(
    email="sofia.gomez@example.com",
    pais="México",
    edad=32,
    nombre="Sofía Gómez"
)

# 2c. Mezcla de argumentos posicionales y por palabra clave
# Los argumentos posicionales deben ir ANTES que los de palabra clave.
print("\nLlamada 3 (mezcla de posicionales y por palabra clave):")
crear_perfil_usuario("Carlos Ruiz", "c.ruiz@example.net", edad=45, pais="Argentina")

# 2d. Intento de llamar con palabra clave antes de posicional (esto dará error)
print("\nLlamada 4 (intento de palabra clave antes de posicional):")
# Escribir esta llamada directamente en el archivo haría que Python se negara a
# ejecutar TODO el programa (error de sintaxis antes de empezar):
#     crear_perfil_usuario(nombre="Ana", "ana@mail.com", edad=30)
# Para mostrar el error sin romper el archivo, le pasamos esa línea como texto a
# compile(), que la revisa sin ejecutarla, y capturamos el SyntaxError.
llamada_incorrecta = 'crear_perfil_usuario(nombre="Ana", "ana@mail.com", edad=30)'
try:
    compile(llamada_incorrecta, "<llamada 4>", "exec")
except SyntaxError as e:
    print(f"Python rechaza la llamada: {llamada_incorrecta}")
    print(f"SyntaxError: {e.msg}")
    print("Regla: los argumentos posicionales deben ir ANTES que los de palabra clave.")

print("-----------------------------------------")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  ¿Cuál es la principal ventaja de utilizar argumentos por palabra clave al
    llamar a una función, especialmente si tiene muchos parámetros?
2.  ¿Es obligatorio que los argumentos por palabra clave sigan el mismo orden
    que los parámetros en la definición de la función?
3.  ¿Cuál es la regla respecto al orden de los argumentos posicionales y los
    argumentos por palabra clave en una llamada a función?
4.  Si una función tiene un parámetro con valor por defecto (ej: `pais="Chile"`),
    ¿puedes aun así pasarle un valor usando un argumento por palabra clave
    (ej: `pais="Perú"`)?
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
    # Guardar los datos en un diccionario y pasarlos con `**` al llamar.
    #   **datos  -> Python reparte cada clave del diccionario como un argumento
    #               por palabra clave (nombre=..., email=..., ...).
    # Conviene: cuando los datos ya vienen agrupados (por ejemplo, leídos de un
    # formulario o un archivo) y no quieres escribirlos uno por uno en cada llamada.
    datos = {
        "email": "sofia.gomez@example.com",
        "pais": "México",
        "edad": 32,
        "nombre": "Sofía Gómez",
    }
    crear_perfil_usuario(**datos)   # equivale a la Llamada 2 de la solución


def alternativa_2():
    # Parámetros que SOLO se pueden pasar por palabra clave, usando un `*` suelto.
    #   def f(*, a, b)  -> todo lo que va después del `*` se debe pasar con su nombre.
    # Conviene: funciones con muchos datos del mismo tipo (como estos textos y
    # números), donde pasarlos por posición se presta para confundir el orden.
    def crear_perfil_estricto(*, nombre, email, edad, pais="Chile"):
        print(f"{nombre} | {email} | {edad} años | {pais}")

    crear_perfil_estricto(nombre="Juan Pérez", email="juan.perez@example.com", edad=28)
    try:
        crear_perfil_estricto("Juan Pérez", "juan.perez@example.com", 28)   # sin nombres: error
    except TypeError as e:
        print("TypeError:", e)


# alternativa_1()
# alternativa_2()
