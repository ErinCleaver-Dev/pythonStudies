import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(0)

def myTurtle(forward, rotateLeft):
    for i in range(4): 
        my_turtle.forward(forward)
        my_turtle.left(rotateLeft)



def circle(times, angle, size, color):
    for i in range(times):
        my_turtle.color(color)
        my_turtle.left(angle)
        myTurtle(size, 90)

circle(150, 7, 90, "#B0E0E6")
circle(100, 11, 60, "#DA70D6")
circle(24, 15, 45, "#E6E6FA")
circle(72, 5, 25, "#B0E0E6")

input ()

