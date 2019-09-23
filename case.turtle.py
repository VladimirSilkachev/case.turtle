#Hello guys
#Developers V.Silkachev
            #K.Popov
            #S.Vinnikov(30%)

import turtle
import math
def blade1():
    #TODO: (vova):  левый синий треуголльник
    pass

def blade2():
    #TODO: (vova): правый красный паралледограм
    pass

def triangle1():
    #TODO: (Kirill): правый большой
    pass

def triangle2():
    #TODO: (Kirill): левый большой
    pass

def rocket():
    #TODO: (Kirill): трапеция
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
    blade1()
    blade2()
    triangle1()
    triangle2()
    rocket()
pass

main()
turtle.done()
