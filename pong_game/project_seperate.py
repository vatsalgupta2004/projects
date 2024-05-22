from turtle import Turtle
class sep_line(Turtle):
    def __init__(self):
        super().__init__()
        self.line_sepeartor()

    def line_sepeartor(self):
        condition=True
        x=0
        y=280
        while(condition):
            obj_turtle=Turtle("square")
            obj_turtle.penup()
            obj_turtle.color("white")
            obj_turtle.shapesize(stretch_len=.1,stretch_wid=.5)
            obj_turtle.goto(x,y)
            if(obj_turtle.ycor()>-280):
                condition=True
                y-=20
            else:
                condition=False