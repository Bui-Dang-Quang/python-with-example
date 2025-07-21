people = int(input("How many people do you want to invite to a party: "))
if(people < 10 and people >= 1):
    for i in range(0,people):
        name = input("Name: ")
        print(name," has been invited")
elif(people >= 10):
    print("Too many people")
else:
    print("No one join!")