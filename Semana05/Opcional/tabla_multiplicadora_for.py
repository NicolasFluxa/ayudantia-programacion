"""
-------------------------------------------------------------------------------
                             EJERCICIO OPCIONAL 01
                         Tabla de Multiplicar con `for`
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Desarrolla un programa que solicite al usuario un número entero y
luego muestre la tabla de multiplicar de ese número desde el 1 hasta el 10.

Formato de salida esperado para cada línea (ejemplo para el número 5, multiplicando por 3):
"5 x 3 = 15"

## OBJETIVO:
## ---------
Usar `for` con `range(1, 11)` y la variable del bucle dentro de un cálculo.

## ENTRADA:
## --------
Un número entero (puede ser negativo). Ejemplo: 5

## SALIDA ESPERADA (ejemplo de ejecución, con 5):
## ----------------------------------------------
Ingresa un número entero para ver su tabla de multiplicar: 5

--- Tabla de Multiplicar del 5 ---
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50
-----------------------------------
¡Tabla generada!
-------------------------------------------------------------------------------
"""

# Solicitar número al usuario
numero_str = input("Ingresa un número entero para ver su tabla de multiplicar: ")
numero = int(numero_str)

print(f"\n--- Tabla de Multiplicar del {numero} ---")

# Usamos un bucle for con range para iterar del 1 al 10
# range(1, 11) generará los números 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
for multiplicador in range(1, 11):
    resultado = numero * multiplicador
    # Imprimir la línea de la tabla con el formato especificado
    print(f"{numero} x {multiplicador} = {resultado}")

print("-----------------------------------")
print("¡Tabla generada!")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  En `range(1, 11)`, ¿por qué se usa `11` como segundo argumento si solo
    queremos multiplicar hasta el 10?
2.  ¿Cómo modificarías el programa para que muestre la tabla de multiplicar
    desde el 1 hasta el 12 en lugar del 10?
3.  (Desafío) ¿Podrías usar un bucle `for` anidado (un `for` dentro de otro `for`)
    para imprimir las tablas de multiplicar de todos los números del 1 al 5?
    Pista: el bucle exterior controlaría el número de la tabla (1 a 5) y el
    bucle interior el multiplicador (1 a 10).
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
    # Con `while`: tú llevas la cuenta del multiplicador.
    # Conviene: casi nunca para esto; sirve para comparar con el `for`, que hace la
    # inicialización, la comparación y el incremento por ti.
    numero = int(input("Ingresa un número entero para ver su tabla de multiplicar: "))
    print(f"\n--- Tabla de Multiplicar del {numero} ---")
    multiplicador = 1
    while multiplicador <= 10:
        print(f"{numero} x {multiplicador} = {numero * multiplicador}")
        multiplicador += 1
    print("-----------------------------------")
    print("¡Tabla generada!")


def alternativa_2():
    # Sin multiplicar: cada resultado es el anterior más `numero` (sumas sucesivas).
    # La multiplicación es una suma repetida: 5 x 3 = 5 + 5 + 5.
    # Conviene: para entender qué hace una tabla de multiplicar por dentro; en un
    # programa real usa `*`, que es más claro.
    numero = int(input("Ingresa un número entero para ver su tabla de multiplicar: "))
    print(f"\n--- Tabla de Multiplicar del {numero} ---")
    resultado = 0
    for multiplicador in range(1, 11):
        resultado = resultado + numero
        print(f"{numero} x {multiplicador} = {resultado}")
    print("-----------------------------------")
    print("¡Tabla generada!")


def alternativa_3():
    # Armar primero todas las líneas en una lista (comprensión de listas) y luego
    # mostrarlas juntas con "\n".join().
    #   [expresión for variable in range(...)] crea una lista, una vuelta por elemento.
    # Conviene: cuando necesitas guardar o reutilizar las líneas (por ejemplo,
    # escribirlas en un archivo) y no solo imprimirlas.
    numero = int(input("Ingresa un número entero para ver su tabla de multiplicar: "))
    print(f"\n--- Tabla de Multiplicar del {numero} ---")
    lineas = [f"{numero} x {m} = {numero * m}" for m in range(1, 11)]
    print("\n".join(lineas))
    print("-----------------------------------")
    print("¡Tabla generada!")


# alternativa_1()
# alternativa_2()
# alternativa_3()
