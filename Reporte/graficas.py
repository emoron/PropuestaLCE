#encoding='utf-8'
# Es necesario reiniciar el sys antes de llamar a setdefault

from ggplot import *
import pandas as pd
import matplotlib as plt
import codecs
import csv
import sys
import io
import os

#sys.setdefaultencoding('utf8')


def leer(archivo):
    pon=[]
    with io.open(archivo, 'r', encoding='utf-8') as file:
        lines_ponentes = csv.reader(file)
        for i in lines_ponentes:
            print i
            pon.append(i)
    return pon


def grafica(df,datos,valor,pregunta,directorio):
    salida = directorio+"pregunta-"+str(valor)+".png"
    print salida
    fig = ggplot(df, aes(x=str(valor))) + geom_bar() + xlab(pregunta[0])
    #+ ggtitle(datos[0]+datos[1])
    fig.save(salida)

archivos = leer('archivos.txt')
ponentes = leer('ponentes.csv')
preguntas = leer('preguntas.csv')

for i in range(len(archivos)):
    os.mkdir(str(i))
    df = pd.read_csv(archivos[i][0])
    archivo = str(i)+"/"

    for j in range(1,17):
        grafica(df,ponentes[i],j,preguntas[j],archivo)
