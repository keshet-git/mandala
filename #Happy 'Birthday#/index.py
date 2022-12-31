from turtle import *
import colorsys
bgcolor("black")
tracer(20)
h = 0
text= ['Happy', 'Birthday']
for i in range(100):
    color(colorsys.hsv_to_rgb(h, 1,1))
    h += 0.05
    up()
    fd(i*4)
    down()
    write(text[i%2],font=('Arial', int((i+4)/4),
    'bold'))
    lt(45)
done()