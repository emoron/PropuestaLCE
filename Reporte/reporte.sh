#!/bin/bash
#csvcut -c 2 ponentes.csv | while read i; $j = 0; do echo "mv $j i"; $j++;  done

#montage *.png -tile 3x4 grafica.png

for i in {0..5}; do

cd "${i}"

convert +append pregunta-1.png  pregunta-2.png  pregunta-3.png   row1.png
convert +append pregunta-4.png pregunta-5.png pregunta-6.png  row2.png
convert +append pregunta-7.png pregunta-8.png pregunta-9.png  row3.png
convert +append pregunta-10.png pregunta-11.png pregunta-12.png row4.png
convert +append pregunta-13.png pregunta-14.png pregunta-15.png row5.png

convert -append row1.png row2.png row3.png row4.png final.png

echo "Final${i}.png"
cd ..


done
