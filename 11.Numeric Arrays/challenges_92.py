from array import *
import random
num1 = array ('i',[])
num2 = array ('i',[])
for i in range(0,3):
    user = int(input("Enter number: "))
    num1.append(user)

for j in range(0,5):
    newvalue = random.randint(1,100)
    num2.append(newvalue)

num1.extend(num2)
num1 = sorted(num1)
for i in num1:
    print(i)
