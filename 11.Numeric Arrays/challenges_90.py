from array import *
num = array ('i', [])
while(len(num) != 5 ):
    number = int(input("Enter number: "))
    if number >=10 and number <= 20:
        num.append(number)
    else:
        print("Outside the range")

if(len(num) == 5):
    print("Thank you")

for i in num:
    print(i)