import turtle

my_turtle = turtle.Turtle()

def myTurtle(forward, rotateLeft):
    for i in range(5): 
        my_turtle.forward(forward)
        for i in range(1): 
            my_turtle.left(rotateLeft)

def circle(times, angle, size):
    for i in range(times):
        my_turtle.left(angle)
        myTurtle(size, 90)
        my_turtle.left(90)
        my_turtle.forward(size)
        my_turtle.left(90)
        my_turtle.left(180)

circle(30, -75, 90)
circle(30, -75, 45)

input ()

