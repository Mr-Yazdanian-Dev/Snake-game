from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color('yellow')
        self.speed("fastest")
        self.create_food()

    # this function will create a new food at a new position in the game window
    def create_food(self):
        fd_x = random.randint(-200,200)
        fd_y = random.randint(-200,200)
        self.goto(fd_x,fd_y)