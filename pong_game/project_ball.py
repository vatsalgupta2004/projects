from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.color("white")
        self.penup()
        self.x_pos=10
        self.y_pos=10
        self.stime=.1
        self.ball_move()

    def ball_move(self):
        numx=self.xcor() + self.x_pos
        numy=self.ycor() + self.y_pos
        self.goto(numx,numy)

    def bounce_y(self):
        self.y_pos*=-1

    def bounce_x(self):
        self.x_pos*=-1
        self.stime*=0.9

    def reset(self):
        self.goto(0,0)
        self.stime=0.1
        self.bounce_x()