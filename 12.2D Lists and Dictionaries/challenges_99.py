array = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
for i in array:
    print(i)

ROW = int(input("Which row they want displayed:"))
while(ROW < 0 or ROW > 3):
    ROW = int(input("Which row they want displayed (choose an option between 0 and 3):"))
print("Value: ",array[ROW])

COLUMN = int(input("Which column in that row you want displayed: "))
while(COLUMN < 0 or COLUMN > 2):
    COLUMN = int(input("w\Which column in that row you want displayed (choose an option between 0 and 2): "))

print(" You choose the value: ",array[ROW][COLUMN])

user = input("Do you want to change the value (Y/N):")
user = user.upper()
if user == "Y":
    newdata = int(input("New Data: "))
    array[ROW][COLUMN] = newdata
    print("The row after change: ",array[ROW])
else:
    print("Program close! ")

