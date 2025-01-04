#Aufgabe 6
#Schreiben Sie ein Programm, dass eine übergebene Jahreszahl (Format: YYYY) auf ein Schaltjahr überprüft. Hierzu sollten Sie wissen, dass ein Schaltjahr vorliegt, wenn die Jahreszahl ohne Rest durch 400 teilbar ist. Ist die Jahreszahl durch 100 ohne Rest teilbar, dann ist es kein Schaltjahr. Ist die Zahl durch 4 ohne Rest teilbar, dann ist es ein Schaltjahr. Alle anderen Jahreszahlen sind keineSchaltjahre. Testen Sie im Anschluss ihre Funktion durch einige Aufrufe.


print("Schaltjahresprüfer")
def schaltjahrespruefer(jz):
    if jz%400==0:
        print("Es ist ein Schaltjahr")
    elif jz%100==0:
        print("Es ist KEIN Schaltjahr")
    elif jz%4==0:
        print("Es ist ein Schaltjahr")
    else:
        print("Es ist kein Schaltjahr")

try:
    jahr = int(input("Bitte geben Sie eine Jahreszahl an: "))
except ValueError:
    print("Falsche Eingabe 'ValueError'")

schaltjahrespruefer(jahr)


