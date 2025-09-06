import turtle

angle = input("Enter int angle: ")
range_num = input("Enter int range: ")

wn = turtle.Screen()
spikemeyer = turtle.Turtle()  

for i in range(int(range_num)):
    spikemeyer.forward(i)
    spikemeyer.left(int(angle))

    color_range = (int(range_num) - i) / int(range_num)

    spikemeyer.color(color_range, color_range, color_range)

print("Click turtle screen to exit...")

wn.exitonclick()
