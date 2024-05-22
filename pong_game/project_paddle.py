from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,num1,num2):
        super().__init__()
        self.coorx=num1
        self.coory=num2
        self.create_paddle()
        
    def create_paddle(self):
        self.shape("square")
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.color("white")
        self.penup()
        self.goto(self.coorx,self.coory)

    def go_up(self):
        new_y=self.ycor()+20
        self.goto(self.xcor(),new_y)

    def go_down(self):
        new_y=self.ycor()-20
        self.goto(self.xcor(),new_y)

    
