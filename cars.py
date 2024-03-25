from turtle import Turtle
import random

COLORS = ['red', 'blue', 'orange', 'purple', 'black', 'brown']
MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.setheading(180)
        color = random.choice(COLORS)
        self.color(color)
        self.x = random.randrange(start=-300, stop=300, step=30)
        self.y = random.randrange(start=-250, stop=280, step=30)
        self.goto(x=self.x, y=self.y)
        self.speed = MOVE_DISTANCE

    def move_car(self):
        self.forward(self.speed)

    def reset_cars(self):
        x = 350
        self.goto(x, self.y)

    def level_up(self):
        self.speed += MOVE_INCREMENT
