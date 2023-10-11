import time
from turtle import Screen

from food import Food
from scoreBoard import ScoreBoard
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Xenzia")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor()<-280 or snake.head.ycor() > 298 or snake.head.ycor() <-298:
        score.game_over()
        is_game_on =False

    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            is_game_on = False
            score.game_over()
screen.exitonclick()