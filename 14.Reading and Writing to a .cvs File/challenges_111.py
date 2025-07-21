import csv
import pandas as pd



# import data
file = open("Books.csv","w")
file.write("Book Name,Author,Year Released\n")
for i in range(0,5):
    book = input("Enter Book's Name:")
    author = input("Enter Name Of Author: ")
    year = input("Year released: ")
    newRecord = f"{book},{author},{year}\n"
    file.write(str(newRecord))

file.close()

# Print table
book_data = pd.read_csv("Books.csv", header=0, sep=",")
print(book_data)



