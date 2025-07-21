num = 10
while (num > 0):
    print("There are ,",num,"green bottles hanging on the wall,",num,"green bottles hanging on the wall, and if 1 green bottle should accidentally fall")
    num = num - 1
    ans = int(input("How many green bottles will be hanging on the wall? :"))
    if(ans == num):
        print("There will be",num,"green bottles hanging on the wall\n")
    else:
        while(ans != num):
            print("No, try again!\n")
            ans = int(input("How many green bottles will be hanging on the wall? :"))
        

print("\nThere are no more green bottles hanging on the wall")
    