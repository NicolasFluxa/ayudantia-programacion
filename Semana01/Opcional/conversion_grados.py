"""
-------------------------------------------------------------------------------
                             EJERCICIO OPCIONAL 01
                   Conversión de Grados Celsius a Fahrenheit
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Escribe un programa que convierta una temperatura de grados Celsius a grados Fahrenheit.
1. Solicita al usuario que ingrese una temperatura en grados Celsius.
   Asegúrate de convertir este valor a un número decimal.
2. Aplica la fórmula de conversión: Fahrenheit = (Celsius * 9/5) + 32
3. Muestra el resultado de la temperatura en Celsius y su equivalente en Fahrenheit,
   ambos formateados a 1 decimal.

## OBJETIVO:
## ---------
Usar `input()`, convertir texto a número con `float()`, hacer un cálculo y
mostrar el resultado con formato (`:.1f` = un decimal).

## ENTRADA:
## --------
Un número (puede tener decimales), por ejemplo: 25.5

## SALIDA ESPERADA (ejemplo de ejecución, con entrada 25.5):
## ---------------------------------------------------------
Conversor de Grados Celsius a Fahrenheit
----------------------------------------
Ingresa la temperatura en grados Celsius (ej: 25.5): 25.5
----------------------------------------
Temperatura ingresada: 25.5°C
Equivalente en Fahrenheit: 77.9°F
----------------------------------------
-------------------------------------------------------------------------------
"""

# Título del programa
print("Conversor de Grados Celsius a Fahrenheit")
print("----------------------------------------")

# 1. Solicitar temperatura en Celsius
celsius_str = input("Ingresa la temperatura en grados Celsius (ej: 25.5): ")
grados_celsius = float(celsius_str)  # input() entrega texto: lo pasamos a número decimal

# 2. Aplicar la fórmula de conversión
grados_fahrenheit = (grados_celsius * 9/5) + 32

# 3. Mostrar los resultados
print("----------------------------------------")
print(f"Temperatura ingresada: {grados_celsius:.1f}°C")
print(f"Equivalente en Fahrenheit: {grados_fahrenheit:.1f}°F")
print("----------------------------------------")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1. ¿Por qué se utiliza `9/5` en la fórmula en lugar de `1.8` directamente?
   ¿Habría alguna diferencia en el resultado si usaras `1.8`? (Considera la precisión).
2. Si quisieras realizar la conversión inversa (Fahrenheit a Celsius),
   ¿cómo sería la fórmula? (Fórmula: Celsius = (Fahrenheit - 32) * 5/9)
   ¿Podrías modificar este programa para que también haga esa conversión,
   quizás preguntando al usuario qué conversión desea hacer? (Esto último es un desafío).
3. ¿Qué son los "números mágicos" en programación y por qué podría ser una buena
   idea asignar `9/5` y `32` a variables con nombres descriptivos en este programa?
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
    # Todo en una línea: input() dentro de float(), sin variable intermedia de texto.
    # Conviene: cuando el texto original no se vuelve a usar. Es más corto.
    print("Conversor de Grados Celsius a Fahrenheit")
    print("----------------------------------------")
    grados_celsius = float(input("Ingresa la temperatura en grados Celsius (ej: 25.5): "))
    grados_fahrenheit = grados_celsius * 1.8 + 32   # 9/5 es lo mismo que 1.8
    print("----------------------------------------")
    print(f"Temperatura ingresada: {grados_celsius:.1f}°C")
    print(f"Equivalente en Fahrenheit: {grados_fahrenheit:.1f}°F")
    print("----------------------------------------")


def alternativa_2():
    # Formato con .format() y con round() en vez de f-string.
    # .format() reemplaza cada {} en orden; es la forma anterior a los f-strings
    # y la verás en código antiguo. round(x, 1) redondea a 1 decimal.
    # Conviene: para reconocerla al leer código ajeno; para escribir, usa f-string.
    print("Conversor de Grados Celsius a Fahrenheit")
    print("----------------------------------------")
    grados_celsius = float(input("Ingresa la temperatura en grados Celsius (ej: 25.5): "))
    grados_fahrenheit = (grados_celsius * 9 / 5) + 32
    print("----------------------------------------")
    print("Temperatura ingresada: {:.1f}°C".format(grados_celsius))
    print("Equivalente en Fahrenheit: {}°F".format(round(grados_fahrenheit, 1)))
    print("----------------------------------------")


def alternativa_3():
    # Función propia que hace solo la conversión (adelanto de funciones, Semana 8).
    # Conviene: cuando necesitas convertir muchas veces sin repetir la fórmula.
    def celsius_a_fahrenheit(c):
        return (c * 9 / 5) + 32

    print("Conversor de Grados Celsius a Fahrenheit")
    print("----------------------------------------")
    grados_celsius = float(input("Ingresa la temperatura en grados Celsius (ej: 25.5): "))
    print("----------------------------------------")
    print(f"Temperatura ingresada: {grados_celsius:.1f}°C")
    print(f"Equivalente en Fahrenheit: {celsius_a_fahrenheit(grados_celsius):.1f}°F")
    print("----------------------------------------")


# alternativa_1()
# alternativa_2()
# alternativa_3()
