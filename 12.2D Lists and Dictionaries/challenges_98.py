array = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
for i in array:
    print(i)

ROW = int(input("select a row: "))
print("Value: ",array[ROW])
user = int(input("enter a new value:"))
array[ROW].append(user)
print("Value: ",array[ROW])
