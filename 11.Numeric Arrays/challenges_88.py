from array import * 
num = array ('i',[])
for i in range(0,5):
    newvalue = int(input("Enter number: "))
    num.append(newvalue)

num = sorted(num)
print(num)
num.reverse()
print(num)