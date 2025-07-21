from array import *
num = array ('f', [10.09, 55.45,65.42,22.33,75.24])
user = int(input("Enter a whole number between 2 and 5: "))

while user > 5 or user < 2:
    print("Error")
    user = int(input("Enter a whole number between 2 and 5: "))

for i in range(0,5):
    div = num[i]/user
    print(round(div,2))
