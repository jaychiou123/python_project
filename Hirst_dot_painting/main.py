import colorgram
import turtle as t
import random
num_color = 30
rgb_color = []
colors = colorgram.extract("image.jpg", num_color)
for i in colors:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    color_tuple = (r, g, b)
    rgb_color.append(color_tuple)
print(rgb_color)

tim = t.Turtle()
tim.speed("fastest")
tim.hideturtle()
t.colormode(255)
screen = t.Screen()
screen.screensize(500,500)
color_list = [(247, 242, 234), (237, 242, 248), (249, 240, 244), (239, 247, 244), (139, 168, 195), (206, 154, 121), (192, 140, 150), (25, 36, 55), (58, 105, 140), (145, 178, 162), (151, 68, 58), (137, 68, 76), (229, 212, 107), (47, 36, 41), (145, 29, 36), (28, 53, 47), (55, 108, 89), (228, 167, 173), (189, 99, 107), (139, 33, 28), (194, 92, 79), (49, 40, 36), (228, 173, 166), (20, 92, 69), (177, 189, 212), (29, 62, 107), (113, 123, 155), (172, 202, 190), (51, 149, 193), (166, 200, 213)]
def move(x, y):
    tim.penup()
    tim.setx(x)
    tim.sety(y)
    tim.pd()

move(-250, -250)
for i in range(10):
    for y in range(10):
        color = random.choice(color_list)
        tim.pendown()
        tim.dot(20,color)
        tim.penup()
        tim.forward(50)
    move(-250, -250 + 50*(i+1))


screen.exitonclick()