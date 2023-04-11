from turtle import Screen
import time
from snake import Snake
from food import  Food
from score import Score

# screen options
sc = Screen()
sc.setup(600, 600)
sc.bgcolor('black')
sc.title('Snake Game')
sc.tracer(0) #igy varni fog a setup parancsra

#create body
snake = Snake()
food = Food()
score = Score()

# control (ha azt akarod ne tunjon el a kigyo ezeket deactivalni kell amig vissza nem jon a kepre
sc.listen()
sc.onkey(fun=snake.up,key="Up")
sc.onkey(fun=snake.down,key="Down")
sc.onkey(fun=snake.left,key="Left")
sc.onkey(fun=snake.right,key="Right")

# main game loop
gameON = True
point = 0
while gameON:
    sc.update()
    time.sleep(0.1)
    snake.move()

    #detect collison with food
    if snake.head.distance(food) < 20:
        point += 1
        food.refresh()
        score.point()
        snake.extend()

    #detect collision with wall
    if snake.head.ycor() > 295 or snake.head.ycor() < -295 or snake.head.xcor() > 295 or snake.head.xcor() < -295:
        gameON = False
        score.game_over()

    for seg in snake.segments:
        if seg == snake.head:
            pass
        elif snake.head.distance(seg) <= 10:
            gameON = False
            score.game_over()


sc.exitonclick()

