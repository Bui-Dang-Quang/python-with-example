ans = input("Which direction will you choose? (Up/Down): ")
ans = ans.title()

if(ans == "Up"):
    topnum = int(input("Enter the top number: "))
    count = 0
    for i in range(0,topnum):
        count = count + 1
    print("From 1 to",topnum,", We have",count,"count")
elif(ans == "Down"):
    num = int(input("Enter the number below 20: "))
    while(num > 20 or num < 1):
        num = int(input("Please enter the number below 20: "))

    count1 = 0
    for i in range(20, num, -1):
        count1 = count1 + 1
    print("From 20 to",num,", We have",count1,"count")
else:
    print("IDU!")