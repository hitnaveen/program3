

import turtle

# Turtle setup
pen = turtle.Turtle()
pen.speed(0)
pen.width(3)

colors = ["red", "yellow", "blue", "green", "orange", "purple"]

# Draw colorful spiral
for i in range(100):
    pen.pencolor(colors[i % len(colors)])
    pen.forward(i * 2)
    pen.right(90)

# Hide turtle
pen.hideturtle()

# Keep window open
turtle.done()