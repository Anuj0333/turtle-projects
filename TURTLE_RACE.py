from turtle import Turtle,Screen
import random

is_race_on=False
s=Screen()

s.setup(width=500,height=500)
user_bet=s.textinput(title="make your bet",prompt="which turtle wins the race? enter a color:")

 
tim=Turtle()
tim.penup()
tim.goto(-240,240)
tim.shape("turtle")
tim.color("red")

tom=Turtle()
tom.penup()
tom.goto(-240,160)
tom.shape("turtle")
tom.color("pink")

toe=Turtle()
toe.penup()
toe.goto(-240,80)
toe.shape("turtle")
toe.color("purple")

tae=Turtle()
tae.penup()
tae.goto(-240,0)
tae.shape("turtle")
tae.color("yellow")

tak=Turtle()
tak.penup()
tak.goto(-240,-80)
tak.shape("turtle")
tak.color("blue")

tel=Turtle()
tel.penup()
tel.goto(-240,-160)
tel.shape("turtle")
tel.color("brown")

tan=Turtle()
tan.penup()
tan.goto(-240,-240)
tan.shape("turtle")

all_turtle=[tim,tom,toe,tae,tak,tel,tan]


if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor()>490:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print(f"you've won! the {winning_color} turtle is the winner !")
            else:
                print(f"you've lost! the {winning_color} turtle is the winner !")
            
        random_distance=random.randint(0,10)
        turtle.forward(random_distance)




print(user_bet)
s.exitonclick()