import turtle

turtle.hideturtle()
turtle.speed(100)

def makeShape(x, y, color, size, angle, corners):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.right(angle)
    turtle.circle(size, steps=corners)
    turtle.end_fill()

def drawLine(x1, y1, color, x2, y2):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.color(color)
    turtle.goto(x2, y2)

def eyebrows(x, y, angle):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("black")
    turtle.right(angle)
    turtle.circle(40, 60, steps=30)

# yellow head
makeShape(3,-100,"yellow",100,0,50)
# mask
makeShape(-5,-60,"cyan",40,45,4)
makeShape(-45,-60,"cyan",40,0,4)
# eyes
makeShape(-45,22,"white",25,0,30)
makeShape(27,22,"white",25,0,30)
makeShape(-33,30,"black",8,0,30)
makeShape(35,30,"black",8,0,30)
# strings of the mask
drawLine(52,-3,"blue",102,15)
drawLine(52,-60,"blue",78,-68)
drawLine(-45,-60,"blue",-70,-70)
drawLine(-45,-3,"blue",-95,15)
# outline the mask
drawLine(-45,-3,"blue",52,-3)
drawLine(52,-3,"blue",52,-60)
drawLine(52,-60,"blue",-45,-60)
drawLine(-45,-60,"blue",-45,-3)
# eyebrows
eyebrows(-10,85,165)
eyebrows(70,72,45)
# body
makeShape(0,-100,"purple",40,45,5)
drawLine(-25,-110,"purple",-60,-130)
drawLine(25,-110,"purple",60,-130)
drawLine(-10,-170,"purple",-15,-200)
drawLine(10,-170,"purple",15,-200)
# dialogue
turtle.penup()
turtle.goto(100,100)
turtle.write("Where is your \nmask, sir??", font=("Verdana",20,"normal"))

turtle.done()