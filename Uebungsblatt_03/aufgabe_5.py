#Etwickeln Sie ein Programm, welches dem Anwender unter Angabe von Startkapital (K0), Zinssatz (p) und Verzinsungszeitraum (n) ein Endkapital (Kn) ausgiebt.

print("Zinseszinsrechner 1.0")
print("Benötigte Informationen: ")
k0 = float(input("Wie hoch ist ihr Startkapital (in $):"))
p = float(input("Wie hoch ist der zugrunde liegende Zinssatz:"))
n = float(input("Für wie viele Jahre soll angelegt werden:"))
kn = k0*(p/100+1)**n

print(f"Mit einem Startkapital von {k0}, einem zugrundeliegenden Zinssatz von {p}% beträgt Ihr angelegtes Geld am Ende des Verzinsungszeitraumes von {n} Monaten:\n{round(kn,2)}$")
