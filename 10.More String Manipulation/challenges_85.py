name = input("Name: ")
count = 0
name = name.lower()
for i in name:
    if i == "a" or i =="e" or i == "i" or i == "o" or i == "u":
        count = count + 1

print("Name: ",name,"Vowels: ",count)