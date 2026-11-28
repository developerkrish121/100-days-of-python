print("Welcome to Python pizza deliveries")
size = input("What size do you want S, M or L ??")
pepperoni = input("Do you want pepporoni on your pizza : Y OR N")
extra_cheese = input("Do you want extra_cheese on your pizza : Y OR N")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill +=20
elif size == "L":
    bill += 25
else:
    print("You typed the wrong input")
    
    
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else :
        bill += 3

if extra_cheese == "Y":
    bill += 1
    
print(f"Your final bill is : ${bill}")