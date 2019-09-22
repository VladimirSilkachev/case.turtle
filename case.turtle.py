#Hello guys
#Developers V.Silkachev
            #K.Popov
            #S.Vinnikov

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
    turtle.up()
    turtle.setpos(z,x)
    turtle.down()
    turtle.right(135)
    turtle.forward(50)
    turtle.right(45)
    turtle.forward(math.sqrt(5000))
    turtle.right(45)
    turtle.forward(50)
pass

def tail_triangle2(c,d):
    turtle.up()
    turtle.setpos(c,d)
    turtle.down()
    turtle.right(90)
    turtle.forward(math.sqrt(5000))
    turtle.right(45)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
pass

def tail(a,b):
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
pass
def main():
    blade1()
    blade2()
    triangle1()
    triangle2()
    rocket()
    tail_triangle1()
    tail_triangle2()
    tail()
pass

main()
turtle.done()
