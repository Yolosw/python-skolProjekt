import math

def inputs():
    var1 = float(input("Första nummret: "))
    return var1

def circleArea(r):
    return math.pow(r, 2) * math.pi

def area(a1, a2):
    return a1 * a2

# Skapar en function som sedan kalkylerar hypotenusan med katerna. Funktionen tar tillbaka k1 och k2 genom return katet.
def kateter(k1, k2):
    katet = math.pow(k1, 2) + math.pow(k2, 2)
    return math.sqrt(katet)

def hypokater(k1, hypo):
    k2 = math.sqrt(hypo** 2 - k1** 2)
    return k2


val = int(input("\n 1. Cirkel Area,\n 2. Rektangel Area\n 3. Kvadrat Area \n 4.Pythogoras sats \n Svar: "))
enhet = input("Enhet: ")
# Välja mellan 4 olika val
match(val):
    case 1:
        var1 = float(input("Radien på circkeln: "))
        print(circleArea(var1), enhet)
    case 2:
        var1, var2 = inputs(), inputs()
        print(area(var1, var2), enhet)
    case 3:
        var1 = inputs()
        print(area(var1, var1), enhet)
    case 4:
        val2 = int(input("\n 1. båda kateter \n 2. Bara 1 katet: "))
        match(val2):
            case 1:
                var1, var2 = inputs(), inputs()
                print(kateter(var1, var2))
            case 2:
                var1, var2 = inputs(), inputs()
                print(hypokater(var1, var2), enhet)



""""
Så här gör du utan match men match är ett bättre val för den är 86% snabbare enligt vissa källor.

if val == 1:
    var1 = float(input("Radien på circkeln: "))
  
    print(circleArea(var1), enhet)
elif val == 2:
    var1, var2 = inputs(), inputs()
    
    print(area(var1, var2), enhet)
elif val == 3:
    var1 = inputs()
    
    print(area(var1, var1), enhet)
elif val == 4:
    val2 = int(input("1. båda kateter \n 2. Bara 1 katet: "))
  

    if val2 == 1:
        var1, var2 = inputs(), inputs()
        print(kateter(var1, var2))
    elif val2 == 2:
        var1 = float(input("katet: "))
        var2 = float(input("Hypotenusan: "))
        print(hypokater(var1, var2), enhet)
else:
    print("Felaktigt val")

"""""