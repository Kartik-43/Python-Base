from turtle import Turtle, Screen
import random
import turtle


turtle.colormode(255)
shapes = Turtle()
shapes.pensize(8)
shapes.speed('slow')
Shapes = ['square', 'arrow', 'circle', 'turtle', 'triangle', 'classic']


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        shapes.forward(100)
        shapes.right(angle)


def draw_inv(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        shapes.forward(100)
        shapes.left(angle)


for shape in range(3, 11):

    for x in Shapes:
        shapes.shape(random.choice(Shapes))
    for i in range(11):
        shapes.color(random_colour())
    draw_shape(shape)
    draw_inv(shape)


screen = Screen()
screen.exitonclick()
