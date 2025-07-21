firstname = input("Enter name: ")
if len(firstname) < 5:
    surname = input("Enter surname: ")
    fullname = firstname + surname
    print(fullname.upper())
else:
    print(firstname.lower())
    