from turtle import Turtle


class TheTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color("black")
        self.penup()
        self.goto(x=0, y=-300)
        self.setheading(90)

    def move_turtle(self):
        self.forward(10)

    def reset_turtle(self):
        self.goto(x=0, y=-300)
