from turtle import Turtle, Screen

square = Turtle()
square.color('red')
square.shape('classic')

for i in range(4):
    square.forward(100)
    square.left(90)

square.hideturtle()

screen = Screen()
screen.exitonclick()
