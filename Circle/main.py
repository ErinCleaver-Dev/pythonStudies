import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(0)

def myTurtle(forward, rotateLeft):
    for i in range(5): 
        my_turtle.forward(forward)
        my_turtle.left(rotateLeft)



def circle(times, angle, size, color):
    for i in range(times):
        my_turtle.color(color)
        my_turtle.left(angle)
        myTurtle(size, 90)
        my_turtle.left(90)
        my_turtle.forward(size)
        my_turtle.left(90)
        my_turtle.left(180)

circle(450, -89, 90, "#B0E0E6")
circle(150, -61, 60, "#DA70D6")
circle(75, -61, 45, "#E6E6FA")
circle(25, -62, 25, "#B0E0E6")

input ()

