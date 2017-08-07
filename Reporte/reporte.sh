#!/bin/bash

#montage *.png -tile 3x4 grafica.png

#echo "    Ponente " |  convert -background  none    -fill black \
#            -pointsize 18   text:-  -trim +repage  \
#            Titulo.png
for i in {0..5}; do
mv ${i}.jpeg ${i}/Titulo.jpeg
cd "${i}"

convert +append pregunta-1.png  pregunta-2.png  pregunta-3.png  pregunta-4.png row1.png
convert +append pregunta-5.png pregunta-6.png pregunta-7.png  pregunta-8.png row2.png
convert +append pregunta-9.png pregunta-10.png  pregunta-11.png pregunta-12.png row3.png
convert +append pregunta-13.png pregunta-14.png pregunta-15.png pregunta-16.png row4.png
#convert +append  row5.png

convert -append Titulo.jpeg row1.png row2.png row3.png row4.png  final.png
#cp row5.png final1.png
echo "Final${i}.png"

cd ..

mv ${i}/final.png ${i}-Final.png

done
