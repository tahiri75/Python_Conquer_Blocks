"""'Ejercicio de Memoización en Análisis de Texto
Imagina que estás trabajando en un sistema de análisis de texto que requiere
calcular la frecuencia de ocurrencia de palabras en un conjunto de
documentos. Implementa una función llamada calcular_frecuencia_palabras que
tome como entrada un texto y devuelva un diccionario que muestre la
frecuencia de cada palabra en el texto.
1. La función debe ser capaz de manejar textos y ser insensible a
mayúsculas/minúsculas (por ejemplo, "Hola" y "hola" se consideran la
misma palabra).
2. Se deben excluir las palabras comunes (artículos, preposiciones, etc.) que
no aportan información relevante al análisis.
3. Utiliza memoización para evitar recalcular la frecuencia de palabras para el
mismo texto."""

import functools
import re
import time


@functools.lru_cache(maxsize=None)
def calcular_frecuencia_palabras(texto):
    # preprocesamiento texto
    texto = texto.lower()
    texto = re.sub(
        r"[^a-z\s]", "", texto
    )  # eliminar puntuacion o caracteres no deseados
    palabras = texto.split()
    print(palabras)

    # excluir palabras comunes
    palabras_comunes = set(
        [
            "el",
            "la",
            "los",
            "las",
            "de",
            "en",
            "y",
            "a",
            "con",
            "es",
            "un",
            "una",
            "para",
            "en",
            "del",
            "al",
        ]
    )

    palabras = [palabra for palabra in palabras if palabra not in palabras_comunes]

    # conteo de frecuencia

    frecuencia = {}
    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    return frecuencia


texto_1 = """'Tienes a tu disposición un conjunto de discos numerados del 1 al N y tres torres
etiquetadas como A, B y C. La torre A contiene inicialmente todos los discos
apilados en orden descendente, desde el disco N en la parte inferior hasta el
disco 1 en la parte superior.
Tu tarea es implementar una solución recursiva para mover todos los discos
desde la torre A hasta la torre C, siguiendo las reglas clásicas de las Torres de
Hanoi:"""

inicio = time.time()
frecuencia = calcular_frecuencia_palabras(texto_1)
fin = time.time()

print(frecuencia)

# con memoizacion
inicio_m = time.time()
frecuencia_m = calcular_frecuencia_palabras(texto_1)
fin_m = time.time()

print("Tiempo sin memoizacion: ", fin - inicio)
print("Tiempo con memoizacion: ", fin_m - inicio_m)
