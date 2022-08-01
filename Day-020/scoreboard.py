from turtle import Turtle

FONT = ("Courier", 18, "normal")

class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.up()
        self.hideturtle()
        self.goto(x=0, y=260)
        self.score = 0
        self.color("white")
        self.write(f"Score: {self.score}", align="center", font=FONT)
    
    def addScore(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=FONT)
        
    def gameOver(self):
        self.goto(x=0, y=0)
        self.write(f"GAME OVER", align="center", font=FONT)
    