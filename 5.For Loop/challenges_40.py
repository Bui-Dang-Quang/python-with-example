number = int(input("Enter the number below 50: "))
while(number > 50 or number < 1):
    number = int(input("Please enter again the number below 50: "))

count = 0
for i in range(50,number-1,-1):
    print(i)
    count = count + 1

print("\nThe number of digit (include 50 and input number) between 50 and",number,"is", count)