total = 0
for i in range(1,6):
    num = int(input("Enter the number: "))
    ans = input("Do u want that number included(Y/N): ")
    ans = ans.title()
    if(ans == "Y" or ans == "Yes"):
        total = total + num
    elif(ans == "N" or ans == "No"):
        print("Ok!")
    else:
        print("Wrong input statement!")

print("Result = ",total)

