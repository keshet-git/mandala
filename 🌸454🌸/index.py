from turtle import *
import colorsys
bgcolor("red")
tracer(30)
pensize(4)
h=0
for i in range(180):
    c=colorsys.hsv_to_rgb(h, 1,1)
    h+=0.004
    width(i//100+4)
    color(c)
    right(120)
    circle(-i*0.8,120)
    circle(i*0.5,120)
    circle(i*0.8,60)
