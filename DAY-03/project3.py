print("Welcome to the treasure hunt. Your task is to find the treasure!")
answer1 = input('"You are at a crossroad Where do you want to go : "left" or "right"').lower()


if answer1 == "left":
    #continue to the game  
    choice2 = input('"you came to a lake . There si a lake . Which colour boat do you choose.  Type "wait" to wait for the boat . Type "swim" to swim"').lower()
    if choice2 == "wait":
        #game will continue
        choice3 = input('"You arrive at an island unharmed. Theere are total 3 doors . Which door would you choose?? "Yellow","Red" or "Blue""').lower()
        if choice3 == "red":
            print("Game Over")
        elif choice3 == "Yellow":
            print("Game Over")
        elif choice3 == "blue":
            print("You win")
        else:
            print("You choose a door that does not exist. Game over")
    else:
        print("Game over")
else:
    print("Game Over") 