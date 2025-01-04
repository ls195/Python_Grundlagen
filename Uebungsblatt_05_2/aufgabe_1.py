#aufgabe 1a: Liste alle Katzennamen auf:

names = ["Luna","Simba","Nala","Leo","Liili","Charly","Lucy","Balu","Mia","Findus","Mimi","Sammy","Maja","Felix","Bella","Loki","Mila","Max","Frida","Tiger"]

print(names[::2])

#aufgabe 1b: Liste alle Katernamen auf:
print(names[1::2])

#aufgbae 1c: Liste die hintersten drei auf:
print(names[-3::])

#aufgane 1d: Ändern sie die Reihenfolge. Luna tauscht den Platz mit Frida
print(f"Index Luna: ", names.index("Luna"))
print(f"Index Frida: ", names.index("Frida"))
index_luna = names.index("Luna")
index_frida = names.index("Frida")
names[index_luna]="Frida"
names[index_frida]="Luna"
print(names)

#afgabe 1e: wie viele tiernamen befinden sich in der Liste?
print(len(names))

#aufgabe 1f: sortiere die Liste gemäß ihrer Länge aufsteigend
names2 = sorted(names, key=len)
print(names2)

#aufgabe 1g: Prüfen sie ob Kater Charly in der Liste enthalten ist:
names

if "Charly" in names:
    print("Charly gefunden", names.index("Charly"))


