number = [123, 433, 998, 973]
# separate line of the list:
for i in number:
    print(i)
num = int(input("Enter number: "))
if num in number:
    print(num, "is in the list and its in position",number.index(num))
else:
    print("Not in the list!")
