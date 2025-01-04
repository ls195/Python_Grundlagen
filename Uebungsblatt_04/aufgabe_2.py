#Programm 'Raten' 
#Aufgabe1: Schreiben Sie ein Programm "Raten", in dem der Benutzer eine Ganzzahl erraten soll. Der Benutzer soll die Ganze Zahl eingeben können. Außerdem soll der Benutzer informiert werden, ob die Zahl zu klein oder zu groß war.
#Aufgabe2: Erweitern sie Ihr Programm, sodass nach 5 Versuchen das Programm mit einer Meldung abbricht (bspw. Die max. Anzahl an Versuchen wurde erreicht!).

import random


counter = 0
target = random.randint(1,9)

while counter <=4:
    try:
        s1 = int(input("Bitte geben Sie eine Ganzzahl ein:"))
        try:
            if s1 == target:
                print("Herzlichen Glückwunsch! Sie haben gewonnen!")
                counter=counter+1
            elif s1 > target:
                print("Leider daneben, du hast zu hoch geschaetzt")
                counter=counter+1
            elif s1 < target:
                print("Leider daneben, du hast zu tieft geschaetzt")
                counter=counter+1
        except ValueError:
            print("Fehlerhafte Eingabe: 'ValueError'")
    except ValueError:
        print("Fehlerhafte Eingabe: 'ValueError'")
print("Maximale Versuche erreicht:\nAnzahl Versuche: 5")
        
