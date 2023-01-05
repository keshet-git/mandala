from turtle import*
import colorsys
tracer(10)
bgcolor('black')
pensize(5)
h=0
for i in range(1000):
    c= colorsys.hsv_to_rgb(h, 1, 1)
    color(c)
    h +=0.005
    up ()
    goto(0,0)
    forward(i)
    down()
    circle(i/3,20)
    left(45)
done()