"""
-------------------------------------------------------------------------------
                                  EJERCICIO 02
                         Funciones con Retorno (return)
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
En el ejercicio anterior las funciones IMPRIMÍAN el resultado con `print()`.
Ahora las funciones lo DEVOLVERÁN con `return`, para que quien las llame
pueda guardarlo en una variable o usarlo en otro cálculo.

Define las siguientes funciones (todas con docstring):
1.  `cuadrado(numero)`: retorna el cuadrado del número.
2.  `calcular_area_rectangulo(base, altura)`: retorna el área (base * altura).
    `calcular_perimetro_rectangulo(base, altura)`: retorna el perímetro.
3.  `es_par(numero)`: retorna `True` si el número es par y `False` si no.
4.  `calcular_precio_final(precio, porcentaje_descuento)`: retorna el precio
    después de aplicar el descuento (por ejemplo, 15 significa 15%).
5.  `clasificar_nota(nota)`: retorna el texto "Aprobado" si la nota es
    mayor o igual a 4.0 (escala chilena de 1.0 a 7.0) y "Reprobado" si no.
6.  Muestra la diferencia entre `print` y `return`: define una función que
    solo imprime el cuadrado y comprueba qué valor entrega (None).

Luego, en el programa principal, pide los datos al usuario, llama a las
funciones, guarda lo que retornan en variables y muéstralo.

## OBJETIVO:
## ---------
Entender que `return` entrega un valor a quien llamó a la función, que ese valor
se puede guardar o combinar con otros, y que una función sin `return` entrega `None`.

## ENTRADA:
## --------
Cuatro datos, uno por línea: un número entero, la base, la altura y una nota.
Ejemplo: 7, 3.5, 2 y 5.5

## SALIDA ESPERADA (ejemplo de ejecución, con 7, 3.5, 2 y 5.5):
## ------------------------------------------------------------
--- 1. Cuadrado de un número ---
Ingresa un número entero: 7
El cuadrado de 7 es 49
Con dos llamadas: 3² + 4² = 25

--- 2. Rectángulo ---
Ingresa la base: 3.5
Ingresa la altura: 2
Área: 7.0
Perímetro: 11.0

--- 3. ¿Par o impar? ---
7 es impar
es_par(7) devuelve: False

--- 4. Precio con descuento ---
Precio normal: $20000, descuento 15% -> precio final: $17000

--- 5. Clasificar una nota ---
Ingresa una nota entre 1.0 y 7.0: 5.5
Con un 5.5 estás: Aprobado

--- 6. print vs return ---
25
Lo que devolvió cuadrado_con_print: None
Lo que devolvió cuadrado: 25
-------------------------------------------------------------------------------
"""

# 1. Cuadrado
def cuadrado(numero):
    """Retorna el cuadrado de un número."""
    return numero * numero   # `return` entrega el valor y termina la función

# 2. Área y perímetro de un rectángulo
def calcular_area_rectangulo(base, altura):
    """Retorna el área de un rectángulo (base por altura)."""
    return base * altura

def calcular_perimetro_rectangulo(base, altura):
    """Retorna el perímetro de un rectángulo (suma de sus cuatro lados)."""
    return 2 * (base + altura)

# 3. ¿Es par?
def es_par(numero):
    """Retorna True si el número es par y False si es impar."""
    # numero % 2 es el resto de dividir por 2: en los pares es 0.
    # La comparación ya entrega True o False, así que se retorna directamente.
    return numero % 2 == 0

# 4. Precio final con descuento
def calcular_precio_final(precio, porcentaje_descuento):
    """
    Retorna el precio después de aplicar un descuento.

    Args:
        precio (int or float): precio original.
        porcentaje_descuento (int or float): descuento en porcentaje (15 = 15%).
    """
    descuento = precio * porcentaje_descuento / 100
    return precio - descuento

# 5. Clasificar una nota
def clasificar_nota(nota):
    """Retorna "Aprobado" si la nota es 4.0 o más, y "Reprobado" si no."""
    if nota >= 4.0:
        return "Aprobado"      # al ejecutar un return, la función termina aquí...
    return "Reprobado"         # ...así que esta línea solo se alcanza si no aprobó

# 6. Una función SIN return (solo imprime)
def cuadrado_con_print(numero):
    """Imprime el cuadrado, pero no lo devuelve (por eso entrega None)."""
    print(numero * numero)


# ----------------------------- Programa principal -----------------------------
print("--- 1. Cuadrado de un número ---")
numero = int(input("Ingresa un número entero: "))
resultado_cuadrado = cuadrado(numero)      # guardamos lo que retorna la función
print(f"El cuadrado de {numero} es {resultado_cuadrado}")
# Como retorna un valor, podemos usarlo dentro de otra operación:
print(f"Con dos llamadas: 3² + 4² = {cuadrado(3) + cuadrado(4)}")

print("\n--- 2. Rectángulo ---")
base = float(input("Ingresa la base: "))
altura = float(input("Ingresa la altura: "))
area = calcular_area_rectangulo(base, altura)
perimetro = calcular_perimetro_rectangulo(base, altura)
print(f"Área: {area:.1f}")
print(f"Perímetro: {perimetro:.1f}")

print("\n--- 3. ¿Par o impar? ---")
if es_par(numero):    # la función retorna un booleano: sirve directo como condición
    print(f"{numero} es par")
else:
    print(f"{numero} es impar")
print(f"es_par({numero}) devuelve: {es_par(numero)}")

print("\n--- 4. Precio con descuento ---")
precio_final = calcular_precio_final(20000, 15)
print(f"Precio normal: $20000, descuento 15% -> precio final: ${precio_final:.0f}")

print("\n--- 5. Clasificar una nota ---")
nota = float(input("Ingresa una nota entre 1.0 y 7.0: "))
print(f"Con un {nota:.1f} estás: {clasificar_nota(nota)}")

print("\n--- 6. print vs return ---")
valor_con_print = cuadrado_con_print(5)    # imprime 25, pero no devuelve nada
print("Lo que devolvió cuadrado_con_print:", valor_con_print)   # None
valor_con_return = cuadrado(5)             # no imprime; devuelve 25
print("Lo que devolvió cuadrado:", valor_con_return)

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  ¿Cuál es la diferencia entre mostrar un valor con `print()` dentro de una
    función y retornarlo con `return`? ¿Cuál de las dos deja la función más
    reutilizable? Usa `cuadrado` y `cuadrado_con_print` para explicarlo.
2.  ¿Qué valor entrega una función que no tiene `return`? Compruébalo con
    `print(cuadrado_con_print(3))`.
3.  En `clasificar_nota`, ¿qué pasa con las líneas que están después de un
    `return` que se ejecutó? ¿Por qué no hace falta un `else`?
4.  `es_par` retorna directamente `numero % 2 == 0`. Reescríbela con un
    `if`/`else` que retorne `True` o `False` de forma explícita. ¿Qué versión
    te parece más clara?
5.  Escribe `es_mayor_de_edad(edad)` que retorne `True` si la edad es 18 o más,
    y úsala en un `if` en el programa principal.
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
    # Los mismos resultados con otra forma de escribir cada función:
    #   numero ** 2          -> "elevado a 2"; igual que numero * numero.
    #   if / else explícito  -> retorna True o False escritos a mano.
    #   if en línea          -> valor_si_cumple if condicion else valor_si_no.
    # Conviene: ** cuando la potencia puede cambiar (numero ** 3); el if/else
    # explícito mientras practicas; el if en línea cuando el valor depende de una
    # sola condición simple.
    def cuadrado(numero):
        return numero ** 2

    def calcular_area_rectangulo(base, altura):
        return base * altura

    def calcular_perimetro_rectangulo(base, altura):
        return base + altura + base + altura

    def es_par(numero):
        if numero % 2 == 0:
            return True
        else:
            return False

    def calcular_precio_final(precio, porcentaje_descuento):
        return precio * (1 - porcentaje_descuento / 100)

    def clasificar_nota(nota):
        return "Aprobado" if nota >= 4.0 else "Reprobado"

    def cuadrado_con_print(numero):
        print(numero ** 2)

    print("--- 1. Cuadrado de un número ---")
    numero = int(input("Ingresa un número entero: "))
    print(f"El cuadrado de {numero} es {cuadrado(numero)}")
    print(f"Con dos llamadas: 3² + 4² = {cuadrado(3) + cuadrado(4)}")

    print("\n--- 2. Rectángulo ---")
    base = float(input("Ingresa la base: "))
    altura = float(input("Ingresa la altura: "))
    print(f"Área: {calcular_area_rectangulo(base, altura):.1f}")
    print(f"Perímetro: {calcular_perimetro_rectangulo(base, altura):.1f}")

    print("\n--- 3. ¿Par o impar? ---")
    if es_par(numero):
        print(f"{numero} es par")
    else:
        print(f"{numero} es impar")
    print(f"es_par({numero}) devuelve: {es_par(numero)}")

    print("\n--- 4. Precio con descuento ---")
    print(f"Precio normal: $20000, descuento 15% -> precio final: ${calcular_precio_final(20000, 15):.0f}")

    print("\n--- 5. Clasificar una nota ---")
    nota = float(input("Ingresa una nota entre 1.0 y 7.0: "))
    print(f"Con un {nota:.1f} estás: {clasificar_nota(nota)}")

    print("\n--- 6. print vs return ---")
    valor_con_print = cuadrado_con_print(5)
    print("Lo que devolvió cuadrado_con_print:", valor_con_print)
    print("Lo que devolvió cuadrado:", cuadrado(5))


def alternativa_2():
    # Una sola función que retorna DOS valores (área y perímetro) en una tupla.
    #   return area, perimetro   -> Python los empaqueta en una tupla (un par).
    #   area, perimetro = f(...) -> al llamar, se "desempaquetan" en dos variables.
    # Conviene: cuando dos resultados salen de los mismos datos y siempre se
    # necesitan juntos. Si se usan por separado, es más claro tener dos funciones.
    def cuadrado(numero):
        return numero * numero

    def area_y_perimetro(base, altura):
        """Retorna (área, perímetro) de un rectángulo."""
        return base * altura, 2 * (base + altura)

    def es_par(numero):
        return numero % 2 == 0

    def calcular_precio_final(precio, porcentaje_descuento):
        return precio - precio * porcentaje_descuento / 100

    def clasificar_nota(nota):
        if nota >= 4.0:
            return "Aprobado"
        return "Reprobado"

    def cuadrado_con_print(numero):
        print(numero * numero)

    print("--- 1. Cuadrado de un número ---")
    numero = int(input("Ingresa un número entero: "))
    print(f"El cuadrado de {numero} es {cuadrado(numero)}")
    print(f"Con dos llamadas: 3² + 4² = {cuadrado(3) + cuadrado(4)}")

    print("\n--- 2. Rectángulo ---")
    base = float(input("Ingresa la base: "))
    altura = float(input("Ingresa la altura: "))
    area, perimetro = area_y_perimetro(base, altura)
    print(f"Área: {area:.1f}")
    print(f"Perímetro: {perimetro:.1f}")

    print("\n--- 3. ¿Par o impar? ---")
    if es_par(numero):
        print(f"{numero} es par")
    else:
        print(f"{numero} es impar")
    print(f"es_par({numero}) devuelve: {es_par(numero)}")

    print("\n--- 4. Precio con descuento ---")
    precio_final = calcular_precio_final(20000, 15)
    print(f"Precio normal: $20000, descuento 15% -> precio final: ${precio_final:.0f}")

    print("\n--- 5. Clasificar una nota ---")
    nota = float(input("Ingresa una nota entre 1.0 y 7.0: "))
    print(f"Con un {nota:.1f} estás: {clasificar_nota(nota)}")

    print("\n--- 6. print vs return ---")
    valor_con_print = cuadrado_con_print(5)
    print("Lo que devolvió cuadrado_con_print:", valor_con_print)
    print("Lo que devolvió cuadrado:", cuadrado(5))


# alternativa_1()
# alternativa_2()
