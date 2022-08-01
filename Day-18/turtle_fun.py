from turtle import Turtle, Screen, colormode
import random

directions = [0, 90, 180, 270]

timmy = Turtle()
timmy.shape("turtle")
timmy.speed("fastest")
colormode(255)

def randomColor():
    
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# def drawSquare():
#     for x in range(4):
#         timmy.forward(100)
#         timmy.right(90)


# def drawDashedLine():
#     for x in range(50):
#         timmy.forward(10)
#         timmy.up()
#         timmy.forward(10)
#         timmy.down()

# def drawShapes():
#     for x in range(3, 11):
#         timmy.color(randomColor())
#         for _ in range(x):
#             timmy.forward(100)
#             timmy.right(360 / x)
            
# def randomWalk():
#     timmy.pensize(10)
#     for _ in range(500):
#         timmy.color(randomColor())
#         timmy.forward(30)
#         timmy.setheading(random.choice(directions))
    
def drawSpiro():
    turn = 10  
    for _ in range(int(360 / turn)):
        timmy.color(randomColor())
        timmy.circle(50)
        timmy.right(turn)
        
    
drawSpiro()

screen = Screen()
screen.exitonclick()
