# import colorgram
# rgb_colors = []
# colors = colorgram.extract('hirst-1.jpg', 50)
# for color in colors:
# r = color.rgb.r
# g = color.rgb.g
# b = color.rgb.b
# new_color = (r, g, b)
# rgb_colors.append(new_color)
# print(rgb_colors)


'''                                         CODE START NOW                                         '''


import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)

hirst = Turtle()
hirst.speed('fast')
hirst.penup()
hirst.shape('circle')
color_list = [(240, 241, 245), (239, 236, 230), (243, 238, 242), (236, 241, 238), (194, 160, 120), (72, 92, 125),
              (143, 87, 59), (216, 209, 122), (140, 160, 188), (183, 147, 162), (29, 33, 46), (119, 73, 92),
              (56, 35, 26), (174, 160, 42), (139, 174, 153), (78, 115, 80), (62, 30, 40), (139, 27, 18), (118, 29, 40),
              (182, 101, 87), (47, 59, 92), (174, 99, 115), (102, 120, 167), (33, 51, 45), (103, 155, 87),
              (214, 176, 190), (216, 181, 174), (66, 83, 28), (164, 208, 188), (182, 187, 212), (218, 206, 11),
              (49, 71, 60), (171, 200, 208), (109, 135, 143), (49, 72, 77)]

hirst.setheading(225)
hirst.forward(300)
hirst.setheading(0)

number_of_dots = 100

for dots in range(1, number_of_dots + 1):
    hirst.dot(20, random.choice(color_list))
    hirst.forward(50)

    if dots % 10 == 0:
        hirst.setheading(90)
        hirst.forward(50)
        hirst.setheading(180)
        hirst.forward(500)
        hirst.setheading(0)

hirst.hideturtle()

screen = Screen()
screen.exitonclick()
