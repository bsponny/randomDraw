import turtle
import random
t = turtle.Turtle()

def triDot(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.dot(5)

def main():
    t.speed(1000)

    x1 = 0
    y1 = 200

    x2 = 200
    y2 = -200

    x3 = -200
    y3 = -200

    triDot(x1, y1)
    triDot(x2, y2)
    triDot(x3, y3)

    xpos = 0
    ypos = 0

    for i in range(1000):
        t.penup()
        point = random.randint(1, 3)
        
        if point == 1:
            xpos = xpos + (x1 - xpos)/2
            ypos = ypos + (y1 - ypos)/2
            t.goto(xpos, ypos)
            t.pendown()
            t.dot(5)
        elif point == 2:
            xpos = xpos + (x2 - xpos)/2
            ypos = ypos + (y2 - ypos)/2
            t.goto(xpos, ypos)
            t.pendown()
            t.dot(5)
        elif point == 3:
            xpos = xpos + (x3 - xpos)/2
            ypos = ypos + (y3 - ypos)/2
            t.goto(xpos, ypos)
            t.pendown()
            t.dot(5)

main()
turtle.done()
