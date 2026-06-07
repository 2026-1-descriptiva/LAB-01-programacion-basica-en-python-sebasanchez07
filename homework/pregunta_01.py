"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import os

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    filepath = os.path.join(os.path.dirname(__file__), "..", "files", "input", "data.csv")
    with open(filepath, "r") as f:
        total = 0
        for line in f:
            cols = line.strip().split("\t")
            total += int(cols[1])
    return total