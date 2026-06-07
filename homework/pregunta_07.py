"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_07():
    """
    Retorne una lista de tuplas que asocia el valor de la columna 2 con la
    lista de letras (columna 1) que tienen ese valor, en el orden en que
    aparecen en el archivo.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

    """
    import os

    filepath = os.path.join(os.path.dirname(__file__), "..", "files", "input", "data.csv")

    # Diccionario: numero (col 2) -> lista de letras (col 1) en orden de aparición
    grupos = {}

    with open(filepath, "r") as f:
        for line in f:
            cols = line.strip().split("\t")
            letra = cols[0]
            numero = int(cols[1])

            if numero not in grupos:
                grupos[numero] = [letra]
            else:
                grupos[numero].append(letra)

    # Armamos lista de tuplas (numero, lista_de_letras) ordenadas por número
    resultado = []
    for numero in sorted(grupos):
        resultado.append((numero, grupos[numero]))

    return resultado
