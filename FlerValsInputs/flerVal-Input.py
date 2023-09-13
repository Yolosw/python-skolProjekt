val = int(input("\n 1. Hej \n 2. Hejdå \n Svar: "))
# Går att använda en string istället men då hade du inte använt en 1 i if statmentet då hade du använt "1"

# Här så kollar vi om val är 1 eller 2 sedan skriver vi ut hej eller hejdå beronde på vad val är.


match(val):
    case 1:
        print("Hej")
        val2 = int(input("1. Tyst \n 2. Prata \n: Svar"))
        match(val2):
            case 1:
                print("Tyst")
            case 2:
                print("Prata")
    case 2:
        print("hejdå")
        val2 = int(input("1. Tyst \n 2. Prata \n: Svar"))
        match(val2):
            case 1:
                print("Tyst")
            case 2:
                print("Prata")  

    
