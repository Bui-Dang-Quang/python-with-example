import random
score = 0
for i in range(1,6):
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)
    sum = num1 + num2
    print(num1,"+",num2,"=")
    user = int(input("Enter answer: "))
    if(user == sum):
        score = score + 1
print("\nUr score",score,"out of 5")
if(score == 0):
    print("You're dumb AF! ")
elif(score == 1 and score ==2):
    print("Noob")
elif(score == 3):
    print("Decent!")
else:
    print("Excellent!")