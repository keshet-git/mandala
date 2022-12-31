from turtle import *
import colorsys
bgcolor("black")
tracer(100)
h =0
for i in range(500):
    c =colorsys.hsv_to_rgb(h,1,1)
    h+= 0.005
    color(c)
    fillcolor(c)
    begin_fill()
    forward(i)
    circle(10)
    right(3)
    backward(i)
    left(180)
    end_fill()
done()