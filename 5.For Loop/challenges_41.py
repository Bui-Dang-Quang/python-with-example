name = input("Name? ")
number = int(input("Number? "))

count = 0
if(number < 10):
    for i in range(1,number + 1):
        print(name)
        count = count + 1
    print("Ur name is printed in",count,"times")
else:
    for i in range(1,4):
        print("Too high!")