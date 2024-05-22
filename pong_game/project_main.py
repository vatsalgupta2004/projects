from turtle import Turtle,Screen
from project_paddle import Paddle
from project_ball import Ball
from project_scoreboard import Scoreboard
from project_seperate import sep_line
import time
obj_screen=Screen()
obj_screen.bgcolor("black")
obj_screen.setup(width=800,height=600)
obj_screen.title("pong game")
obj_screen.tracer(0)

obj_right_paddle=Paddle(380,0)
obj_left_paddle=Paddle(-380,0)
obj_ball=Ball()
obj_score=Scoreboard()
obj_line_sep=sep_line()
    
obj_screen.listen()
obj_screen.onkey(fun=obj_right_paddle.go_up,key="Up")
obj_screen.onkey(fun=obj_right_paddle.go_down,key="Down")
obj_screen.onkey(fun=obj_left_paddle.go_up,key="q")
obj_screen.onkey(fun=obj_left_paddle.go_down,key="a")
 
game_is_on=True
while(game_is_on):
    obj_screen.update()
    time.sleep(obj_ball.stime)
    obj_ball.ball_move()
    if(obj_ball.ycor()>280 or obj_ball.ycor()<-280):
        obj_ball.bounce_y()
    #collision with paddle
    if(obj_ball.distance(obj_right_paddle)<40 and obj_ball.xcor()>320):
        obj_ball.bounce_x()

    if(obj_ball.distance(obj_left_paddle)<40 and obj_ball.xcor()<-325):
       obj_ball.bounce_x()
    
    #reset_right
    if(obj_ball.xcor()>380):
        obj_score.r_point()
        obj_ball.reset()
        
    #reset_left
    if(obj_ball.xcor()<-390):
        obj_score.l_point()
        obj_ball.reset()
    
    if(obj_score.l_Score==10 or obj_score.l_Score==10):
        game_is_on=False
        if(obj_score.l_Score==10):
            obj_score.l_wins()
        elif(obj_score.r_Score==10):
            obj_score.r_wins()

obj_screen.exitonclick()