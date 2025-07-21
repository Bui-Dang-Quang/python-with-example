new_name = input("Enter new name:")
file = open("Name.txt","a")
file.write(f"{new_name}\n")
file.close()