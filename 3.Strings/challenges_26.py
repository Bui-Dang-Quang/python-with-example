piglatin = input("Enter the word: ")
piglatin = piglatin.title()
firstword = piglatin[0]
length = len(piglatin)
rest = piglatin[1:length]

if(firstword != "A" and firstword != "E" and firstword !="I" and firstword != "O" and firstword != "U" ):
    newpig = rest + firstword + "ay"
    print("Pig latin after changes: " + newpig)
else:
    newpig = firstword + rest + "way"
    print("Pig latin after changes: " + newpig)