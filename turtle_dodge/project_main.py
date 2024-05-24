from turtle import Turtle,Screen
import time
from project_player import Player
from project_movcars import CarManager
from project_scoreboard import Scoreboard
import random

obj_screen=Screen()
obj_screen.setup(height=600,width=600)
obj_screen.bgcolor("black")
obj_screen.tracer(0)
obj_screen.colormode(255)

obj_player = Player()
obj_cars = CarManager()
obj_score = Scoreboard()

obj_screen.listen()
obj_screen.onkeypress(fun=obj_player.move_up,key="Up")
obj_screen.onkeypress(fun=obj_player.move_down,key="Down")

game_is_on=True
while(game_is_on):
    obj_screen.update()
    time.sleep(obj_player.speed)
    obj_cars.create_car()
    obj_cars.move_cars()
    obj_score.update_level()
    
    #finish line
    if(obj_player.ycor()>280):
        obj_player.reset_player()
        obj_score.level_won()
        obj_cars.level_up()
    #resist back move
    if(obj_player.ycor()<-280):
        obj_player.reset_player()

    #collision
    for car in obj_cars.all_Cars:
        if(obj_player.distance(car)<20):
            game_is_on=False
            obj_score.level_lost()
            obj_cars.speed_reset()

obj_screen.exitonclick()