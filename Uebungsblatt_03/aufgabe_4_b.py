#aufgabe 4b
#Schreiben Sie ein Programm, dass durch die Eingabe der Seiten a und b sowie der Hoehe c das Volumen und die Oberflaeche des Quarders berechnet:

print("Zur Berechnung von Volumen und Oberflaeche benötigen wir: Seitenlaenge a, Seitenlaenge b und die Höhe c")
seitenlaenge_a = float(input("Bitte Seitenlaenge a angeben:"))
seitenlaenge_b = float(input("Seitenlaenge b:"))
hoehe_c = float(input("Hoehe c:"))
print(f"Volumen: {seitenlaenge_a*seitenlaenge_b*hoehe_c}")
print(f"Gesamtoberfläche: {seitenlaenge_a*seitenlaenge_b*2+seitenlaenge_a*hoehe_c*2+seitenlaenge_b*hoehe_c*2}")


