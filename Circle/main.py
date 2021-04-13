import turtle

my_turtle = turtle.Turtle()

def myTurtle(forward, rotateLeft):
    for i in range(5): 
        my_turtle.forward(forward)
        for i in range(1): 
            my_turtle.left(rotateLeft)

for i in range(30):
  my_turtle.left(-75)
  myTurtle(90, 90)
  my_turtle.left(90)
  my_turtle.forward(90)
  my_turtle.left(90)
  my_turtle.left(180)

input ()

