print(""" 
-------------------Choose the option-------------------------
|                                                           |
|   1. Square (length and area)                             |
|   2. Triangle (height and area)                           |
|                                                           |
-------------------------------------------------------------
""")

number = input("Enter a number: ")

if(number == "1"):
    squareside = int(input("Enter length for the side of the square: "))
    areasq = squareside * squareside
    print("Area of the square: ", areasq)
elif(number == "2"):
    base = int(input("Enter the length of the base of the triangle: "))
    height = int(input("Enter the height of the triangle: "))
    areatri = (base*height)/2
    print("Area of the triangle: ", areatri)
else:
    print("Incorrect option selected")