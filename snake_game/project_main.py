from turtle import Screen
import time
from project3.snake_game.project_snake import Snake
from project_17_food import Food
from project3.snake_game.project_scoreboard import Score

obj_screen = Screen()
obj_screen.colormode(255)
obj_screen.tracer(0)
obj_screen.setup(height=624,width= 600)
obj_screen.bgcolor("black")
obj_screen.title("My Snake Game")

Score1= Score()
Snake1= Snake()
food1= Food()

obj_screen.listen()
obj_screen.onkey(fun=Snake1.up,key="Up")
obj_screen.onkey(fun=Snake1.down,key="Down")
obj_screen.onkey(fun=Snake1.left,key="Left")
obj_screen.onkey(fun=Snake1.right,key="Right")

game_is_on=True
while(game_is_on):
    obj_screen.update()
    time.sleep(.09)
    Snake1.snake_move()
    if(Snake1.objs[0].xcor()>290 or Snake1.objs[0].xcor()<-290 or Snake1.objs[0].ycor()>290 or Snake1.objs[0].ycor()<-290):
        game_is_on=False
        Score1.game_over()

    for segments in Snake1.objs:
        if Snake1.objs[0] == segments:
            pass
        elif Snake1.objs[0].distance(segments)<10:
            game_is_on=False
            Score1.game_over()

    #collision with food
    if Snake1.objs[0].distance(food1) < 15:
        food1.refresh()
        food1.colour()
        Score1.score_increase()
        Snake1.increase_snake()

obj_screen.exitonclick()