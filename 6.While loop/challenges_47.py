num1 = int(input("Enter the first number: "))
sum = num1
ans = input("Do u want to add another number(Y/N): ")
ans = ans.title()
while(ans == "Y"):
    num2 = int(input("Enter another number: "))
    sum = sum + num2
    ans = input("Do u want to add another number(Y/N): ")
    ans = ans.title()

print(sum)