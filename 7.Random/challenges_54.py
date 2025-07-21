import random
Choice = random.choice(["Head","Tail"])
User = input("Guess the side of the coin(Head/Tail): ")
User = User.title()
while(User != "Head" and User != "Tail"):
    User = input("Please type-in the correct response (Head/Tail): ")
    User = User.title()

if(User == Choice):
    print("You win")
else:
    print("Fuck u")