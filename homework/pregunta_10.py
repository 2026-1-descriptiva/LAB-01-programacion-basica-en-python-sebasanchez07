"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas (letra_col1, cantidad_elementos_col4,
    cantidad_elementos_col5) para cada registro del archivo, en el mismo
    orden en que aparecen en el CSV.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ('B', 4, 4),
     ('A', 2, 4),
     ('C', 4, 4),
     ('A', 2, 5),
     ('A', 3, 6),
     ('B', 2, 3),
     ('E', 4, 6),
     ('B', 4, 6),
     ('C', 4, 5),
     ('C', 4, 3),
     ('D', 4, 5),
     ('E', 2, 3),
     ('B', 2, 5),
     ('D', 2, 4),
     ('E', 3, 6),
     ('D', 2, 3),
     ('E', 4, 3),
     ('E', 2, 3),
     ('E', 2, 3),
     ('E', 3, 3),
     ('D', 3, 3),
     ('A', 3, 5),
     ('E', 2, 6),
     ('E', 3, 6),
     ('A', 3, 3),
     ('E', 3, 5),
     ('A', 2, 5),
     ('C', 4, 6),
     ('A', 2, 5),
     ('D', 2, 6),
     ('E', 2, 4),
     ('B', 3, 6),
     ('B', 3, 5),
     ('D', 2, 3),
     ('B', 2, 5),
     ('C', 4, 3),
     ('E', 2, 3),
     ('E', 3, 3)]

    """
    import os

    filepath = os.path.join(os.path.dirname(__file__), "..", "files", "input", "data.csv")

    resultado = []

    with open(filepath, "r") as f:
        for line in f:
            cols = line.strip().split("\t")
            letra = cols[0]                   # Columna 1: una sola letra
            letras_col4 = cols[3].split(",")  # Columna 4: lista separada por comas
            pares = cols[4].split(",")        # Columna 5: pares clave:valor separados por comas

            # len() cuenta cuántos elementos tiene cada lista
            resultado.append((letra, len(letras_col4), len(pares)))

    return resultado
