from mimetypes import init
from turtle import Screen, Turtle

MOVE_DISTANCE = 20

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake():
    
    def __init__(self) -> None:
        self.createSnake()
        self.head = self.segments[0]
        
    ## Creates starting segments
    def createSnake(self):
        self.segments = []
        for position in STARTING_POSITIONS:
            self.add_segment(position)
            
    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.shapesize(0.9, 0.9)
        new_segment.up()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)
        
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        
    def up(self):
        if (self.head.heading() != DOWN):
            self.head.setheading(UP)

    def left(self):
        if (self.head.heading() != RIGHT):
            self.head.setheading(LEFT)
        
    def right(self):
        if (self.head.heading() != LEFT):
            self.head.setheading(RIGHT)
        
    def down(self):
        if (self.head.heading() != UP):
            self.head.setheading(DOWN)

