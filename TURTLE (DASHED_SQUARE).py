import turtle as t

dash = t.Turtle()

dash.color('green')
dash.shape('circle')

for i in range(10):
    dash.forward(10)
    dash.penup()
    dash.forward(10)
    dash.pendown()

dash.left(90)
for b in range(10):
    dash.forward(10)
    dash.penup()
    dash.forward(10)
    dash.pendown()

dash.left(90)
for d in range(10):
    dash.forward(10)
    dash.penup()
    dash.forward(10)
    dash.pendown()

dash.left(90)
for c in range(10):
    dash.forward(10)
    dash.penup()
    dash.forward(10)
    dash.pendown()

dash.hideturtle()

screen = t.Screen()
screen.exitonclick()
