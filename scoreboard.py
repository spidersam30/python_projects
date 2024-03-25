from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed('fastest')
        self.level = 1
        self.penup()
        self.goto(x=-300, y=300)

    def score_update(self):
        self.clear()
        self.write(f"LEVEL:{self.level}", font=("Courier", 16, "bold"))

    def level_change(self):
        self.level += 1
        self.score_update()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER.", font=("Courier", 16, "bold"))
