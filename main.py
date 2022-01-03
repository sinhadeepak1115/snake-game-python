import turtle
from turtle import Screen, Turtle


screen = Screen()
screen.setup(height=600, width=600)
screen.title("Snake Game")
screen.bgcolor("green")

start_position = [(0, 0), (-20, 0), (-40, 0)]



for position in start_position:
    segment = Turtle("square")
    segment.color("blue")
    segment.goto(position)

screen.exitonclick()