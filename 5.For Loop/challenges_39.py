number = int(input("Enter the number from 1 to 12: "))
while(number < 1 or number > 12):
    number = int(input("Enter the number from 1 to 12: "))
    
for i in range(1,13):
    times = i*number
    print(i,"x",number,"=",times)
