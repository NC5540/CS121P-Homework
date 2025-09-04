import turtle

angle = input("Enter int angle: ")
int_range = input("Enter int range: ")

wn = turtle.Screen()
alex = turtle.Turtle()  

for i in range(int(int_range)):
    alex.forward(i)
    alex.left(int(angle))
     
print("Click turtle screen to exit...")

wn.exitonclick()
