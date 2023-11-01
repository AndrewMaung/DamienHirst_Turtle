import turtle as turtle_module
import random
color_list = [(207, 165, 127), (164, 169, 38), (140, 48, 106), (244, 79, 57), (3, 144, 60), (241, 66, 140), (249, 220, 224), (2, 142, 185), (162, 55, 52), (243, 101, 162), (53, 203, 226), (211, 232, 234), (251, 228, 16), (22, 166, 128), (220, 237, 231), (253, 230, 0), (27, 196, 219), (156, 186, 168), (236, 164, 192)]
turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.hideturtle()
tim.penup()
tim.speed("fastest")
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
no_of_dots = 90

for dot_count in range(1,no_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
