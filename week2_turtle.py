import turtle

turtle.color('red', 'orange')

turtle.begin_fill()
turtle.speed(4)
turtle.backward(100)
turtle.right(30)
turtle.forward(50)
turtle.end_fill()

turtle.clear()

def draw_shape():
    sides = int(input('number of sides: '))
    angle = 360 / sides
    for i in range(sides):
        turtle.forward(100)
        turtle.right(angle)


draw_shape()
turtle.left(90)
turtle.forward(100)
draw_shape()

turtle.done()
