from turtle import Screen,Turtle
from snake import Snake
import time


def Game():
    my_screen = Screen()
    my_screen.setup(width=1200,height=1200)
    my_screen.bgcolor("Black")
    my_screen.title("Snake Game")
    my_screen.tracer(0)

    # this will create a static snake object at the center of canvas 
    my_snake = Snake()

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














    # this method will close the window of the game , only when we press click with our mouse
    my_screen.exitonclick()



Game()