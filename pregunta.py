"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re

def ingest_data():

    with open('clusters_report.txt') as clusters_report:
        rows = clusters_report.readlines()

    # drop first 4 rows
    rows = rows[4:]

    # list of clusters
    clusters = []
    cluster = [0, 0, 0, '']

    for row in rows:
        if re.match('^ +[0-9]+ +', row):
            number, qty, percentage, * words = row.split()
        
            # cast units
            cluster[0] = int(number)
            cluster[1] = int(qty)
            cluster[2] = float(percentage.replace(',','.'))

            # save key words
            words.pop(0) # drop '%'
            words = ' '.join(words)
            cluster[3] += words

        # rows of cluster with keywords
        elif re.match('^ +[a-z]', row):
            words = row.split()
            words = ' '.join(words)
            cluster[3] += ' ' + words

        elif re.match('^\n', row) or re.match('^ +$', row):
            cluster[3] = cluster[3].replace('.', '')
            clusters.append(cluster)
            cluster = [0, 0, 0, '']

    data_frame = pd.DataFrame (clusters, columns = ['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave'])
    return data_frame