programmes = []
for i in range(0,4):
    programmes.append(input("Enter the TV programmes: "))

print("\n")
for i in programmes:
    print(i)
print("\n")

user = input("Enter another show: ")
position = int(input("Enter the desire position (enter by number): "))
programmes.insert(position,user)

print("\n")
for i in programmes:
    print(i)
print("\n")