person = []
for i in range(0,3):
    person.append(input("Enter the person who get invite: "))
print(person)

ans = input("Do u want to add another person (Yes/No): ")
ans = ans.title()

while(ans != "No"):
    person.append(input("Enter the name: "))
    print(person)
    ans = input("Do u want to add another person (Yes/No): ")
    ans = ans.title()

print("\n Result: ", person)
print(" Length: ", len(person),"\n")

name = input("Enter the available name: ")
if(name in person):
    print(name,"is in the position",person.index(name))
    user = input("Do u still want that person to come to the party(Yes/No): ")
    user = user.title()
    if(user == "No"):
        person.remove(name)
        print(person)
    else:
        print("U accepted!")
else:
    print("Name not found in the list.")
