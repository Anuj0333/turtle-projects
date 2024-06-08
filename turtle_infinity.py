import turtle
from turtle import Turtle, Screen

tinny_turtle = Turtle()
s = Screen()
tinny_turtle.shape("turtle")
for _ in range(50):
    tinny_turtle.forward(10)
    tinny_turtle.penup()
    tinny_turtle.forward(10)
    tinny_turtle.pendown()


s.exitonclick()
