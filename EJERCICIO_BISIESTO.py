year = int(input("Introduce un año:"))
divido4= year % 4
dividido100= year % 100
dividido400= year % 400
if year<1582:
    print ("No dentro del calendario Gregoriano")
else:
    if divido4 != 0:
        print ("COMUN")
    elif dividido100 ==0:
        print ("BISIESTO")
    elif dividido400 ==0:
        print ("BISIESTO")
    else:
        print ("BISIESTO")

