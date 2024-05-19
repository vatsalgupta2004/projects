from turtle import Turtle,Screen

obj_turtle=Turtle()
obj_screen=Screen()

def move_forward():
    obj_turtle.forward(20)

def move_backward():
    obj_turtle.backward(20)

def move_anticlock():
    new_heading=obj_turtle.heading()+10
    obj_turtle.setheading(new_heading)

def move_clock():
    new_heading=obj_turtle.heading()-10
    obj_turtle.setheading(new_heading)

def clear_all():
    obj_turtle.reset()
    # alternative
    # obj_turtle.clear()
    # obj_turtle.penup()
    # obj_turtle.home()
    # obj_turtle.pendown()

obj_screen.listen()

obj_screen.onkey(key="W",fun=move_forward)
obj_screen.onkey(key="S",fun=move_backward)
obj_screen.onkey(key="A",fun=move_anticlock)
obj_screen.onkey(key="D",fun=move_clock)
obj_screen.onkey(key="C",fun=clear_all)

obj_screen.onkey(key="w",fun=move_forward)
obj_screen.onkey(key="s",fun=move_backward)
obj_screen.onkey(key="a",fun=move_anticlock)
obj_screen.onkey(key="d",fun=move_clock)
obj_screen.onkey(key="c",fun=clear_all)

obj_screen.exitonclick()