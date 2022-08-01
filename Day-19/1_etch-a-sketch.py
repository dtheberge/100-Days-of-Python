from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def forward():
    tim.forward(10)
def left():
    tim.left(10)
def backwards():
    tim.backward(10)
def right():
    tim.right(10)
def clear():
    tim.clear()
    tim.reset()

screen.listen()

screen.onkey(key="w", fun=forward)
screen.onkey(key="a", fun=left)
screen.onkey(key="s", fun=backwards)
screen.onkey(key="d", fun=right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()