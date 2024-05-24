from turtle import Turtle,Screen
import random

obj_screen=Screen()
obj_screen.setup(width=400,height=400)
obj_screen.colormode(255)

colors1=set([])
def color_genertaor():
    global colors1
    for i in range(0,100,1):
        a=random.randint(0,255)
        b=random.randint(0,255)
        c=random.randint(0,255)
        colors1.add((a,b,c))
color_genertaor()
input_bet=(obj_screen.textinput(title="turtle race",prompt=f"select your desired color {list(colors1)[0]},{list(colors1)[1]},{list(colors1)[2]},{list(colors1)[3]},{list(colors1)[4]},{list(colors1)[5]} turtle to final your bet:").lower())
print(f"your bet color was {input_bet}")
obj_list=[]
position=155

def creation():
    global position
    for turtle_obj in range(0,6,1):
        obj_turtle=Turtle()
        obj_turtle.shape("turtle")
        obj_turtle.penup()
        obj_turtle.speed(0)
        obj_turtle.color(list(colors1)[turtle_obj])
        obj_turtle.goto(x=-180,y=position)
        position-=60
        obj_list.append(obj_turtle)

def race_onn():
    if input_bet:
        race_on=True
    else :
        race_on=False

    while(race_on):
        for i in obj_list:
            i.forward(random.randint(0,20))
            if i.xcor() > 180:
                race_on=False
                winning_color=i.pencolor()
                if(winning_color==input_bet):
                    print(f"You won, {winning_color} is the winning color")
                else:
                    print(f"You lost,{winning_color} is the winning color")

# def clear_all():
#     obj_screen.reset()

obj_screen.listen()
obj_screen.onkey(fun=creation,key="s")
obj_screen.onkey(fun=creation,key="S")
obj_screen.onkey(fun=race_onn,key="R")
obj_screen.onkey(fun=race_onn,key="r")

# obj_screen.onkey(fun=clear_all,key="c")
# obj_screen.onkey(fun=clear_all,key="C")

obj_screen.exitonclick()