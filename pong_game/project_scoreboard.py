from turtle import Turtle
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_Score=0
        self.r_Score=0
        self.update_score()

    def update_score(self):
        self.goto(-390,260)
        self.write(f"P1",align="left",font=("Arial",25,"normal"))
        self.goto(-100,200)
        self.write(f"{self.l_Score}",align="center",font=("Arial",75,"normal"))
        self.goto(390,260)
        self.write(f"P2",align="right",font=("Arial",25,"normal"))
        self.goto(100,200)
        self.write(f"{self.r_Score}",align="center",font=("Arial",75,"normal"))

    def l_point(self):
        self.l_Score+=1
        self.clear()
        self.update_score()

    def r_point(self):
        self.r_Score+=1
        self.clear()
        self.update_score()

    def l_wins(self):
        self.goto(0,0)
        self.write(f"P1 wins 🎊",align="center",font=("Arial",75,"normal"))

    def r_wins(self):
        self.goto(0,0)
        self.write(f"P2 wins 🎊",align="center",font=("Arial",75,"normal"))
    
        

    

