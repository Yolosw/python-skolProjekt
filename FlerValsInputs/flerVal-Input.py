val = int(input("\n 1. Hej \n 2. Hejdå \n Svar: "))
# Går att använda en string istället men då hade du inte använt en 1 i if statmentet då hade du använt "1"

# Här så kollar vi om val är 1 eller 2 sedan skriver vi ut hej eller hejdå beronde på vad val är.
if val == 1:
    print("Hej")
    # Skapar ett nytt val
    val2 = int(input("1. Tyst \n 2. Prata \n: Svar"))
    if val2 == 1:
        print("Tyst")
    elif val2 == 2:
        print("Prata")
elif val == 2:
    # Skapar ett nytt val
    print("Hejdå")
    val2 = int(input("1. Tyst \n 2. Prata \n: Svar"))
    if val2 == 1:
        print("Tyst")
    elif val2 == 2:
        print("Prata")
    

# Tar upp om du skriver fel
else:
    print("Felaktigt val")