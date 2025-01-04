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
        guthaben = guthaben - kosten
        return float(guthaben)
    elif guthaben < kosten:
        return float(guthaben)

def guthaben_einzahlen(guthaben):
    e_status = True
    while e_status == True:
        einzahlung = float(input("Bitte Münzen (10ct, 20ct, 50ct, 1$$, 2$$) einwerfen:\n")) 
        print(f"Guthaben derzeit:\t\t\t{guthaben}$$.")
        if einzahlung == 0.1 or einzahlung == 0.2 or einzahlung == 0.5 or einzahlung == 1 or einzahlung == 2:
            guthaben += einzahlung
            print(f"Eingezahltes Guthaben:\t\t\t\t{guthaben} $$")
            antwort = int(input("Möchten Sir Ihr Guthaben weiter auffüllen?\n1\t-\tJA, weiter einzahlen.\n2\t-\tNEIN, zur Bestellung."))
            if antwort == 1:
                continue
            if antwort == 2:
               return guthaben
        else:
            print("Nur das Einzahlen mit den Münzen 10ct, 20ct, 50ct, 1$$ und 2$$ sind möglich.")



while run == True:
    print("\t\t\t\t\t\t\t")
    print("\t\t\t\t\t\t\t")
    print("---------------------------------------------------------")
    print("*********Guthaben einzahlen und auswählen:*********\n")
    print("Nr:\t-\tGetränk\t\t\t-\tKosten")
    print(f"1\t-\tWasser mit Kohlensäure\t-\t{wmc_cost} $$")
    print(f"2\t-\tWasser ohne Kohlensäure\t-\t{wwc_cost} $$")
    print(f"3\t-\tCola\t\t\t-\t{cola_cost} $$")
    print("4\t-\t#Automat beenden#\t-\t### ##")
    print("--------------------------------------------------------")

  
    try:
        guthaben  = guthaben_einzahlen(guthaben)
    except TypeError:
        print("\n\n*****MELDUNG*START*****\n\n\t\tEingabe fehlerhaft beim Guthaben: 'TypeError'\n\n*****MELDUNG*ENDE*****\n\n")
        
    except ValueError:
        print("\n\n*****MELDUNG*START*****\n\n\t\tEingabe fehlerhaft beim Guthaben: 'ValueError'\n\n*****MELDUNG*ENDE*****\n\n")

  
    try:
        e1 = int(input("Auswahl: "))
    except TypeError:
        print("\n\n*****MELDUNG*START*****\n\n\t\tEingabe fehlerhaft bei der Auswahl: 'TypeError'\n\n*****MELDUNG*ENDE*****\n\n")
        
    except ValueError:
        print("\n\n*****MELDUNG*START*****\n\n\t\tEingabe fehlerhaft bei der Auswahl: 'ValueError'\n\n*****MELDUNG*ENDE*****\n\n")
    

    try:
        match e1:   
            case 1:
                if wmc_count > 0:
                    print(f"Kosten:\t\t{wmc_cost}")
                    rg = pruefung(wmc_cost, guthaben)
                    if rg == None:
                        print("Sie erhalten ein Wasser mit Kohlensäure.")
                        wmc_count-=1
                        guthaben = rg
                    else:
                        if rg >= 0:
                            print("Sie erhalten ein Wasser mit Kohlensäure.")
                            print(f"Ihr Rückgeld: \t\t{round(rg,2)}$$")
                            wmc_count-=1
                        elif rg == -1:
                            print("Sie haben zu wenig Guthaben")
                            continue
                else:
                    print("\n\n*****MELDUNG*START*****\n\n\t\tWasser mit Kohlensäure ist leider ausverkauft!\n\n*****MELDUNG*ENDE*****\n\n")
            case 2:
                if wwc_count > 0:
                    print(f"Kosten:\t\t{wwc_cost}")
                    rg = pruefung(wwc_cost, guthaben)
                    if rg == None:
                        print("Sie erhalten ein stilles Wasser")
                        wwc_count-=1
                        guthaben = rg
                    else:
                        if rg >= 0:
                            print("Sie erhalten ein stilles Wasser")
                            print(f"Ihr Rückgeld: \t\t{round(rg,2)}$$")
                            wwc_count-=1
                        elif rg == -1:
                            print("Sie haben zu wenig Guthaben")
                            continue
                else:
                    print("\n\n*****MELDUNG*START*****\n\n\t\tWasser ohne Kohlensäure ist leider ausverkauft!\n\n*****MELDUNG*ENDE*****\n\n")
            case 3:
                if cola_count > 0:
                    print(f"Kosten:\t\t{cola_cost}")
                    rg = pruefung(cola_cost, guthaben)
                    if rg == None:
                        print("Sie erhalten eine Cola.")
                        cola_count-=1
                        guthaben = rg
                    else:
                        if rg >= 0:
                            print("Sie erhalten eine Cola.")
                            print(f"Ihr Rückgeld: \t\t{round(rg,2)}$$.")
                            cola_count-=1
                        elif rg == -1:
                            print("Sie haben zu wenig Guthaben")
                            continue
                else:
                    print("\n\n*****MELDUNG*START*****\n\n\t\tCola ist leider ausverkauft!\n\n*****MELDUNG*ENDE*****\n\n")            

            case 4:
                print("Programm beendet!")
                break
    except NameError:
        print("\n\n*****MELDUNG*START*****\n\n\t\tError: 'NameError'\n\n*****MELDUNG*ENDE*****\n\n")
