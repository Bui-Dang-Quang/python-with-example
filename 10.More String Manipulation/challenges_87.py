# word = input("Enter Word: ")
# length = len(word)

# for i in range(length,0,-1):
#     position = word[i-1]
#     print(position)


word = input("Enter Word: ")
length = len(word)
num = 1

for i in word:
    position = length - num
    letter = word[position]
    print(letter)
    num = num + 1

