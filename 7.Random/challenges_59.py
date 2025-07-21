import random
color = random.choice(["Red","Blue","Green","Yellow","Black"])
user = input("Choose ur guess [Green, Blue,Yellow,Black,Red]: ")
user = user.title()
while(user != color):
    user = input("Choose another guess [Green, Blue,Yellow,Black,Red]: ")
    user = user.title()
    if(user == color):
        print("Well Done! ")
    else:
        if(color == "Red"):
            print("You are probably feeling RED right now")
        elif(color == "Blue"):
            print("You are probably feeling BLUE right now")
        elif(color == "Yellow"):
            print("You are probably feeling YELLOW right now")
        elif(color == "Green"):
            print("You are probably feeling GREEN right now")
        elif(color == "Black"):
            print("You are probably feeling DARK right now")
