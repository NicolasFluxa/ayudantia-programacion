"""
-------------------------------------------------------------------------------
                                  EJERCICIO 01
           Alcance de Variables y Argumentos por Defecto en Funciones
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Este ejercicio explora cómo funcionan las variables dentro y fuera de las
funciones (alcance) y cómo definir funciones con parámetros que tienen
valores por defecto.

1.  **Alcance de Variables:**
    a. Declara una variable global `mensaje_global = "Soy global"`.
    b. Define una función `probar_alcance()`:
        i.   Dentro de esta función, declara una variable local
             `mensaje_local = "Soy local"`.
        ii.  Imprime `mensaje_local` desde dentro de la función.
        iii. Intenta imprimir `mensaje_global` desde dentro de la función.
    c. Llama a `probar_alcance()`.
    d. Después de llamar a la función, intenta imprimir `mensaje_local`
       fuera de la función. Observa y explica el error (si lo hay).
    e. Intenta imprimir `mensaje_global` fuera de la función.

2.  **Argumentos por Defecto:**
    a. Define una función `configurar_notificacion(mensaje, tipo="informativo", repetir=1)`:
        i.   `mensaje` es un parámetro obligatorio.
        ii.  `tipo` debe tener un valor por defecto "informativo".
        iii. `repetir` debe tener un valor por defecto 1.
        iv.  La función debe imprimir el mensaje, su tipo y cuántas veces se repetirá.
    b. Llama a `configurar_notificacion` de las siguientes maneras:
        i.   Solo con el `mensaje` obligatorio.
        ii.  Con `mensaje` y `tipo`.
        iii. Con `mensaje`, `tipo` y `repetir`.
        iv.  Con `mensaje` y `repetir` (usando argumento de palabra clave para `repetir`).

## OBJETIVO:
## ---------
Distinguir variables locales (viven solo dentro de la función) de globales
(se pueden leer en todo el archivo), y usar parámetros con valor por defecto
para que algunos datos sean opcionales al llamar a la función.

## ENTRADA:
## --------
Ninguna: todos los valores están escritos en el código.

## SALIDA ESPERADA (extracto de la ejecución):
## -------------------------------------------
--- 1. Alcance de Variables ---
Dentro de la función, mensaje_local: 'Soy local y solo existo dentro de probar_alcance().'
Dentro de la función, mensaje_global: 'Soy global y existo fuera de cualquier función.'

Intentando acceder a mensaje_local fuera de la función:
Error: name 'mensaje_local' is not defined. ...

--- 2. Argumentos por Defecto ---
Llamada 1 (solo mensaje):
Notificación:
  Mensaje: 'Actualización del sistema completada.'
  Tipo   : 'informativo'      <- tomó el valor por defecto
  Repetir: 1 vez/veces        <- tomó el valor por defecto
-------------------------------------------------------------------------------
"""

# 1. Alcance de Variables
print("--- 1. Alcance de Variables ---")
mensaje_global = "Soy global y existo fuera de cualquier función." # a. Variable global

def probar_alcance():
    """Demuestra el alcance de variables locales y globales."""
    # b.i. Variable local
    mensaje_local = "Soy local y solo existo dentro de probar_alcance()."
    # b.ii. Imprimir variable local (desde dentro)
    print(f"Dentro de la función, mensaje_local: '{mensaje_local}'")
    # b.iii. Imprimir variable global (desde dentro)
    print(f"Dentro de la función, mensaje_global: '{mensaje_global}'")

# c. Llamar a la función
probar_alcance()

# d. Intentar imprimir mensaje_local fuera de la función
print("\nIntentando acceder a mensaje_local fuera de la función:")
try:
    print(mensaje_local)
except NameError as e:
    print(f"Error: {e}. 'mensaje_local' no está definida fuera de la función.")

# e. Intentar imprimir mensaje_global fuera de la función
print(f"\nFuera de la función, mensaje_global: '{mensaje_global}'")
print("-----------------------------------------")


# 2. Argumentos por Defecto
print("\n--- 2. Argumentos por Defecto ---")
def configurar_notificacion(mensaje, tipo="informativo", repetir=1):
    """Configura y muestra una notificación con tipo y repeticiones opcionales."""
    print("\nNotificación:")
    print(f"  Mensaje: '{mensaje}'")
    print(f"  Tipo   : '{tipo}'")
    print(f"  Repetir: {repetir} vez/veces")

# b.i. Solo con el mensaje obligatorio
print("\nLlamada 1 (solo mensaje):")
configurar_notificacion("Actualización del sistema completada.")

# b.ii. Con mensaje y tipo
print("\nLlamada 2 (mensaje y tipo):")
configurar_notificacion("Error crítico en el servidor.", tipo="urgente")

# b.iii. Con mensaje, tipo y repetir
print("\nLlamada 3 (mensaje, tipo y repetir):")
configurar_notificacion("Recordatorio: reunión a las 10 AM", tipo="recordatorio", repetir=3)

# b.iv. Con mensaje y repetir (usando argumento de palabra clave para repetir).
# Si escribiéramos solo 2, Python lo tomaría como el `tipo` (es el segundo parámetro).
# Con `repetir=2` le decimos a cuál parámetro va, y así nos saltamos `tipo`.
print("\nLlamada 4 (mensaje y repetir, omitiendo tipo):")
configurar_notificacion("Oferta especial solo por hoy.", repetir=2)

print("-----------------------------------------")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  Explica con tus palabras la diferencia entre una variable local y una global.
    ¿Desde dónde se puede acceder a cada una?
2.  ¿Qué sucede si intentas modificar una variable global directamente dentro de
    una función sin usar la palabra clave `global`? (Investiga la palabra clave `global`).
3.  ¿Cuál es la ventaja de usar argumentos por defecto en una función?
4.  En la "Llamada 4" a `configurar_notificacion`, ¿por qué fue necesario usar
    `repetir=2` (argumento por palabra clave) en lugar de solo `2`?
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
    # La función recibe el dato por PARÁMETRO en vez de leer una variable global.
    # Funciona igual, pero la función ya no depende de que exista algo "afuera":
    # se puede probar y reutilizar sola.
    # Conviene: casi siempre. Leer globales dentro de funciones funciona, pero
    # vuelve el programa difícil de seguir cuando crece.
    def probar_alcance(mensaje_recibido):
        mensaje_local = "Soy local y solo existo dentro de probar_alcance()."
        print(f"Dentro de la función, mensaje_local: '{mensaje_local}'")
        print(f"Dentro de la función, mensaje recibido: '{mensaje_recibido}'")

    mensaje = "Soy global y existo fuera de cualquier función."
    probar_alcance(mensaje)    # pasamos el valor como argumento
    try:
        print(mensaje_local)   # sigue sin existir fuera de la función
    except NameError as e:
        print(f"Error: {e}.")


contador_global = 0   # variable global usada solo por la alternativa_2


def sumar_uno_con_global():
    global contador_global      # sin esta línea, Python crearía una variable local nueva
    contador_global += 1


def sumar_uno_con_return(valor):
    return valor + 1


def alternativa_2():
    # Modificar un valor "de afuera": palabra clave `global` frente a `return`.
    # Sin `global`, la asignación dentro de la función crearía una variable LOCAL nueva
    # y la de afuera no cambiaría (pregunta 2 de comprensión).
    # Conviene: `return` en casi todos los casos: la función avisa lo que calculó y
    # quien la llama decide qué hacer. Usa `global` solo si no hay otra salida.
    sumar_uno_con_global()
    print("Después de sumar_uno_con_global():", contador_global)

    otro_contador = 0
    otro_contador = sumar_uno_con_return(otro_contador)   # guardamos lo que retorna
    print("Después de sumar_uno_con_return():", otro_contador)


def alternativa_3():
    # Los mismos argumentos de la "Llamada 4", pasados todos de forma posicional.
    # Si pasas el `tipo` completo ("informativo"), no necesitas la palabra clave.
    # Conviene: la palabra clave (`repetir=2`) cuando quieres saltarte parámetros y
    # dejar claro a cuál va cada valor; la forma posicional, cuando son pocos y el
    # orden es evidente.
    def configurar_notificacion(mensaje, tipo="informativo", repetir=1):
        print(f"  {mensaje} | tipo: {tipo} | repetir: {repetir}")

    configurar_notificacion("Oferta especial solo por hoy.", repetir=2)
    configurar_notificacion("Oferta especial solo por hoy.", "informativo", 2)   # equivale a la anterior


# alternativa_1()
# alternativa_2()
# alternativa_3()
