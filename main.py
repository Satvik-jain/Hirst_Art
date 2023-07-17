# Getting color from a picture
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     color_list = []
#     for _ in color.rgb:
#         color_list.append(_)
#     rgb_colors.append(tuple(color_list))
# print(rgb_colors)

from random import choice
from turtle import Turtle, Screen, colormode

color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
              (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
              (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
              (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64),
              (107, 127, 153), (176, 192, 208), (168, 99, 102)]

# each circle is having radius 20 and distance between the circles is 50.

colormode(255)
tim = Turtle()
tim.hideturtle()
tim.speed('fastest')
tim.penup()
tim.goto(-300, -300)
tim.pendown()

for _ in range(10):
    for __ in range(10):
        tim.color(choice(color_list))
        tim.begin_fill()
        tim.circle(10)
        tim.end_fill()
        tim.penup()
        if __ != 9:
            tim.forward(60)
        tim.pendown()

    tim.setheading(90)

    if _ % 2 == 0:
        tim.penup()
        tim.forward(90)
        tim.left(90)
    else:
        tim.penup()
        tim.forward(50)
        tim.right(90)

screen = Screen()
screen.exitonclick()
