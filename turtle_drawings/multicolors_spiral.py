from turtle import *

colors = ['red', 'yellow', 'green', 'purple', 'blue', 'orange']
t = Pen() #setup the turtle pen
bgcolor('black')


for i in range(500): #nr. of iteration
    t.pencolor(colors[i%6]) #set the color
    t.width(i/100 + 1) #set the width
    t.forward(i) #pointer of the turtle triangle if backward it will make from edge of remove no draw
    t.left(50)
    speed(1000)



