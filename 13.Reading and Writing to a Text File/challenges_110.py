file = open("Name.txt","r")
print(file.read())
file.close()


file = open("Name.txt","r")
user = input("Choose Name:")
user = user + "\n"
for row in file:
    if row != user:
        file = open("Name2.txt","a")
        new = row
        file.write(new)
        file.close()
file.close()