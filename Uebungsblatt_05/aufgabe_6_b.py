
###Anzahl
wmc = 5
wwc = 5
cola = 5
###
run = True

print("Getränkeautomat wurde gestartet")
while run == True:
    print("Menu:")
    print("Wählen sie aus: ")
    print("1\t-\tWasser mit Kohlensäure\t-\t1,90 $$")
    print("2\t-\tWasser ohne Kohlensäure\t-\t2,10 $$")
    print("3\t-\tCola\t\t\t-\t2,90 $$")
    print("4\t-\t#Automat beenden#")
   


    try:
        e1 = int(input("Auswahl: "))
    except TypeError:
        print("Error: 'TypeError'")
    except ValueError:
        print("Error: 'ValueError'")
        
    try:
        match e1:   
            case 1:
                if wmc > 0:
                    print("Sie erhalten ein Wasser mit CO2")
                    wmc-=1
                else:
                    print("\n\n*****MELDUNG*START*****\n\n\t\tWasser mit Kohlensäure ist leider ausverkauft!\n\n*****MELDUNG*ENDE*****\n\n")
            case 2:
                if wwc > 0:
                    print("Sie erhalten ein stilles Wasser")
                    wwc-=1
                else:
                    print("\n\n*****MELDUNG*START*****\n\n\t\tWasser ohne Kohlensäure ist leider ausverkauft!\n\n*****MELDUNG*ENDE*****\n\n")
            case 3:
                if cola > 0:
                    print("Sie erhalten eine Cola")
                    cola-=1
                else:
                    print("\n\n*****MELDUNG*START******\n\n\t\tCola ist leider ausverkauft!\n\n*****MELDUNG*ENDE*****\n\n")
            case 4:
                print("Programm beendet!")
                break
    except NameError:
        print("Error: 'NameError'")
