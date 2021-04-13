import turtle

my_turtle = turtle.Turtle()

def myTurtle(forward, rotateLeft):
    my_turtle.forward(forward)
    my_turtle.left(rotateLeft)
    my_turtle.forward(forward)
    my_turtle.left(rotateLeft)
    my_turtle.forward(forward)
    my_turtle.left(rotateLeft)
    my_turtle.forward(forward)

myTurtle(90, 90)
my_turtle.forward(90)
myTurtle(90, 90)
myTurtle(90, 90)
myTurtle(90, 90)
myTurtle(90, 90)
my_turtle.forward(90)
my_turtle.left(90)
my_turtle.forward(90)
myTurtle(90, 90)
my_turtle.right(180)
my_turtle.forward(90)
my_turtle.right(90)
myTurtle(90, 90)
my_turtle.right(180)
my_turtle.forward(90)
my_turtle.right(90)
myTurtle(90, 90)

input()
