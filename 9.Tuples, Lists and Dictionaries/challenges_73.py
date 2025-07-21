fav_food = {}
for i in range(1,5):
    fav_food[i] = input("Enter ur favourite food: ")
print(fav_food)

detest = int(input("which food u want to get rid of and remove it from the list (enter by number): "))
del fav_food[detest]
print(sorted(fav_food.values()))