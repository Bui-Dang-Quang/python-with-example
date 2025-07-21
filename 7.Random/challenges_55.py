import random
Rand = random.randint(1,5)
user = int(input("User's guess: "))
if(user == Rand):
    print("Well done")
else:
    if(user > Rand or user < Rand):
        user2 = int(input("User's second guess: "))
        if(user2 == Rand):
            print("Correct")
        else:
            print("You loose")