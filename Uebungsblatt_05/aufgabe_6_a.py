run = True
while run == True:
    print("Getränkeautomat gestartet:")
    print("Menu:")
    print("Wählen sie aus: ")
    print("1\t-\tWasser mit Kohlensäure")
    print("2\t-\tWasser ohne Kohlensäure")
    print("3\t-\tCola")
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
                print("Sie erhalten ein Wasser mit CO2")
            case 2:
                print("Sie erhalten ein stilles Wasser")
            case 3:
                print("Sie erhalten eine Cola")
            case 4:
                print("Programm beendet!")
                break
    except NameError:
        print("Error: 'NameError'")
