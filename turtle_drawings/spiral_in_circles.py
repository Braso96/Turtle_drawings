from turtle import *
from  random import *

shape('turtle')
bgcolor('lightblue')
speed(20)
pensize(2)

colors = ['red', 'yellow', 'blue']

number = randint(20, 300) #nr of circles

for x in range(number):
    color(choice(colors))
    circle(100)
    left(360/number)