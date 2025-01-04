#aufgabe 4c
#Schreien Sie ein Programm, dass durch die Eingabe des Radius r und der Höhe h das Volumen und die Oberfläche des Zylinders berechnet.

import math
r = float(input("Bitte Radius in cm angeben: "))
h = float(input("Bitte Hoehe in cm angeben: "))

oberflaeche = (2*math.pi*r) +(2*math.pi*r*h)

print(f"Die Oberflaeche des Zylinders betraegt: {oberflaeche}cm.")
