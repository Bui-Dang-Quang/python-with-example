file = open("Numbers.txt","w")
for i in range(0,5):
    number = input("Enter the number: ")
    file.write(f"{number},")

file.close()


# file = open("Numbers.txt", "w")

# for i in range(0, 5):
#     number = input("Enter the number: ")
#     file.write(f"{number},")

# # Move the cursor back and remove the trailing comma
# file.seek(file.tell() - 1, 0)
# file.truncate()

# file.close()
