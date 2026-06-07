"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor después del `:` es un número entero.
    Retorne la lista de tuplas (clave, valor_mínimo, valor_máximo) ordenadas
    alfabéticamente por clave.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    import os

    filepath = os.path.join(os.path.dirname(__file__), "..", "files", "input", "data.csv")

    # Diccionario: clave -> [minimo, maximo] vistos hasta ahora
    grupos = {}

    with open(filepath, "r") as f:
        for line in f:
            cols = line.strip().split("\t")
            # La columna 5 (índice 4) viene como "jjj:12,bbb:3,ddd:9"
            pares = cols[4].split(",")

            for par in pares:
                # Cada par es "clave:valor"
                clave, valor = par.split(":")
                valor = int(valor)

                if clave not in grupos:
                    grupos[clave] = [valor, valor]
                else:
                    if valor < grupos[clave][0]:
                        grupos[clave][0] = valor
                    if valor > grupos[clave][1]:
                        grupos[clave][1] = valor

    # Lista de tuplas (clave, minimo, maximo) ordenadas alfabéticamente
    resultado = []
    for clave in sorted(grupos):
        minimo = grupos[clave][0]
        maximo = grupos[clave][1]
        resultado.append((clave, minimo, maximo))

    return resultado
