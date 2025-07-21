from array import *
num = array ('i', [1,3,5,7,9])
user = int(input("Select one of the number in array: "))

while user not in num:
    print("Invailid Number")
    user = int(input("Select one of the number in array: "))

print(user,"is in the position",num.index(user))
