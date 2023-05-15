import turtle

t = turtle.Turtle()
t.speed(-1)
t.setheading(90)
t.penup()
t.goto(0, -200)
t.pendown()


def xD(t, len):
    if len == 0: return

    nt = t.clone()
    nt.forward(50)

    nt.left(20)
    xD(nt, len - 2)

    nt.right(40)
    print(t.pos(), "len - (len - 1): ", len - 1)
    xD(nt, len - 1)


xD(t, 6)

window = turtle.Screen()
window.exitonclick()