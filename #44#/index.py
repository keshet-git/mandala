from turtle import *
import colorsys
tracer(100)
bgcolor('black')
pensize(3)
goto(180,20)
h=0.4
for i in range(100):
    c= colorsys.hsv_to_rgb(h, 1, 1)
    color(c)
    h += 0.005
    circle(i-140,-40)
    circle(i-140,-40)
    left(220)
