color = []
for i in range(0,10):
    color.append(input("Enter the color: "))
print(color)
start = int(input("\nEnter number between 0 and 4: "))
end = int(input("Enter number between 5 and 9:"))
print("\n",color[start:end])