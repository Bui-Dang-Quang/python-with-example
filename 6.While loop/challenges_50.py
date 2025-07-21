number = int(input("Enter a number between 10 and 20: "))
while(number > 20 or number < 10):
    if(number > 20):
        print("Too high")
    elif(number < 10):
        print("Too low")
    number = int(input("Enter another number between 10 and 20: "))

print("Thank you !")
    
    