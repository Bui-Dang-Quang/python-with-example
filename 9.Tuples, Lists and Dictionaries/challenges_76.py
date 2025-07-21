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