from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor('#f5f5f5')
screen.title('Snake Game')
screen.update()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right ")

game_on = True

while game_on and -300 < snake.head.xcor() < 295 and -295 < snake.head.ycor() < 300:
    screen.update()
    time.sleep(0.05)
    snake.move()
    scoreboard.refresh()

    if snake.head.distance(food) <= 14:
        scoreboard.current_score += 1
        snake.add_square()
        food.refresh()

    for i in snake.squares[1:]:
        if snake.head.distance(i) < 12:
            game_on = False

scoreboard.game_over()

screen.exitonclick()
