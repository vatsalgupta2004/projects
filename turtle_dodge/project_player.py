from turtle import Turtle
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.x=0
        self.y=-280
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.placement()
        self.speed=0.1

    def placement(self):
        self.goto(self.x,self.y)
    
    def move_up(self):
        new_y=((self.ycor())+20)
        self.goto(self.xcor(),new_y)
        self.y+=20

    def move_down(self):
        new_y=((self.ycor())-20)
        self.goto(self.xcor(),new_y)
        self.y-=20
    
    def reset_player(self):
        self.x=0
        self.y=-280
        self.placement()
    
