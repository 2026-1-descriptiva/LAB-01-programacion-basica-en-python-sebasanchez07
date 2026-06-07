"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
    import os

    # 1) Construimos la ruta al archivo data.csv (subimos un nivel desde /homework)
    filepath = os.path.join(os.path.dirname(__file__), "..", "files", "input", "data.csv")

    # 2) Diccionario vacío: mes -> cantidad de registros
    conteo = {}

    # 3) Abrimos el archivo y leemos línea por línea
    with open(filepath, "r") as f:
        for line in f:
            # 4) Quitamos el salto de línea y separamos por tabulador
            cols = line.strip().split("\t")
            # 5) Tomamos la columna 3 (índice 2) que es la fecha "YYYY-MM-DD"
            fecha = cols[2]
            # 6) Extraemos el mes: caracteres en posiciones 5 y 6 -> "MM"
            #    Ej: "1999-02-28"[5:7] = "02"
            mes = fecha[5:7]
            # 7) Sumamos 1 al contador de ese mes (si no existe, arranca en 0)
            conteo[mes] = conteo.get(mes, 0) + 1

    # 8) Ordenamos alfabéticamente y devolvemos la lista de tuplas
    return sorted(conteo.items())
