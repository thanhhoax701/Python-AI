from turtle import *
import colorsys

speed(100)
hideturtle()
bgcolor('black')
hue=0.0
pensize(2)
for i in range(240):
    col=colorsys.hsv_to_rgb(hue,1,1)
    pencolor(col)
    hue+=0.005
    circle(i)
    lt(5)

done()