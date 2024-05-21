from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.hideturtle()
        self.goto(x=0,y=270)
        self.color("white")
        self.write(f"Score = {self.score}",align="center",font=("Arial",20,"normal"))
        
    def score_increase(self):
        self.score+=1
        self.clear()
        self.write(f"Score = {self.score}",align="center",font=("Arial",20,"normal"))

    def game_over(self):
        self.goto(x=0,y=0)
        self.clear()
        self.write(f"GAME OVER!\n\n",align="center",font=("Arial",20,"normal"))
        if(self.score<5):
            self.write(f"\nYour Score = {self.score}\n",align="center",font=("Arial",17,"normal"))
            self.write(f"\n😭😭😭",align="center",font=("Arial",17,"normal"))
        elif(self.score>5 and self.score<10):
            self.write(f"\nYour Score = {self.score}\n",align="center",font=("Arial",17,"normal"))
            self.write(f"\n😊😊😊",align="center",font=("Arial",17,"normal"))
        else:
            self.write(f"\nYour Score = {self.score}\n",align="center",font=("Arial",17,"normal"))
            self.write(f"\n🎊🎊🎊",align="center",font=("Arial",17,"normal"))