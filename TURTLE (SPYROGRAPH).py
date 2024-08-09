import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
spirograph = Turtle()
turtle.colormode(255)


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour


spirograph.speed(11)


def draw_spirograph(size):
    for _ in range(int(360 / size)):
        spirograph.color(random_colour())
        spirograph.circle(100)
        spirograph.setheading(spirograph.heading() + size)


num = screen.numinput(title='Input for the GAP', prompt='Enter the GAP between each circle : ')
draw_spirograph(num)


screen.exitonclick()
