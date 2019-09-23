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
    #TODO: (Kirill): левый большой
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

def triangle2():
     #TODO: (Kirill): правый большой
    turtle.color("red")
    turtle.begin_fill()
    turtle.up()
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
    #TODO: (Kirill): праллелограм
    turtle.color("pink")
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
    tail_triangle1()
    tail_triangle2()
    tail()
    triangle1(125,-18)
    triangle2(201,-92)
    rocket()
    blade1()
    blade2()
pass

main()
turtle.done()
