import turtle
import random

def rgb_random():
    return random.choice((0, 0.25))

print("Random background color is:",rgb_random(),",", rgb_random(),",", rgb_random())

rotation_num = int(input("Enter rotational copies: "))
side_num = int(input("Enter sides per polygon: "))
pixel_length = int(input("Enter edge pixel length: "))

wn = turtle.Screen()
shape = turtle.Turtle()
side_angle = 360 / side_num
shape_color = "white"
shape_size = 4

wn.bgcolor(rgb_random(), rgb_random(), rgb_random())

def drawShape(side_num, length, angle, tz, tz_color, tz_size):
    for i in range(side_num):
        tz.color(tz_color)
        tz.pensize(tz_size)
        tz.forward(length)
        tz.left(angle)


for i in range(rotation_num):
    drawShape(side_num, pixel_length, side_angle, shape, shape_color, shape_size)
    shape.left(360 // rotation_num)

for i in range(rotation_num):
    shape_color = "black"
    shape_size = 1
    drawShape(side_num, pixel_length, side_angle, shape, shape_color, shape_size)
    shape.left(360 // rotation_num)


print("Click turtle screen to exit...")

wn.exitonclick()
