from turtle import Turtle, Screen
import random
import turtle as t

t.colormode(255)
tim = Turtle()
tim.shape("turtle")
tim.shapesize(5)
tim.color("red")  # change color of turtle
tim.pensize(5)  # change size of turtle
tim.speed(1)  # change speed of turtle
tim.forward(500)

my_screen = Screen()
my_screen.title("My turtle game")
# my_screen.bgcolor("yellow")
# my_screen.setup(width=800, height=600)
canvheight = my_screen.canvheight
print(canvheight)
my_screen.exitonclick()
# Challenge 1 - Draw a Square
# for _ in range(4):