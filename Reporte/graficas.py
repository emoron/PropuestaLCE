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
from PIL import Image,ImageDraw,ImageFont
import re

#sys.setdefaultencoding('utf8')


def leer(archivo):
    pon=[]
    with io.open(archivo, 'r', encoding='utf-8') as file:
        lines_ponentes = csv.reader(file)
        for i in lines_ponentes:
#            print i
            pon.append(i)
    return pon

def create_image_file(cadena,name="titulo.png", ext='png', size=(1900, 100), color=(255, 255, 255)):
    #filename  = os.getcwd()+"/"+path+"/"+name
    #print filename

    file_obj = open(name, 'w')
    image = Image.new("RGBA", size=size, color=color)
    usr_font = ImageFont.truetype("/Users/ale/anaconda/lib/python2.7/site-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSans.ttf", 59)
    d_usr = ImageDraw.Draw(image)
    d_usr = d_usr.text((40, 1), cadena, (0, 0, 0), font=usr_font)
    image.save(file_obj,ext)
    file_obj.close()

def crear_archivo(cadena="TEst",name='test.jpeg', ext='jpeg', size=(500, 1200), color=(255, 255, 255)):
    file_obj = open(name, 'w')
    image = Image.new("RGBA", size=size, color=color)
    usr_font = ImageFont.truetype(
        "/Users/ale/anaconda/lib/python2.7/site-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSans.ttf", 59)
    d_usr = ImageDraw.Draw(image)
    d_usr = d_usr.text((5, 125), cadena, (0, 0, 0), font=usr_font)
    image.save(file_obj, ext)
    file_obj.close()

def grafica(df,datos,valor,pregunta,directorio):
    salida = directorio+"pregunta-"+str(valor)+".png"
    print salida

    fig = ggplot(df, aes(x=str(valor))) + geom_bar() + xlab(pregunta[0])
    #+ ggtitle(datos[0]+datos[1])
    fig.save(salida)

archivos = leer('archivos.txt')
ponentes = leer('ponentes.csv')
preguntas = leer('preguntas.csv')

for i in range(len(ponentes)):
    create_image_file(unicode(ponentes[i][1]),str(i)+".jpeg")

     
for i in range(len(archivos)):
    os.mkdir(str(i))
    df = pd.read_csv("data/"+archivos[i][0])
    archivo = str(i)+"/"



    for j in range(1,17):
        nombre = ponentes[i][1]
        print nombre
        #create_image_file(nombre,str(i));
        grafica(df,ponentes[i],j,preguntas[j],archivo)
