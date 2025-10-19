from turtle import Screen,Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


def Game():
    my_screen = Screen()
    my_screen.setup(width=600,height=600)
    my_screen.bgcolor("Black")
    my_screen.title("Snake Game")
    my_screen.tracer(0)

    # this will create a static snake object at the center of canvas 
    my_snake = Snake()
    snake_food = Food()
    my_score = Scoreboard()

    # this will run a method that listen to us in order to get any key that we press to change the location of the snake
    my_screen.listen()

    # becuase I use my_snake.go_up() as an argument for other method(function), I need to omit () from my_snake.go_up()
    my_screen.onkey(my_snake.go_up,"Up")     
    my_screen.onkey(my_snake.go_down,"Down")
    my_screen.onkey(my_snake.go_left,"Left")
    my_screen.onkey(my_snake.go_right,"Right")

    # this loop will continue the movement of snake
    is_game_on = True
    while is_game_on: 
        my_screen.update()
        time.sleep(0.05)
        my_snake.move()

        # this will check the eating of food  by snake
        if my_snake.head.distance(snake_food) < 15 :
            my_score.add_score()
            snake_food.create_food()
            my_snake.create_new_snake_at_end()

        # this will check the collision of snakes with itself
        for each_seg in my_snake.seg_list[1:]:
            if my_snake.head.distance(each_seg) < 10:
                is_game_on = False
                my_score.game_over()

        # this will check the collision of snakes with walls
        if my_snake.head.xcor() > 280 or my_snake.head.xcor() < -280 or my_snake.head.ycor() > 280 or my_snake.head.ycor() < -280:
            is_game_on = False
            my_score.game_over()

    # this method will close the window of the game , only when we press click with our mouse
    my_screen.exitonclick()



Game()