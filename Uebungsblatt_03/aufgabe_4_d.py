#aufgabe_4_d
#Schreiben Sie ein Programm, dass durch die Eingabe des Radius r das Volumen und die Oberfläce der Kugel berechnet. 

import math
print("Volumen- und Oberflaechenrechner fuer eine Kugel 1.0")
r = float(input("Bitte geben Sie den Radius ein: "))
v = 4/3*r**3*math.pi
o = 4*r**2*math.pi
print(f"Das Volumen des Kreises betraegt: {round(v,2)}, die Oberflaeche des Kreises betraegt: {round(o,2)}")

