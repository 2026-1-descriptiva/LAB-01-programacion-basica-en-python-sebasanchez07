"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario donde las claves son las cadenas de tres letras
    que aparecen en la columna 5 y los valores son la cantidad de veces
    que dicha cadena aparece en todo el archivo.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}

    """
    import os

    filepath = os.path.join(os.path.dirname(__file__), "..", "files", "input", "data.csv")

    # Diccionario: clave (de col 5) -> cantidad de apariciones
    conteo = {}

    with open(filepath, "r") as f:
        for line in f:
            cols = line.strip().split("\t")
            pares = cols[4].split(",")

            for par in pares:
                # "clave:valor" -> solo nos interesa la clave
                clave, _ = par.split(":")
                conteo[clave] = conteo.get(clave, 0) + 1

    return conteo
