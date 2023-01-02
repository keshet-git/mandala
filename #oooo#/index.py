from turtle import *
import colorsys

speed(0)
bgcolor('black')
pensize(2)
h=0.1
for i in range(250):
    c= colorsys.hsv_to_rgb(h, 1, 1)
    color(c)
    h += 0.1
    circle(i,170)
    rt(100)
    for j in range(0):
        rt(40)
    
done()