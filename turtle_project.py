
from turtle import Turtle,Screen

t=Turtle()
s=Screen()
t.shape("turtle")
t.color("SeaGreen")
for steps in range(75):
    for c in ('blue', 'red', 'green'):
        t.color(c)
        t.forward(75)
        t.right(30)
print(t, s.canvheight)
s.exitonclick()