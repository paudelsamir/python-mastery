from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        self.score= 0
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 240)
        self.hideturtle() 
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.write(arg= f"Score: {self.score}", move= False,align="center", font=("arial", 15, "normal"))
        
    def game_over(self):
        self.goto(0,0)
        self.write(arg= "Game Over", move= False,align="center", font=("arial", 15, "normal"))
        
        
    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()
