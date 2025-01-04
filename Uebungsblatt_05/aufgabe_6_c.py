#Aufgabe 6 c

###Anzahl
wmc_count = 5
wwc_count = 5
cola_count = 5

#Kosten
wmc_cost = 1.90
wwc_cost = 2.10
cola_cost = 2.90

#guthaben 
guthaben = 0.0

###
run = True

###################FUNKTIONEN
def pruefung(kosten, guthaben):
    if guthaben > kosten:
        return guthaben-kosten
    elif guthaben < kosten:
        return -1



while run == True:
    print("\t\t\t\t\t\t\t")
    print("\t\t\t\t\t\t\t")
    print("---------------------------------------------------------")
    print("*********Bitte Guthaben einwerfen und auswählen:*********\n")
    print("Nr:\t-\tGetränk\t\t\t-\tKosten")
    print(f"1\t-\tWasser mit Kohlensäure\t-\t{wmc_cost} $$")
    print(f"2\t-\tWasser ohne Kohlensäure\t-\t{wwc_cost} $$")
    print(f"3\t-\tCola\t\t\t-\t{cola_cost} $$")
    print("4\t-\t#Automat beenden#\t-\t### ##")
    print("--------------------------------------------------------")

    
    try:
        e1 = int(input("Auswahl: "))
    except TypeError:
        print("\n\n*****MELDUNG*START*****\n\n\t\tEingabe fehlerhaft bei der Auswahl: 'TypeError'\n\n*****MELDUNG*ENDE*****\n\n")
        
    except ValueError:
        print("\n\n*****MELDUNG*START*****\n\n\t\tEingabe fehlerhaft bei der Auswahl: 'ValueError'\n\n*****MELDUNG*ENDE*****\n\n")
 
    try:
        guthaben  = float(input("Guthaben einwerfen: "))
    except TypeError:
        print("\n\n*****MELDUNG*START*****\n\n\t\tEingabe fehlerhaft beim Guthaben: 'TypeError'\n\n*****MELDUNG*ENDE*****\n\n")
        
    except ValueError:
        print("\n\n*****MELDUNG*START*****\n\n\t\tEingabe fehlerhaft beim Guthaben: 'ValueError'\n\n*****MELDUNG*ENDE*****\n\n")

   

    try:
        match e1:   
            case 1:
                if wmc_count > 0:
                    rg = pruefung(wmc_cost, guthaben)
                    if rg >= 0:
                        print("Sie erhalten ein Wasser mit CO2")
                        print(f"Ihr Rückgeld: \t\t{round(rg,2)}") 
                        wmc_count-=1
                    elif rg == -1:
                        print("Sie haben zu wenig Guthaben")
                        continue
                else:
                    print("\n\n*****MELDUNG*START*****\n\n\t\tWasser mit Kohlensäure ist leider ausverkauft!\n\n*****MELDUNG*ENDE*****\n\n")
            case 2:
                if wwc_count > 0:
                    rg = pruefung(wwc_cost, guthaben)
                    if rg >= 0:
                        print("Sie erhalten ein stilles Wasser")
                        print(f"Ihr Rückgeld: \t\t{round(rg,2)}")
                        wwc_count-=1
                    elif rg == -1:
                        print("Sie haben zu wenig Guthaben")
                        continue
                else:
                    print("\n\n*****MELDUNG*START*****\n\n\t\tWasser ohne Kohlensäure ist leider ausverkauft!\n\n*****MELDUNG*ENDE*****\n\n")
            case 3:
                if cola_count > 0:
                    rg = pruefung(cola_cost, guthaben)
                    if rg >= 0:
                        print("Sie erhalten eine cola")
                        print(f"Ihr Rückgeld: \t\t{round(rg,2)}")
                        cola_count-=1
                    elif rg == -1:
                        print("Sie haben zu wenig Guthaben")
                        continue
                else:
                    print("\n\n*****MELDUNG*START******\n\n\t\tCola ist leider ausverkauft!\n\n*****MELDUNG*ENDE*****\n\n")
            case 4:
                print("Programm beendet!")
                break
    except NameError:
        print("\n\n*****MELDUNG*START*****\n\n\t\tError: 'NameError'\n\n*****MELDUNG*ENDE*****\n\n")
