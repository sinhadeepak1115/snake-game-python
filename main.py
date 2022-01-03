import time
import turtle
from turtle import Screen, Turtle


screen = Screen()
screen.setup(height=600, width=600)
screen.title("Snake Game")
screen.bgcolor("green")
screen.tracer(0)

start_position = [(0, 0), (-20, 0), (-40, 0)]


segments = []

for position in start_position:
    segment = Turtle("square")
    segment.penup()
    segment.color("blue")
    segment.goto(position)
    segments.append(segment)



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segments) -1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)





screen.exitonclick()