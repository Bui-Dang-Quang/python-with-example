from array import *
num = array ('i', [1,3,5,7,9,9])
print("Array info: ",num)
user = int(input("Enther Number: "))
if num.count(user) == 1:
    print(user,"appears only once")
else:
    print(user,"have been repeated",num.count(user),"time")