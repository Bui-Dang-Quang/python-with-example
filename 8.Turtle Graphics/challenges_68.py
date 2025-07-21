import random
import turtle

line = random.randint(1,50)


for i in range(line):
    length = random.randint(25,100)
    rotate = random.randint(1,360)
    turtle.forward(length)
    turtle.right(rotate)

turtle.exitonclick()