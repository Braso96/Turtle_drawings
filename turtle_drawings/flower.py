from turtle import *
from random import *

bgcolor('lightyellow')
colors = ['red', 'violet']

def flow():
    for i in range(180):
        color(choice(colors))
        circle(190-i, 90)
        left(90)
        circle(190-i, 90)
        left(10)
        speed(100)

flow()
