import turtle
import pandas

obj_screen = turtle.Screen()
obj_screen.title("us states game")
obj_screen.setup(730, 504)
image = "blank_states_img.gif"
obj_screen.addshape(image)
turtle.shape(image)
turtle.goto(x=0, y=3)
# basically gets the co-ordinates on click of mouse
# def get_click_coordinate(x,y):
#     print(x,y)
# turtle.onscreenclick(get_click_coordinate)
# turtle.mainloop()

content_states = pandas.read_csv("50_states.csv")
dict_states = content_states["state"].to_dict()
dict_states_x = content_states["x"].to_dict()
dict_states_y = content_states["y"].to_dict()
# print(dict_states)
# print(dict_states_x)
# print(dict_states_y)
# print(len(dict_states))
Score_Count = 0
condition = True
while (condition):
    if (Score_Count == 50):
        condition = False
    answer_state = (obj_screen.textinput(title=f"states guessed {Score_Count}/{len(dict_states)}", prompt="State")).title()
    for i in range(0, len(dict_states), 1):
        if (answer_state == dict_states[i]):
            Score_Count += 1
            obj_turtle = turtle.Turtle()
            obj_turtle.color("black")
            obj_turtle.penup()
            obj_turtle.hideturtle()
            obj_turtle.goto(x=dict_states_x[i], y=dict_states_y[i])
            obj_turtle.write(arg=f"{answer_state}", align="left", font=("Arial", 8, "bold"))
obj_turtle = turtle.Turtle()
obj_turtle.color("black")
obj_turtle.penup()
obj_turtle.hideturtle()
obj_turtle.goto(x=0, y=0)
obj_turtle.write(arg=f"YOU GUESSED ALL THE {len(dict_states)} STATES\n\tGAME OVER😎!", align="center",
                 font=("Arial", 22, "bold"))
#obj_screen.exitonclick()
turtle.mainloop()
