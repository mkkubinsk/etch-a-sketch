import turtle as t

timmy = t.Turtle()
screen = t.Screen()


def move_forward():
    timmy.forward(5)

def move_backwards():
    timmy.backward(5)

def turn_counter_clockwise():
    timmy.left(10)

def turn_clockwise():
    timmy.right(10)


screen.listen()
screen.onkeypress(fun=move_forward, key="w")
screen.onkeypress(fun=move_backwards, key="s")
screen.onkeypress(fun=turn_counter_clockwise, key="a")
screen.onkeypress(fun=turn_clockwise, key="d")
screen.onkeypress(fun=timmy.reset, key="c")

screen.exitonclick()
