from turtle import Turtle
from project_17_food import Food 
import random
class Snake(Food):
    def __init__(self):
        self.objs=[]
        self.distance1=20
        self.RIGHT=0
        self.UP=90
        self.LEFT=180
        self.DOWN=270
        self.colors2=[]
        self.color_genertaor()
        self.body_creation()

    def body_creation(self):
        self.objs=[]
        self.pos_x=0
        self.pos_y=0
        for i in range(0,3,1):
            self.add_snake(self.pos_x,self.pos_y)
            self.pos_x-=20

    def color_genertaor(self):
        for i in range(0,100,1):
            a=random.randint(1,255)
            b=random.randint(1,255)
            c=random.randint(1,255)
            self.colors2.append((a,b,c))

    def add_snake(self,pos_x,pos_y):
        obj_turtle = Turtle("square")
        obj_turtle.color(random.choice(self.colors2))
        obj_turtle.penup()
        obj_turtle.goto(pos_x,pos_y)
        self.objs.append(obj_turtle)

    def increase_snake(self):
        self.lastx = self.objs[-1].xcor()
        self.lasty = self.objs[-1].ycor()
        self.add_snake(self.lastx,self.lasty)

    def snake_move(self):
        for seg_num in range((len(self.objs)-1),0,-1):
            new_x = self.objs[seg_num-1].xcor()
            new_y = self.objs[seg_num-1].ycor()
            self.objs[seg_num].goto(new_x,new_y)
        self.objs[0].forward(self.distance1)

    def up(self):
        if(self.objs[0].heading()!=self.DOWN):
            self.objs[0].setheading(self.UP)

    def down(self):
        if(self.objs[0].heading()!=self.UP):
            self.objs[0].setheading(self.DOWN)

    def right(self):
        if(self.objs[0].heading()!=self.LEFT):
            self.objs[0].setheading(self.RIGHT)

    def left(self):
        if(self.objs[0].heading()!=self.RIGHT):
            self.objs[0].setheading(self.LEFT)