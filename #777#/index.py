from turtle import*
import colorsys
tracer(15)
bgcolor('black')
pensize(1.5)
h=0.4
for i in range(1500):
    c= colorsys.hsv_to_rgb(h, 1, 1)
    color(c)
    h +=1/37
    goto(0,0)
    circle(i,- 30)
    left(180)
    left(222)
done()