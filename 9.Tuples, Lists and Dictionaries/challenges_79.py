nums = []
for i in range(0,3):
    num = input("Enter the number: ")
    nums.append(num)
print(nums)

user = input("Do u still want the last number? (Yes/No): ")
user = user.title()
if(user == "No"):
    nums.remove(num) #remove the last element
    print(nums)
else:
    print("Nothing happend! ")

