# country_tuple = ("VN","CN","US","UK","FRA")
# print(country_tuple)
# country = input("Enter one of the countries: ").upper()
# print(country,"has index number",country_tuple.index(country),"\n")


# num = int(input("number ?"))
# print("The position of",num,"REFER to",country_tuple[num])

# ------------------------------------------------------------------------------////


countries = ("VN","CN","US","UK","FRA")
for i in range(0,5):
    print(countries[i])

num = int(input("Number: "))
if(num == 0 or num == 1 or  num == 2 or num == 3 or num == 4):
    print("The position of",num,"REFER to",countries[num])
else:
    print("Invalid !")
