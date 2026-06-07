"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contenga la suma de la columna 2 (el número)
    asociada a cada letra (minúscula) de la columna 4.

    Es decir, para cada letra minúscula que aparece en la columna 4, se suman
    todos los valores de la columna 2 que comparten registro con esa letra.

    Rta/
    {'a': 122,
     'b': 49,
     'c': 91,
     'd': 73,
     'e': 86,
     'f': 134,
     'g': 35}

    """
    import os

    filepath = os.path.join(os.path.dirname(__file__), "..", "files", "input", "data.csv")

    # Diccionario: letra (de col 4) -> suma de numeros (col 2)
    suma = {}

    with open(filepath, "r") as f:
        for line in f:
            cols = line.strip().split("\t")
            numero = int(cols[1])         # Columna 2 (número entero)
            letras = cols[3].split(",")   # Columna 4: letras separadas por coma

            # Por cada letra de la columna 4, le sumamos el número de la columna 2
            for letra in letras:
                suma[letra] = suma.get(letra, 0) + numero

    return suma
