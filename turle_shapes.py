from turtle import Turtle,Screen
import turtle as t
import random
import turtle 
tim=t.Turtle()
color=["chocolate1","brown2","azure4","lightCoral","khaki4"]
s=Screen()
def draw_shapes(num_sides):
        
    for i in range(num_sides):
            
        angle =360/ num_sides
        tim.forward(100)
        tim.left(angle)
        # tim.circle(angle)
for shape_side_n in range(3,11):
     tim.color(random.choice(color))
     draw_shapes(shape_side_n)


s.exitonclick()
