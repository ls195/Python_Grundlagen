#Aufgabe 4
#Ändern sie das Programm ab, sodass der Benutzer nun eine zu erratene Zahl festlegen kann. Das Programm muss nun die Zahl des Benutzers erraten.

import random

try:
    target = int(input("Bitte Ziel-Ganzzahl zwischen 1 und 100 angeben: "))
except ValueError:
    print("Fehlerhafte Eingabe: 'ValueError'")
except TypeError:
    print("Fehlerhafte Eingabe: 'TypeError'")
except NameError:
    print("Fehlerhafte Eingabe: 'NameError'")
counter= 0

while counter <=4:
        
    s1 = random.randint(1,100)
    print(f"Schaetzung des Computers: {s1}")
    try:
        if s1 == target:
            print("Der Computer hat richtig getippt und gewonnen!")
            break
        elif s1 > target:
            print("Daneben! Der Computer hat zu hoch geschaetzt")
            counter=counter+1
        elif s1 < target:
            print("Daneben! Der Computer hat zu tief geschaetzt")
            counter=counter+1
    except NameError:
        print("Fehlerhafte Eingabe: 'NameError'")
        break 
    finally:
        print("Vielen Dank fürs Mitspielen!")
print("Maximale Versuche erreicht:\nAnzahl Versuche: 5")
        
