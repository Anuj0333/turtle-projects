'''below code which is commmented is for for retriving color list from image'''
# import colorgram

# rgb_colors=[]
# colors=colorgram.extract('C:/Users/ASUS/OneDrive/Documents/anuj_work\python_mini_projects/turtle_project/spots_paint.jpg', 30)
# print(colors)
# for i in colors:
#     r=i.rgb.r
#     g=i.rgb.g
#     b=i.rgb.b
#     new_color=(r,g,b)
#     rgb_colors.append(new_color)

# print(rgb_colors)




import turtle as turtle_module
import random 
turtle_module.colormode(255)
tim=turtle_module.Turtle()
color_list=[(248, 246, 235), (233, 251, 242), (252, 238, 248), (235, 243, 251), (234, 225, 93), (233, 49, 133), (213, 158, 105), (115, 177, 214), (212, 133, 177), (196, 75, 23), (193, 163, 14), (36, 103, 168), (33, 192, 111), (11, 22, 65), (235, 225, 2), (183, 45, 124), (122, 189, 156), (189, 10, 68), (23, 28, 169), (237, 161, 203), (12, 186, 220), (136, 222, 199), (237, 70, 36), (10, 41, 22), (46, 127, 68), (50, 21, 10), (124, 219, 233), (104, 92, 213), (172, 173, 235), (57, 15, 30)]
tim.penup( )
tim.hideturtle()
tim.speed("fastest")
tim.setheading(225)
tim.forward(300)
tim.setheading(0)


number_of_dots=100
for i in range(1,number_of_dots+1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)
    

    if i%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)





screen=turtle_module.Screen()
screen.exitonclick( )