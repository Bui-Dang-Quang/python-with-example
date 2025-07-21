# CACH 1:
# upper = input("Type an upper case word: ")

# while not upper.isupper():
#         print("This is not in uppercase")
#         upper = input("Type an upper case word: ")

# print("Uppercase")

#CACH 2:

upper = input("Type an upper case word: ")
ans = False
while not ans:
    if upper.isupper():
        print("UPPERCASE")
        ans = True
    else:
        print("Try again!")
        upper = input("Type an upper case word: ")

