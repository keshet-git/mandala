import turtle as t
import colorsys
t.bgcolor('black')
t.speed(5)
h=0
def draw(angle,n):
    t.fd(n)
    t.left(angle)
    t.fd(n)
    t.circle(30,90)
t.setpos(-200,0)
for i in range(8):
    c= colorsys.hsv_to_rgb(h, 1, 1)
    h += 0.15
    t.color(c)
    draw(135, 200)
    draw(90, 200)
done()