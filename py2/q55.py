import math
print("Program to make a dictionary as a look up table")
d={"AFG":"Afghanistan", "ALB":"Albania", "DZA":"Algeria","AGO": "Angola","ATA":"Antarctica","ARG":"Argentina","ARM": "Armenia"}
d2={1:math.factorial(1), 2:math.factorial(2), 3:math.factorial(3),4:math.factorial(4),5:math.factorial(5),6:math.factorial(6),7:math.factorial(7)}
k=input("Enter the abbrevation for country")
k=k.upper()
print("Country is",d[k])
n=int(input("Enter the number whose factorial needs to be find out"))
print ("Factorial is",d2[n])

