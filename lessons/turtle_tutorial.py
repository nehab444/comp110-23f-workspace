"""Turtle practice."""

from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
colormode(255)

leo.color(99, 204, 250)

leo.penup()
leo.goto(45, 60)
leo.pendown()

i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1

done()