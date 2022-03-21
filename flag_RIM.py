import turtle
wn = turtle.Screen()
wn.bgcolor("black")
turtle = turtle.Turtle()
turtle.speed(10)
turtle.penup()
turtle.shape("turtle")


def drawFillRectangle(x, y, length, width, color):
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.end_fill()
    turtle.penup()

def drawStar(x,y,color,length) :
    turtle.goto(x,y)
    turtle.setheading(0)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color(color)
    for turn in range(0,5) :
        turtle.forward(length)
        turtle.right(144)
    turtle.end_fill()
    turtle.penup()

def drawCircle(x,y,color,radius) :
    turtle.goto(x,y)
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def drawMoon (x,y,color,radius):
    turtle.up()
    turtle.goto(x,y)
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()  

def drawGreen() :
    x = -230
    y = 125
    color = 'dark green'
    drawFillRectangle(x, y, 280, 550, color)

def drawRed() :
    x = -230
    y =  125
    color = 'red'
    drawFillRectangle(x, y, -280, 550, color)

def drawRedd() :
    x = 320
    y =  -155
    color = 'red'
    drawFillRectangle(x, y, 280, -550, color)

def Star() :
        x = 25
        y = 10
        color = 'yellow'
        drawStar(x, y, color, 50)
  
def Circle() :
           x = 45
           y = -100
           color = 'yellow'
           drawCircle(x, y, color, 80)

def Moon():
            x = 45
            y = -72
            color = 'dark green'
            drawMoon(x, y, color, 70)
             
drawGreen()
drawRed()
drawRedd()
Circle()
Moon()
Star()

turtle.goto(125,-200)
turtle.color('yellow')
turtle.write("عيد استقلال مجيد ")
turtle.goto(125,-220)
turtle.color('green')
turtle.write(" المعهد العالي للمحاسبة وإدارة المؤسسات ")
turtle.back(20)


