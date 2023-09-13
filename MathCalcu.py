
import math
def circleArea(r):
    return  math.pow(r, 2) * math.pi
def area(a1, a2):
    return a1 * a2
def kateter(k1, k2):
    katet = math.pow(k1, 2) + math.pow(k2, 2)
    return(math.sqrt(katet))
def hypokater(k1, hypo):
    k2 = math.sqrt(hypo** 2 - k1** 2)
    return k2


val = int(input("\n 1. Cirkel Area,\n 2. Rektangel Area\n 3. Kvadrat Area \n 4.Pythogoras sats \n Svar: "))
enhet = str(input("Enhet: "))
if val == 1:
    var1 = float(input("Radien på circkeln: "))
    print(circleArea(var1), enhet)
elif val == 2:
    var1 = float(input("Första sidan: "))
    var2 = float(input("Andra sidan: "))
    print(area(var1, var2))
elif val == 3:
    var1 = float(input("Sidan: "))
    print(area(var1, var1), enhet)
elif val == 4:
    val2 = int(input("1. båda kateter \n 2. Bara 1 katet: "))

    if val2 == 1:
        var1 = float(input("Första katet: "))
        var2 = float(input("Andra katet: "))
        print(kateter(var1, var2))
    elif val2 == 2:
        var1 = float(input("katet: "))
        var2 = float(input("Hypotenusan: "))
        print(hypokater(var1, var2), enhet)
    
else:
    print("Felaktigt val")