file = open("Name.txt","w")
for i in range(0,5):
    name = input("Name: ")
    file.write(f"{name}\n")
file.close()