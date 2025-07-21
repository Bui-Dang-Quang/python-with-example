raining = str.lower(input("It is raining ?(yes/no): "))
if raining == "yes":
    windy = str.lower(input("It is windy ?(yes/no)"))
    if windy == "yes":
        print("It is too windy for an umbrella")
    else:
        print("Take an umbrella")
else:
    print("Enjoy your day")
