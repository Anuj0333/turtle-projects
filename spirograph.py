from turtle import Turtle,Screen
import random
import turtle as t

tim=t.Turtle()
s=Screen()
t.colormode(255)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color=(r,g,b)
    return random_color
tim.speed("fastest")
def draw_Spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)) :
        tim.color(random_color())
        tim.circle(100)
        current_heading=tim.heading()
        tim.setheading(current_heading+size_of_gap)
draw_Spirograph(5)




s.exitonclick()