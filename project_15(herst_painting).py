from turtle import Turtle,Screen
import random
obj_turtle=Turtle()
obj_screen=Screen()

obj_turtle.shape("arrow")
obj_screen.colormode(255)
colours=[(255,0,0),(255,165,0),(25,90,10),(55,90,0),(0,0,255),(0,255,0),(55,55,10),(5,90,80),(25,0,0),(5,0,190)]

obj_turtle.speed(0)
obj_turtle.penup()

def row_create(num):
    for i in range(num):
        obj_turtle.color(random.choice(colours))
        obj_turtle.dot(10)
        obj_turtle.forward(20)

def return_pos(num):
    obj_turtle.left(90)
    obj_turtle.forward(20)
    obj_turtle.left(90)
    for i in range(num):
        obj_turtle.forward(20)
    obj_turtle.right(180)

def times(num3,num):
    for i in range(num3):
        row_create(num)
        return_pos(num)

number=int(input("Enter number of dots you want in each row :"))
rows=int(input("Enter number of rows you want :"))
times(rows,number)

obj_screen.exitonclick()