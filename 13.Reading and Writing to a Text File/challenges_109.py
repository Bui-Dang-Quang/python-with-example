import time
print(""" 
==========================Choice Selection================================
        1.Create a new File
        2.Display the file
        3.Add a new item to the file
        4.Exit the program
        Make a selection 1,2,3 or 4:
\n
""")
def Answer():
    while True:
        try:
            user = int(input("Make ur decision, choose number between 1-4: "))
            while user not in range(1,5):
                user = int(input("Make a proper decision, choose a number between 1-4: "))
        except ValueError:
            print("You have been type a wrong statement, Please try again!")
            time.sleep(1)
            continue
        
        if user == 1:
            sub = input("Enter subject: ")
            file = open("Subject.txt","w")
            file.write(sub + "\n")
            file.close()
        elif user == 2:
            file = open("Subject.txt","r")
            print(file.read())
        elif user == 3:
            moresub = input("Enter a new subject: ")
            file = open("Subject.txt","a")
            file.write(moresub + "\n")
            file.close()
        else: 
            if user == 4:
                return False

Answer()


        