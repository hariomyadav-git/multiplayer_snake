from turtle import Turtle
from random import randint
all_food = []

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color("green")
        self.speed(0)
        all_food.append(self)
        self.refresh()


    def refresh(self):

        self.goto(x=randint(-275, 275), y=randint(-275, 275))
