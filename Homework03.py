import turtle

# Getting user input
angle = input("Enter int angle: ")
num_range = int(input("Enter int range: "))

# Setting turtle objects
wn = turtle.Screen()
spikemeyer = turtle.Turtle()  

for i in range(num_range):
    # Drawing shape with range and angle given
    spikemeyer.forward(i)
    spikemeyer.left(int(angle))

    # Adjusting color with range as drawing progresses
    color_range = (num_range - i) / num_range

    spikemeyer.color(color_range, color_range, color_range)

print("Click turtle screen to exit...")

wn.exitonclick()
