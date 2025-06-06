from turtle import Turtle, Screen
from snake import Snake
import time
window = Screen()
window.setup(600,600)
window.bgcolor("black")
window.title("Snake Game")
window.tracer(0)

sam = Snake()

game_on = True
while game_on:
    sam.move()
    window.update()
    time.sleep(1)
    window.listen()
    window.onkey(Snake.up,"Up")
    window.onkey(Snake.down,"Down")
    window.onkey(Snake.right,"Right")
    window.onkey(Snake.left,"Left")

window.exitonclick()