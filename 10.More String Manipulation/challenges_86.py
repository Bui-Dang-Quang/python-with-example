
password = input("Enter the password: ")
again = input("Enter again the password: ")

if password == again:
    print("Thank you!")
elif password.lower() == again.lower():
    #convert word(vd: password == dim & again == DiM) => dim == dim => print message
    print("They must be in the same case")
else:
    print("Incorrect")
