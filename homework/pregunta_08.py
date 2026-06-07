"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Igual que pregunta_07 pero las letras de la lista deben estar ordenadas
    alfabéticamente y sin duplicados.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """
    import os

    filepath = os.path.join(os.path.dirname(__file__), "..", "files", "input", "data.csv")

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

    resultado = []
    for numero in sorted(grupos):
        # set() elimina duplicados, sorted() ordena alfabéticamente, list() lo vuelve lista
        letras_unicas_ordenadas = sorted(set(grupos[numero]))
        resultado.append((numero, letras_unicas_ordenadas))

    return resultado
