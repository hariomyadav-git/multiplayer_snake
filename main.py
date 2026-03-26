import random
from turtle import Screen
import time
from snake import Snake
from food import Food,all_food
game_on = True
screen_width = 600
screen_height = 600
DIFF_COLOURS_OF_SNAKE = ["red", "purple","blue",]
NUM_OF_SNAKES = 2
name_of_snakes = []

s = Screen()
s.title("MY Snake Game")
s.tracer(0)
s.setup(width=screen_width,height=screen_height)

s.bgcolor("black")

def exit_game():
    global game_on
    game_on = False
    s.bye()



#MAKIN SNAKE OBJECT
for n in range(NUM_OF_SNAKES):
    snake = Snake(s_colour=DIFF_COLOURS_OF_SNAKE[n],s_ypos=n)
    snake.name_of_snakes.append(snake)
    name_of_snakes.append(snake)

#MAKING FOOD OBJECT
food = Food()



#CONTROL OF SNAKE 1
s.listen()
s.onkeypress(exit_game,"t")
s.onkeypress(name_of_snakes[0].up,"Up")
s.onkeypress(name_of_snakes[0].down,"Down")
s.onkeypress(name_of_snakes[0].left,"Left")
s.onkeypress(name_of_snakes[0].right,"Right")

#CONTROL OF SNAKE 2
s.listen()
s.onkeypress(name_of_snakes[1].up,"w")
s.onkeypress(name_of_snakes[1].down,"s")
s.onkeypress(name_of_snakes[1].left,"a")
s.onkeypress(name_of_snakes[1].right,"d")

#MAIN LOOP
while game_on:
    s.update()
    time.sleep(0.1)

    for sna in range(NUM_OF_SNAKES):
        name_of_snakes[sna].move()
        name_of_snakes[sna].collision_with_wall(screen_width,screen_height)
        # name_of_snakes[sna].collision_with_tail()

        for f in all_food[:]:
            if name_of_snakes[sna].head.distance(f) < 18:
                name_of_snakes[sna].add_segment()
                if f == food:
                    f.refresh()

                else:
                    f.hideturtle()
                    f.goto(1000,1000)
                    if f in all_food:
                        all_food.remove(f)



    name_of_snakes[1].collision_with_tail_of_other(name_of_snakes[0])
    name_of_snakes[0].collision_with_tail_of_other(name_of_snakes[1])
























s.exitonclick()