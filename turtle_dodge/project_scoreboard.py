from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        self.level=0
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.update_level()

    def update_level(self):
        self.clear()
        self.goto(x=-295,y=274)
        self.write(f"LEVEL  {self.level}",align="left",font=("Arial",15,"normal"))

    def level_won(self):
        self.level+=1

    def level_lost(self):
        self.goto(0,0)
        if(self.level<1):
            self.write(f"Your Score {self.level} 😭\n",align="center",font=("Arial",30,"normal"))
            self.write(f"Thankyou for playing",align="center",font=("Arial",30,"normal"))
        elif(self.level>3 and self.level<7):
            self.write(f"Your Score {self.level} 😊\n",align="center",font=("Arial",30,"normal"))
            self.write(f"Thankyou for playing",align="center",font=("Arial",30,"normal"))
        elif(self.level>=7):
            self.write(f"Your Score {self.level} 😎\n",align="center",font=("Arial",30,"normal"))
            self.write(f"Thankyou for playing",align="center",font=("Arial",30,"normal"))
        self.level=0