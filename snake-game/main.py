from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scorboard import Scoreboard


import time
window = Screen()
window.setup(800,800)
window.bgcolor("black")
window.title("Snake Game")
window.tracer(0)

sam = Snake()
food = Food()
score = Scoreboard()

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
    if Snake.head.distance(food) < 15:
        food.appear()
        Snake.extend()
        score.increase_score()
    
    if Snake.head.xcor() > 370 or Snake.head.xcor() < -370 or Snake.head.ycor() > 370 or Snake.head.ycor() < -370:
        game_on = False
        score.game_over()
        
    for segment in Snake.turtles[:-1]:
        if Snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()
            

window.exitonclick()