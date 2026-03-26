from turtle import Turtle
from food import Food,all_food
import time



one_segment_size = 20
NUM_OF_SEGMENTS = 3
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
height_lag = 250

class Snake:
    def __init__(self,s_colour,s_ypos):
        self.segments = []
        self.colour = s_colour
        self.s_ypos = s_ypos
        self.make_snake()
        self.head = self.segments[0]
        self.name_of_snakes = []



    def make_snake(self):
        for i in range(NUM_OF_SEGMENTS):
            t = Turtle(shape="square")
            t.color(self.colour)
            t.penup()
            t.goto(y=self.s_ypos * one_segment_size, x= i * - one_segment_size)
            self.segments.append(t)


    def add_segment(self):
        t = Turtle(shape="square")
        t.color("white")
        t.penup()
        t.goto(self.segments[-1].position())
        self.segments.append(t)

    def move(self):
        for x in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[x - 1].xcor()
            new_y = self.segments[x - 1].ycor()
            self.segments[x].goto(x=new_x, y=new_y)

        self.segments[0].forward(one_segment_size)

    def up(self):
        self.segments[0].setheading(UP)
    def down(self):
        self.segments[0].setheading(DOWN)
    def left(self):
        self.segments[0].setheading(LEFT)
    def right(self):
        self.segments[0].setheading(RIGHT)



    def collision_with_tail_of_other(self,other_snake):
        for segment in other_snake.segments:
            if self.head.distance(segment) >= 11:
                continue
            cut_part = self.segments[3:]
            self.segments = self.segments[0:3]

            self.head.goto(0, 0)

            for t in cut_part:
                loot = Food()
                loot.color("gold")
                all_food.append(loot)
                loot.goto(t.position())
                t.hideturtle()
                t.clear()
                t.goto(1000,1000)
                del t

    # def collision_with_tail(self):
    #     for segment in self.segments[1:]:
    #         if self.head.distance(segment) >= 11:
    #             continue
    #         cut_part = self.segments[3:]
    #         self.segments = self.segments[0:3]
    #         self.head.goto(0,0)
    #         for t in cut_part:
    #             loot = Food()
    #             loot.color("gold")
    #             all_food.append(loot)
    #             loot.goto(t.position())
    #             t.hideturtle()
    #             t.clear()
    #             t.goto(1000,1000)
    #             del t


    def collision_with_wall(self,s_width,s_height):
        #or   > s_height or self.head.ycor() < -s_height:
        if self.head.xcor() > s_width :
            self.head.goto(x=-s_width,y=self.head.ycor())

        elif self.head.xcor() < -s_width :
            self.head.goto(x=s_width,y=self.head.ycor())

        elif self.head.ycor() < -s_height +height_lag:
            self.head.goto(x=self.head.xcor(),y=s_height - height_lag)

        elif self.head.ycor() > s_height  - height_lag:
            self.head.goto(x=self.head.xcor(),y=-s_height + height_lag)

    # DETECTING COLLISION WITH FOOD
    # def collision_with_food(self,all_foo):
    #






