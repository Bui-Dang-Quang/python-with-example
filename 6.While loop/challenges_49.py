compnum = 50
count = 1
number = int(input("Enter a number: "))
while(number != compnum):
    if(number > compnum):
        print("Ur guess is too high !")
    else:
        print("Ur guess is too low !")
    count = count + 1
    number = int(input("Enter another number: "))

print("Well done, you took",count,"attempts")