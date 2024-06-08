from turtle import Turtle,Screen
import turtle as t 
import random
import turtle
tim=t.Turtle()
t.colormode(255)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color=(r,g,b)
    return random_color
s=Screen()
direction=[0,90,270,180]

tim.width(15)
tim.speed("fastest")
for i in range(250):
    tim.forward(30) 
   
    tim.color(random_color())
    tim.setheading(random.choice(direction))
s.exitonclick()