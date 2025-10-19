from turtle import Turtle

# these are constant values
FONT = ("Arial",24,"normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.update_scoreboard()

    # this function will update the score board values
    def update_scoreboard(self):
        self.write(f'Score : {self.score}',align=ALIGNMENT,font=FONT)

    # this function will add a score to the previous score if the snake eat the food
    def add_score (self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
    
    # this function will check the situation of the game (being game over or not)
    def game_over(self):
        self.goto(0,0)
        self.write(f'Game Over :)',align=ALIGNMENT,font=FONT)
