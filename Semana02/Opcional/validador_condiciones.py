"""
-------------------------------------------------------------------------------
                             EJERCICIO OPCIONAL 01
                        Pequeño Validador de Condiciones
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Vamos a simular una pequeña validación para una atracción en un parque de diversiones.
Para subir a la atracción "Montaña Rusa Extrema", se deben cumplir dos condiciones:
1. La persona debe medir más de 1.50 metros de altura.
2. La persona debe tener al menos 12 años de edad.

El programa debe:
a. Preguntar al usuario su altura en metros (ej: 1.65).
b. Preguntar al usuario su edad en años (ej: 14).
c. Preguntar si tiene un "pase VIP" (responder "si" o "no").
d. Evaluar si la persona cumple AMBAS condiciones de altura y edad.
   Guarda este resultado en una variable booleana (ej: `cumple_requisitos_basicos`).
e. Evaluar una condición adicional: si la persona tiene un "pase VIP" O (`or`)
   cumple los requisitos básicos (`cumple_requisitos_basicos`).
   Guarda este resultado en una variable booleana (ej: `puede_subir_final`).
f. Imprimir la altura, edad y si tiene pase VIP.
g. Imprimir si cumple los requisitos básicos.
h. Imprimir si finalmente puede subir a la atracción.

## OBJETIVO:
## ---------
Combinar condiciones con `and` y `or` y guardar el resultado en variables booleanas.

## ENTRADA:
## --------
Tres líneas: altura en metros (decimal), edad en años (entero) y "si" o "no".

## SALIDA ESPERADA (ejemplo de ejecución, con 1.65, 14 y no):
## ----------------------------------------------------------
--- Validador para Montaña Rusa Extrema ---
Ingresa tu altura en metros (ej: 1.65): 1.65
Ingresa tu edad en años (ej: 14): 14
¿Tienes un pase VIP? (responde 'si' o 'no'): no

--- Datos Ingresados ---
Altura: 1.65 metros
Edad: 14 años
¿Tiene Pase VIP?: No

--- Resultados de Validación ---
¿Cumple requisitos básicos (altura > 1.50m Y edad >= 12 años)?: True
¿Puede subir a la Montaña Rusa Extrema?: True
-----------------------------------
-------------------------------------------------------------------------------
"""

print("--- Validador para Montaña Rusa Extrema ---")

# a. Preguntar altura
altura_str = input("Ingresa tu altura en metros (ej: 1.65): ")
altura_metros = float(altura_str)

# b. Preguntar edad
edad_str = input("Ingresa tu edad en años (ej: 14): ")
edad_anios = int(edad_str)

# c. Preguntar si tiene pase VIP
tiene_pase_vip_str = input("¿Tienes un pase VIP? (responde 'si' o 'no'): ")
# Convertimos la respuesta a minúsculas para que "SI", "Si" y "si" valgan igual.
# El resultado de `==` es un booleano (True/False) y es lo que se guarda.
tiene_pase_vip = tiene_pase_vip_str.lower() == "si"

print("\n--- Datos Ingresados ---")
print(f"Altura: {altura_metros:.2f} metros")
print(f"Edad: {edad_anios} años")
print(f"¿Tiene Pase VIP?: {'Sí' if tiene_pase_vip else 'No'}") # Usamos un "if en línea" para mostrar

# d. Evaluar si cumple AMBAS condiciones de altura y edad
condicion_altura_ok = altura_metros > 1.50
condicion_edad_ok = edad_anios >= 12
cumple_requisitos_basicos = condicion_altura_ok and condicion_edad_ok

# e. Evaluar si tiene pase VIP O cumple los requisitos básicos
puede_subir_final = tiene_pase_vip or cumple_requisitos_basicos

print("\n--- Resultados de Validación ---")
# g. Imprimir si cumple los requisitos básicos
print(f"¿Cumple requisitos básicos (altura > 1.50m Y edad >= 12 años)?: {cumple_requisitos_basicos}")

# h. Imprimir si finalmente puede subir
print(f"¿Puede subir a la Montaña Rusa Extrema?: {puede_subir_final}")
print("-----------------------------------")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1. En la línea `tiene_pase_vip = tiene_pase_vip_str.lower() == "si"`,
   ¿qué hace el método `.lower()`? ¿Por qué es útil en este caso?
2. Si una persona mide 1.55m y tiene 11 años, y NO tiene pase VIP:
   a. ¿Cuál sería el valor de `condicion_altura_ok`?
   b. ¿Cuál sería el valor de `condicion_edad_ok`?
   c. ¿Cuál sería el valor de `cumple_requisitos_basicos`?
   d. ¿Cuál sería el valor de `puede_subir_final`?
3. ¿Cómo cambiarías la lógica de `puede_subir_final` si la regla fuera que DEBE tener
   pase VIP Y ADEMÁS cumplir los requisitos básicos para poder subir?
4. El "if en línea" `('Sí' if tiene_pase_vip else 'No')` es una forma concisa de un if-else.
   ¿Cómo escribirías esa misma lógica usando una estructura if-else tradicional para
   asignar "Sí" o "No" a una variable antes de imprimirla?
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
    # Acepta "si" y también "sí" (con tilde) usando `in` sobre una tupla de respuestas
    # válidas, y calcula todo con menos variables.
    # `x in (a, b)` es True si x es igual a alguno de los valores de la tupla.
    # Conviene: cuando hay varias respuestas posibles para decir "sí".
    print("--- Validador para Montaña Rusa Extrema ---")
    altura_metros = float(input("Ingresa tu altura en metros (ej: 1.65): "))
    edad_anios = int(input("Ingresa tu edad en años (ej: 14): "))
    respuesta = input("¿Tienes un pase VIP? (responde 'si' o 'no'): ")
    tiene_pase_vip = respuesta.strip().lower() in ("si", "sí")

    print("\n--- Datos Ingresados ---")
    print(f"Altura: {altura_metros:.2f} metros")
    print(f"Edad: {edad_anios} años")
    print(f"¿Tiene Pase VIP?: {'Sí' if tiene_pase_vip else 'No'}")

    cumple_requisitos_basicos = altura_metros > 1.50 and edad_anios >= 12
    puede_subir_final = tiene_pase_vip or cumple_requisitos_basicos

    print("\n--- Resultados de Validación ---")
    print(f"¿Cumple requisitos básicos (altura > 1.50m Y edad >= 12 años)?: {cumple_requisitos_basicos}")
    print(f"¿Puede subir a la Montaña Rusa Extrema?: {puede_subir_final}")
    print("-----------------------------------")


def alternativa_2():
    # Mismo resultado con if/else tradicional, sin `and` ni `or`, y el "if en línea"
    # reemplazado por un if-else normal (pregunta 4 de comprensión).
    # Conviene: cuando recién aprendes y quieres ver paso a paso cada decisión.
    print("--- Validador para Montaña Rusa Extrema ---")
    altura_metros = float(input("Ingresa tu altura en metros (ej: 1.65): "))
    edad_anios = int(input("Ingresa tu edad en años (ej: 14): "))
    respuesta = input("¿Tienes un pase VIP? (responde 'si' o 'no'): ")
    tiene_pase_vip = respuesta.lower() == "si"

    print("\n--- Datos Ingresados ---")
    print(f"Altura: {altura_metros:.2f} metros")
    print(f"Edad: {edad_anios} años")
    if tiene_pase_vip:
        texto_vip = "Sí"
    else:
        texto_vip = "No"
    print(f"¿Tiene Pase VIP?: {texto_vip}")

    if altura_metros > 1.50:
        if edad_anios >= 12:
            cumple_requisitos_basicos = True
        else:
            cumple_requisitos_basicos = False
    else:
        cumple_requisitos_basicos = False

    if tiene_pase_vip:
        puede_subir_final = True
    else:
        puede_subir_final = cumple_requisitos_basicos

    print("\n--- Resultados de Validación ---")
    print(f"¿Cumple requisitos básicos (altura > 1.50m Y edad >= 12 años)?: {cumple_requisitos_basicos}")
    print(f"¿Puede subir a la Montaña Rusa Extrema?: {puede_subir_final}")
    print("-----------------------------------")


# alternativa_1()
# alternativa_2()
