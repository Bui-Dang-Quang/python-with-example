import csv
file = open("Stars.csv","w")
newRecord = "Brian,73,Taurus\n"
file.write(str(newRecord))
file.close()

file = open("Stars.csv", "a")
name = input("Enter name: ")
age = input("Enter age: ")
star = input("Enter star sign: ")
newRecord = name + "," + age + "," + star + "\n"
file.write(newRecord)
file.close()

print("\n")
file = open("Stars.csv","r") 
for row in file: 
 print(row)


print("\n")
file = open("Stars.csv","r")  
reader = csv.reader(file) 
rows = list(reader) 
print(rows[1]) 



file = open("Stars.csv", "r")
search = input("Enter the data you are searching for: ")

reader = csv.reader(file)

# Loop through each row in the CSV file
for row in reader:
    # Check if the search term is in any field of the row
    if search in row:
        print(row)

file.close()

file = list(csv.reader(open("Stars.csv"))) 
tmp = [] 
for row in file: 
 tmp.append(row)

file = open("NewStars.csv", "w", newline="")  # Open file in write mode
x = 0

for row in tmp:
    newRec = f"{tmp[x][0]},{tmp[x][1]},{tmp[x][2]}\n"  # Use f-string for better readability
    file.write(newRec)
    x = x + 1

file.close()
