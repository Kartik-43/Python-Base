import turtle
from turtle import Turtle, Screen
import random

random_walk = Turtle()
turtle.colormode(255)


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour


Direction = [0, 90, 180, 270]
random_walk.pensize(15)
random_walk.speed('fast')

for i in range(200):
    random_walk.color(random_colour())
    random_walk.forward(30)
    random_walk.setheading(random.choice(Direction))

screen = Screen()
screen.exitonclick()
