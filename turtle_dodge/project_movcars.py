from turtle import Turtle
from project_color_gen import Colors_collection
import random

obj_color=Colors_collection()
Colours=obj_color.colors_list

Starting_move_distance = 5
Move_increment = 8

class CarManager:

    def __init__(self):
        self.all_Cars=[]
        self.current_speed=Starting_move_distance

    def create_car(self):
        random_luck=random.randint(0,10)
        if (random_luck==4):
            new_car=Turtle("square")
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(Colours))
            random_y = random.randint(-250,250)
            new_car.goto(300,y=random_y)
            self.all_Cars.append(new_car)

    def move_cars(self):
        for car in self.all_Cars:
            car.backward(self.current_speed)

    def level_up(self):
        self.current_speed+=Move_increment

    def speed_reset(self):
        self.current_speed=Starting_move_distance
        

