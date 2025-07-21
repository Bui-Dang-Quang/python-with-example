from array import *
num = array ('i',[])
for i in range(0,3):
    newvalue = int(input("Enter number: "))
    num.append(newvalue)
num = sorted(num)
print(num)

user = int(input("Select one of the number in array: "))
if user in num:
    num.remove(user)
    print(num)
else:
    print("Invailid Number")