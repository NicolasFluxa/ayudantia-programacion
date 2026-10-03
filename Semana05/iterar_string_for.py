"""
-------------------------------------------------------------------------------
                                  EJERCICIO 02
                        Iterar sobre un String con `for`
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Escribe un programa que solicite al usuario ingresar una palabra o frase
y luego utilice un bucle `for` para realizar las siguientes acciones:

1.  Imprimir cada carácter de la palabra o frase en una línea diferente.
2.  Contar y mostrar cuántas vocales ('a', 'e', 'i', 'o', 'u',
    ignorando mayúsculas/minúsculas) hay en la palabra o frase.
3.  (Opcional) Crear una nueva cadena que sea la inversa de la cadena ingresada.

## OBJETIVO:
## ---------
Ver que un texto se puede recorrer carácter por carácter con `for`, y usar
un acumulador (contador o texto) que se va armando en cada vuelta.

## ENTRADA:
## --------
Una palabra o frase. Ejemplo: Hola

## SALIDA ESPERADA (ejemplo de ejecución, con "Hola"):
## ---------------------------------------------------
Ingresa una palabra o una frase: Hola

--- 1. Imprimiendo cada carácter ---
H
o
l
a

--- 2. Conteo de vocales ---
La palabra o frase 'Hola' tiene 2 vocal(es).

--- 3. (Opcional) Cadena Inversa ---
El texto original es: 'Hola'
El texto invertido es: 'aloH'

¡Proceso completado!

Nota: las vocales con tilde (á, é, í, ó, ú) no se cuentan en esta solución.
-------------------------------------------------------------------------------
"""

# Solicitar palabra o frase al usuario
texto_usuario = input("Ingresa una palabra o una frase: ")

print("\n--- 1. Imprimiendo cada carácter ---")
# 1. Imprimir cada carácter
for caracter in texto_usuario:
    print(caracter)

# 2. Contar vocales
contador_vocales = 0
vocales = "aeiouAEIOU"  # Incluimos mayúsculas y minúsculas para no tener que convertir el texto

for caracter in texto_usuario:
    if caracter in vocales: # Comprueba si el caracter está en la cadena de vocales
        contador_vocales = contador_vocales + 1

print("\n--- 2. Conteo de vocales ---")
print(f"La palabra o frase '{texto_usuario}' tiene {contador_vocales} vocal(es).")


# 3. (Opcional) Crear cadena inversa
texto_inverso = ""
# Iteramos sobre el texto original
for caracter in texto_usuario:
    # Añadimos el carácter actual al PRINCIPIO del texto_inverso
    # (ej: "Hola" -> "H" -> "oH" -> "loH" -> "aloH")
    texto_inverso = caracter + texto_inverso

print("\n--- 3. (Opcional) Cadena Inversa ---")
print(f"El texto original es: '{texto_usuario}'")
print(f"El texto invertido es: '{texto_inverso}'")


print("\n¡Proceso completado!")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  En el bucle `for caracter in texto_usuario:`, ¿qué representa la variable
    `caracter` en cada iteración?
2.  Para el conteo de vocales, se usó `if caracter in vocales:`.
    Explica cómo funciona el operador `in` cuando se usa con cadenas de texto.
3.  En la parte opcional de invertir la cadena, ¿por qué la línea
    `texto_inverso = caracter + texto_inverso` logra invertirla?
    ¿Qué pasaría si usaras `texto_inverso = texto_inverso + caracter`?
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
    # Recorrer el texto con `while` y un índice (Semana 4 + índices de texto).
    # texto[indice] entrega el carácter en esa posición, igual que en las listas.
    # Conviene: cuando necesitas saber la posición del carácter o saltarte algunos.
    # Si solo quieres cada carácter, `for caracter in texto` es más simple.
    texto_usuario = input("Ingresa una palabra o una frase: ")

    print("\n--- 1. Imprimiendo cada carácter ---")
    indice = 0
    while indice < len(texto_usuario):
        print(texto_usuario[indice])
        indice += 1

    contador_vocales = 0
    indice = 0
    while indice < len(texto_usuario):
        if texto_usuario[indice] in "aeiouAEIOU":
            contador_vocales += 1
        indice += 1
    print("\n--- 2. Conteo de vocales ---")
    print(f"La palabra o frase '{texto_usuario}' tiene {contador_vocales} vocal(es).")

    texto_inverso = ""
    indice = len(texto_usuario) - 1      # empezamos por el último carácter
    while indice >= 0:
        texto_inverso += texto_usuario[indice]
        indice -= 1
    print("\n--- 3. (Opcional) Cadena Inversa ---")
    print(f"El texto original es: '{texto_usuario}'")
    print(f"El texto invertido es: '{texto_inverso}'")
    print("\n¡Proceso completado!")


def alternativa_2():
    # Contar con sum() y una condición, y invertir con un "corte" de texto [::-1].
    #   sum(1 for c in texto if c in vocales)  -> suma un 1 por cada vocal encontrada.
    #   texto[::-1] -> recorre el texto de atrás hacia adelante (paso -1).
    # Conviene: cuando ya dominas el `for` y quieres la versión corta. Hace exactamente
    # lo mismo que los bucles de la solución principal, en una línea cada uno.
    texto_usuario = input("Ingresa una palabra o una frase: ")

    print("\n--- 1. Imprimiendo cada carácter ---")
    for caracter in texto_usuario:
        print(caracter)

    contador_vocales = sum(1 for caracter in texto_usuario if caracter in "aeiouAEIOU")
    print("\n--- 2. Conteo de vocales ---")
    print(f"La palabra o frase '{texto_usuario}' tiene {contador_vocales} vocal(es).")

    texto_inverso = texto_usuario[::-1]
    print("\n--- 3. (Opcional) Cadena Inversa ---")
    print(f"El texto original es: '{texto_usuario}'")
    print(f"El texto invertido es: '{texto_inverso}'")
    print("\n¡Proceso completado!")


def alternativa_3():
    # Contar con el método .count() de los textos, vocal por vocal, y pasar todo a
    # minúsculas con .lower() para no repetir las mayúsculas.
    # Conviene: cuando quieres contar letras sin escribir tú el bucle. Ojo: .count()
    # cuenta un texto a la vez, por eso se suma una vez por cada vocal.
    texto_usuario = input("Ingresa una palabra o una frase: ")

    print("\n--- 1. Imprimiendo cada carácter ---")
    for caracter in texto_usuario:
        print(caracter)

    minusculas = texto_usuario.lower()
    contador_vocales = 0
    for vocal in "aeiou":
        contador_vocales += minusculas.count(vocal)
    print("\n--- 2. Conteo de vocales ---")
    print(f"La palabra o frase '{texto_usuario}' tiene {contador_vocales} vocal(es).")

    # reversed() entrega los caracteres de atrás hacia adelante; "".join() los une.
    texto_inverso = "".join(reversed(texto_usuario))
    print("\n--- 3. (Opcional) Cadena Inversa ---")
    print(f"El texto original es: '{texto_usuario}'")
    print(f"El texto invertido es: '{texto_inverso}'")
    print("\n¡Proceso completado!")


# alternativa_1()
# alternativa_2()
# alternativa_3()
