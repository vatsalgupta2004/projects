from turtle import Turtle
import random
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.colors1=[]
        self.color_genertaor()
        self.colour()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()
        
    def refresh(self):
        self.goto(x=random.randint(-280,280),y=random.randint(-280,280))
    
    def colour(self):
        self.color(random.choice(self.colors1))
    
    def color_genertaor(self):
        # self.colors1=[]
        for i in range(0,100,1):

            a=random.randint(1,255)
            b=random.randint(1,255)
            c=random.randint(1,255)
            self.colors1.append((a,b,c))