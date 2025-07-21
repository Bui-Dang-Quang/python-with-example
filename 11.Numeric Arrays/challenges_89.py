from array import *
import random
num = array ('i',[])
for i in range(0,5):
    newvalue = random.randint(1,100)
    num.append(newvalue)

for i in num:
    print(i)

