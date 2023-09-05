import math


choose = float(input("Choose Method:\n \n 1.Area av cirkel.\n 2. Omkrets"))

if choose == 1:
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * radius ** 2
    print("The area of the circle is: ", area)

elif choose == 2:
    radius = float(input("Enter the radius of the circle: "))
    omkrets = 2 * math.pi * radius
    print("The circumference of the circle is: ", omkrets)


