import random
num = random.randint(1,10)
user = int(input("Enter a number: "))
count = 1
while(user != num):
    if(user > num):
        print("Too high")
    else:
        print("Too low")
    user = int(input("Enter a number: "))
    count = count + 1


if(user == num): print("U get a right answer after",count,"attemps!")