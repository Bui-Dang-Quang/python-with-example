list = {}
for i in range(0,4):
    name = input("Name: ")
    age = int(input("Age: "))
    size = int(input("Size: "))
    list[name] = {"Age":age,"Size":size}
for i in list:
    print(i,list[i])
print("\n")
for name in list:
    print((name),list[name]["Age"])

# user = input("\nName of one of the people in the list: ")
# print(user,list[user])
