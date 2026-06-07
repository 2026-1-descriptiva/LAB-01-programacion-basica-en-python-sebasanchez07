"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor máximo y mínimo de la columna 2
    por cada letra de la primera columna, ordenadas alfabéticamente.

    Rta/
    [('A', 9, 2),
     ('B', 9, 1),
     ('C', 9, 0),
     ('D', 8, 3),
     ('E', 9, 1)]

    """
    import os

    filepath = os.path.join(os.path.dirname(__file__), "..", "files", "input", "data.csv")

    # Diccionario: letra -> [minimo, maximo] vistos hasta ahora
    grupos = {}

    with open(filepath, "r") as f:
        for line in f:
            cols = line.strip().split("\t")
            letra = cols[0]
            numero = int(cols[1])

            if letra not in grupos:
                # Primera vez que vemos esta letra: min y max arrancan iguales
                grupos[letra] = [numero, numero]
            else:
                # Actualizamos min (índice 0) y max (índice 1)
                if numero < grupos[letra][0]:
                    grupos[letra][0] = numero
                if numero > grupos[letra][1]:
                    grupos[letra][1] = numero

    # Armamos la lista de tuplas (letra, maximo, minimo) ordenadas por letra
    resultado = []
    for letra in sorted(grupos):
        minimo = grupos[letra][0]
        maximo = grupos[letra][1]
        resultado.append((letra, maximo, minimo))

    return resultado
