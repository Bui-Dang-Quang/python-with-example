import turtle
turtle.color("black","red")
turtle.begin_fill()
for i in range(0,4):
    turtle.forward(70)
    turtle.right(90)
turtle.end_fill()
turtle.penup()
turtle.forward(100)

turtle.pendown()
turtle.color("black","blue")
turtle.begin_fill()
for i in range(0,4):
    turtle.forward(70)
    turtle.right(90)

turtle.end_fill()
turtle.penup()
turtle.forward(100)

turtle.pendown()
turtle.color("purple","gray")
turtle.begin_fill()
for i in range(0,4):
    turtle.forward(70)
    turtle.right(90)

turtle.end_fill()
turtle.penup()
turtle.forward(100)

turtle.exitonclick()