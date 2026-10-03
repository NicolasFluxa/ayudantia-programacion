# Ayudantía de Programación en Python

Material de apoyo de la ayudantía del ramo **Programación en Python**, Universidad Autónoma de Chile (sede Talca). Ayudantías 2023 a 2026.

Son ejercicios cortos, con solución comentada, preguntas de comprensión y **otras formas de hacerlo**, ordenados por semana: desde `print()` y variables hasta funciones y un proyecto integrador. Sirven para practicar después de clases y para repasar antes de una evaluación.

## Contenido

| Carpeta | Tema | Qué encontrarás |
|---|---|---|
| `Semana01` | Primeros pasos | `print`, comentarios, variables y tipos de datos. Opcional: conversión de Celsius a Fahrenheit |
| `Semana02` | Entrada de datos y lógica | `input`, operaciones aritméticas, comparaciones y operadores lógicos. Opcional: validador de condiciones |
| `Semana03` | Condicionales | `if` / `elif` / `else`: mayoría de edad y clasificación de un número. Opcional: calculadora de descuentos |
| `Semana04` | Ciclo `while` | Contador y menú interactivo. Opcional: adivina el número |
| `Semana05` | Ciclo `for` y `range()` | Conteos y recorrido de un texto. Opcional: tabla de multiplicar |
| `Semana06` | Listas (1) | Crear, acceder y modificar listas. Opcional: lista de compras dinámica |
| `Semana07` | Listas (2) | Recorrer, ordenar, buscar y contar. Opcional: análisis de números (suma, máximo, mínimo, promedio) |
| `Semana08` | Funciones (1) | Definir funciones, parámetros, docstrings y `return`. Opcional: función que retorna el análisis de una lista |
| `Semana09` | Funciones (2) | Alcance de variables, argumentos por defecto y por palabra clave. Opcional: `*args` y `**kwargs` |
| `Semana10` | Proyecto integrador | Gestor de tareas por consola y su extensión con búsqueda (este último archivo ya incluye todo y se ejecuta solo). Opcional: verificador de fortaleza de contraseña |
| `Triangulos` | Extra | Figuras con `for`: escaleras, pirámides y diamante |

Dentro de cada semana, los ejercicios principales están directamente en la carpeta y los más desafiantes, en `Opcional/`.

## Cómo están escritos los ejercicios

Cada archivo `.py` trae, en este orden:

1. **Enunciado**: qué debes resolver, con el objetivo, la entrada y un ejemplo de la salida esperada (al inicio del archivo).
2. **Solución comentada**: una solución propuesta en Python.
3. **Preguntas de comprensión**: para reflexionar sobre el código.
4. **Otras formas de hacerlo**: de 1 a 3 maneras distintas de obtener el mismo resultado (por ejemplo, `for` frente a `while`, f-string frente a concatenación, `in` frente a un bucle de búsqueda), cada una con una línea que dice cuándo conviene. Vienen dentro de funciones `alternativa_1()`, `alternativa_2()`, etc. que **no se ejecutan solas**: para probarlas, quita el `#` de la llamada que aparece al final del archivo.

Los archivos de `Triangulos` tienen la misma estructura, sin preguntas de comprensión.

## Cómo ejecutar los ejemplos

Necesitas **Python 3.8 o superior** ([descargar](https://www.python.org/downloads/)). Los ejemplos no usan librerías externas: no hay nada más que instalar.

1. Descarga el repositorio con el botón verde **Code** > **Download ZIP**, o clónalo con `git clone` usando la URL de ese mismo botón.
2. Abre una terminal en la carpeta del repositorio.
3. Ejecuta el archivo que quieras. Por ejemplo:

```
python Semana01/variables_y_tipos_de_datos.py
```

En Windows también puedes escribir `py` en lugar de `python`. Si el nombre del archivo tiene espacios (como en `Triangulos`), ponlo entre comillas:

```
python "Triangulos/5. Pirámide.py"
```

También puedes abrir los archivos en VS Code, PyCharm, Thonny o el editor que prefieras y ejecutarlos desde ahí.

## Cómo sacarle provecho

- Intenta resolver cada enunciado por tu cuenta antes de mirar la solución.
- Ejecuta el código, modifícalo y observa qué cambia.
- Responde las preguntas de comprensión: son una buena forma de autoevaluarte.
- Revisa las "Otras formas de hacerlo" y compáralas con tu solución: no hay una única respuesta correcta, pero sí versiones más claras o más cortas según el caso.

## Dudas

Este repositorio complementa las clases. La instancia principal para resolver dudas son las sesiones de ayudantía: llega con tus preguntas preparadas.

---

Material preparado por Nicolás Fluxá, ayudante de Programación en Python.
[Perfil en LinkedIn](https://www.linkedin.com/in/nflux%C3%A1/)
