
import turtle
import math
def blade1(t,r):
    turtle.up
    turtle.color('green')
    turtle.begin_fill()
    turtle.up()
    turtle.setposition(t,r)
    turtle.down()
    turtle.left(180)
    turtle.fd(100)
    turtle.left(45)
    turtle.fd(70)
    turtle.left(135)
    turtle.fd(100)
    turtle.left(45)
    turtle.fd(70)
    turtle.end_fill()
pass

def blade2():
    turtle.color('blue')
    turtle.begin_fill()
    turtle.right(45)
    turtle.fd(100)
    turtle.right(135)
    turtle.fd(73)
    turtle.right(90)
    turtle.fd(73)
    turtle.end_fill()
pass

def triangle1(k,o):
    turtle.up()
    turtle.color('yellow')
    turtle.begin_fill()
    turtle.right(90)
    turtle.setposition(k,o)
    turtle.down()
    turtle.forward(107)
    turtle.right(135)
    turtle.forward(150)
    turtle.right(135)
    turtle.forward(107)
    turtle.end_fill()
pass

def triangle2(l,f):
    turtle.color("red")
    turtle.up()
    turtle.begin_fill()
    turtle.setposition(l,f)
    turtle.down()
    turtle.right(90)
    turtle.forward(107)
    turtle.right(270)
    turtle.forward(107)
    turtle.left(135)
    turtle.fd(150)
    turtle.end_fill()
pass

def rocket():
    turtle.color("gray")
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(50)
    turtle.left(45)
    turtle.forward(30)
    turtle.left(135)
    turtle.forward(50)
    turtle.end_fill()
pass

def tail_triangle1(z,x):
    turtle.color('purple')
    turtle.begin_fill()
    turtle.up()
    turtle.setpos(z,x)
    turtle.down()
    turtle.right(45)
    turtle.forward(50)
    turtle.right(135)
    turtle.forward(math.sqrt(5000))
    turtle.right(135)
    turtle.forward(50)
    turtle.end_fill()
pass

def tail_triangle2(c,d):
    turtle.color('pink')
    turtle.begin_fill()
    turtle.up()
    turtle.setpos(c,d)
    turtle.down()
    turtle.right(45)
    turtle.forward(math.sqrt(5000))
    turtle.right(135)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.end_fill()
pass

def tail(a,b):
    turtle.color('orange')
    turtle.begin_fill()
    turtle.right(45)
    turtle.up()
    turtle.setpos(a,b)
    turtle.down()
    turtle.right(45)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.end_fill()
pass
def main():
    tail_triangle1(125, -18)
    tail_triangle2(54, -18)
    tail(0, 0)
    triangle1(125,-18)
    triangle2(201,-92)
    rocket()
    blade1(201,58)
    blade2()

pass

main()
turtle.done()

