import sys
import sys
import io
import os
from PIL import Image,ImageDraw,ImageFont

reload(sys)
sys.setdefaultencoding('utf8')

def create_image_file(cadena,path,name="titulo.png", ext='png', size=(1900, 100), color=(255, 255, 255)):
    #filename  = os.getcwd()+"/"+path+"/"+name
    #print filename

    file_obj = open(name, 'w')
    image = Image.new("RGBA", size=size, color=color)
    usr_font = ImageFont.truetype("/Users/ale/anaconda/lib/python2.7/site-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSans.ttf", 59)
    d_usr = ImageDraw.Draw(image)
    d_usr = d_usr.text((40, 1), cadena, (0, 0, 0), font=usr_font)
    image.save(file_obj,ext)
    file_obj.close()

def crear_archivo(cadena="TEst",name='test.jpeg', ext='jpeg', size=(1900, 100), color=(255, 255, 255)):
    file_obj = open(name, 'w')
    image = Image.new("RGBA", size=size, color=color)
    usr_font = ImageFont.truetype(
        "/Users/ale/anaconda/lib/python2.7/site-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSans.ttf", 59)
    d_usr = ImageDraw.Draw(image)
    d_usr = d_usr.text((0, 0), cadena, (0, 0, 0), font=usr_font)
    image.save(file_obj, ext)
    file_obj.close()



for i in range(len(ponentes)):
    create_image_file(ponentes[i][1]+".jpeg")
