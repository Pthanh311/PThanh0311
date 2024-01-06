import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(0)
h = 0
n = 36

for i in range(220):
    color = colorsys.hsv_to_rgb(h,1,1)
    h+= 1/n
    t.color(color)
    t.circle(130)
    t.left(2)    