from turtle import Screen
from theturtle import TheTurtle
from cars import Cars
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.screensize(canvwidth=600, canvheight=600)
screen.title("TURTLE CROSSING")
screen.tracer(0)
screen.listen()
player = TheTurtle()
score = ScoreBoard()
score.score_update()
game_is_on = True
list_of_cars = []
for _ in range(30):
    cars = Cars()
    list_of_cars.append(cars)
while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.onkey(key='Up', fun=player.move_turtle)

    if player.ycor() == 300:
        player.reset_turtle()
        score.level_change()
        for bots in list_of_cars:
            bots.level_up()

    for bots in list_of_cars:
        bots.move_car()
        if bots.xcor() < -350:
            bots.reset_cars()
        if player.distance(bots) < 20:
            score.game_over()
            game_is_on = False

screen.exitonclick()
