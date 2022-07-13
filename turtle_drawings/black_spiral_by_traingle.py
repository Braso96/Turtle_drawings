import  turtle

forw = 1

tri = turtle.Turtle()
tri.speed(100)

for i in range(1000):
    tri.forward(forw)
    tri.left(120)
    tri.left(1)
    forw +=1
turtle.done()