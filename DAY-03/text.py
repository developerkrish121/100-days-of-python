print("Welcome to the RollerCoaster")
height = int(input("What is your height in cm??"))
age = 43
if height>=120 :
    print("You can ride")
    if age>=18:
        print("big")
    else:
        print("small")    
else :
    print("You cannot ride")

# Modulo Operator

print(10%3)

number1 = int(input("Enter a number"))
if number1 % 2 == 0:
    print("Number is even")
else :
    print("Number is odd")