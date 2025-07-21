import random
num = random.randint(1,10)
user = int(input("Enter a number: "))
while(user != num):
    user = int(input("Enter a number: "))

if(user == num): print("U get a right answer!")