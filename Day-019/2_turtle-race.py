from tkinter import Y
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtlte will win? Enter their color: ")
colors=["red", "orange", "yellow", "green", "blue", "purple"]
turtles=[]

y = -70
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.up()
    new_turtle.goto(x=-230, y=y)
    turtles.append(new_turtle)
    y += 30
    
if user_bet:
    is_race_on = True
    
while(is_race_on):
    
    for turtle in turtles:
        if(turtle.xcor() > 225):
            is_race_on = False
            winning_color = turtle.pencolor()
            if(winning_color == user_bet):
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

is_race_on = False
screen.exitonclick()