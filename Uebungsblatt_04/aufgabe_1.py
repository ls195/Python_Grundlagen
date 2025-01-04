#Programm 'Raten' 
#Schreiben Sie ein Programm "Raten", in dem der Benutzer eine Ganzzahl erraten soll. Der Benutzer soll die Ganze Zahl eingeben können. Außerdem soll der Benutzer informiert werden, ob die Zahl zu klein oder zu groß war.

import random

target = random.randint(1,9)
try:
    s1 = int(input("Bitte geben Sie eine Ganzzahl ein:"))
    try:
        if s1 == target:
            print("Herzlichen Glückwunsch! Sie haben gewonnen!")
        elif s1 > target:
            print("Leider daneben, du hast zu hoch geschaetzt")
        elif s1 < target:
            print("Leider daneben, du hast zu tieft geschaertzt")
    except ValueError:
        print("Fehlerhafte Eingabe: 'ValueError'")

except ValueError:
    print("Fehlerhafte Eingabe: 'ValueError'")

