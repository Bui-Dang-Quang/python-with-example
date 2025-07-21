import random
import turtle

color = random.choice(["red","blue","black","green","gray","brown"])
for i in range(0,8):
    turtle.pensize(4)
    turtle.color(color)
    turtle.right(45)
    turtle.forward(100)


turtle.exitonclick()