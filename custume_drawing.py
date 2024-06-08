from turtle import Turtle,Screen
tim=Turtle()
s=Screen()

def move_forwards():
    tim.forward(10)
def move_backwards():
    tim.backward(10)
def move_right():
    tim.right(10)
    tim.heading()
def move_left():
    tim.left(10)
    tim.heading()
def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    
s.listen()
s.onkey(key="W",fun=move_forwards)
s.onkey(key="X",fun=move_backwards)
s.onkey(key="A",fun=move_right)
s.onkey(key="S",fun=move_left)
s.onkey(key="C",fun=clear_screen)
s.exitonclick()