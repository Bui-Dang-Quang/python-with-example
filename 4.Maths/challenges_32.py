import math
radius = int(input("Enter the radius: "))
depth = int(input("Enter the depth: "))
circle = math.pi * math.pow(radius,2)
volume = circle * depth
print(round(volume,3))