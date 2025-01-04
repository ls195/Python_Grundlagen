#Aufgabe 5
#Ändern sie das Programm ab, sodass die Hinweise die von Ihnen ausgegeben werden von dem Programm berücksichtigt werden können und so die Anzahl der Versuche auf ein Minimum reduziert wird.

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
obergr=100
untergr=1
s1 = random.randint(1,100)

while counter == 0 or counter > 0 and counter < 6:
    print("___________________________________")
    print(f"Aktuelle Runde: {counter}")
    print(f"Aktuelle Schätzung: {s1}") 
    if s1 == target:
        print("Der Computer hat richtig getippt und gewonnen!")
        print(f"Der Computer hat nur {counter} Versuche gebraucht!")
        break
    elif s1 > target:
        print("Daneben! Der Computer hat zu hoch geschaetzt")
        obergr=s1
        s1=random.randint(untergr, obergr)
        print("_______________________________")
        counter=counter+1
    elif s1 < target:
        print("Daneben! Der Computer hat zu tief geschaetzt")
        untergr = s1
        s1=random.randint(untergr,obergr)
        print("________________________________")
        counter=counter+1
        
if counter == 5:
    print("Maximale Anzahl von Versuchen erreicht!")
print("Thank you for visiting!")
        
