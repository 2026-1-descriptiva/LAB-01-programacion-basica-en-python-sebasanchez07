"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Retorne un diccionario con la suma de los valores numéricos (parte
    derecha después de `:`) de la columna 5, agrupados por la letra de la
    columna 1.

    Rta/
    {'A': 177,
     'B': 187,
     'C': 114,
     'D': 136,
     'E': 324}

    """
    import os

    filepath = os.path.join(os.path.dirname(__file__), "..", "files", "input", "data.csv")

    # Diccionario: letra (de col 1) -> suma de valores (de col 5)
    suma = {}

    with open(filepath, "r") as f:
        for line in f:
            cols = line.strip().split("\t")
            letra = cols[0]            # Columna 1: letra mayúscula
            pares = cols[4].split(",") # Columna 5: pares "clave:valor"

            # Por cada par "clave:valor", sumamos solo el valor a la letra de col 1
            for par in pares:
                _, valor = par.split(":")
                valor = int(valor)
                suma[letra] = suma.get(letra, 0) + valor

    return suma
