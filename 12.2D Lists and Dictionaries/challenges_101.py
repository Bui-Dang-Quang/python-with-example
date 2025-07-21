sale = {"John":{"N":3056,"S":8463,"E":8441,"W":2694},"Tom":{"N":4832,"S":6786,"E":4737,"W":3612},"Anne":{"N":5239,"S":4802,"E":5820,"W":1859},"Fiona":{"N":3904,"S":3645,"E":8821,"W":2451}}
print("\n")
for i in sale:
    print(i,sale[i])

name = input("Enter name: ")
while name not in sale:
    name = input("Enter name: ")

region = input("Enter region: ")
while region not in sale[i]:
    region = input("Enter region: ")

print("""\nYou choose: 
            1.Name:""",name,"""
            2.Region:""",region,"\n")

user = int(input("Enter a new value for the change: "))
sale[name][region] = user

print("Value: ",name,sale[name])
