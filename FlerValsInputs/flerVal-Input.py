val = int(input("1. Hej \n 2. Hejdå"))
# Går att använda en string istället men då hade du inte använt en 1 i if statmentet då hade du använt "1"

# Här så kollar vi om val är 1 eller 2 sedan skriver vi ut hej eller hejdå beronde på vad val är.
if val == 1:
    print("Hej")
elif val == 2:
    print("Hejdå")

# Tar upp om du skriver fel
else:
    print("Felaktigt val")