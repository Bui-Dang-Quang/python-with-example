count = 0
ans = input("Do u want to invite someone ? (Y/N): ")
ans = ans.title()
while(ans == "Y"):
    name = input("Name: ")
    print(name,"has now been invited")
    count = count + 1
    ans = input("Do u want to invite another ? (Y/N): ")
    ans = ans.title()

print("U invited about",count,"people")