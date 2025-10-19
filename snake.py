from turtle import Turtle

# these are constant values
SEG_POSSIOTION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.seg_list=[]
        self.create_snake()
        self.head = self.seg_list[0]  

    # this function will create initial snake
    def create_snake(self):
        for position in SEG_POSSIOTION:
            seg = Turtle(shape="square")
            seg.color("White")
            seg.penup()
            seg.goto(position)
            self.seg_list.append(seg)

    # this function will create a new snake after eating the food
    def create_new_snake_at_end(self):
            new_snake = Turtle(shape="square")
            new_snake.color("White")
            new_snake.penup()
            position = None

            new_snake_x = self.seg_list[len(self.seg_list)-1].xcor()
            new_snake_y = self.seg_list[len(self.seg_list)-1].ycor()

            new_snake.goto(new_snake_x,new_snake_y)
            self.seg_list.append(new_snake)

    # this function will move the snake
    def move(self):
        for seg_number in range(len(self.seg_list)-1,0,-1):
            new_xp= self.seg_list[seg_number-1].xcor()
            new_yp= self.seg_list[seg_number-1].ycor()
            self.seg_list[seg_number].goto(new_xp,new_yp)
        self.head.forward(MOVE_DISTANCE)
    
    # this function will move our snake up
    def go_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    # this function will move our snake down
    def go_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    # this function will move our snake left
    def go_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    # this function will move our snake right   
    def go_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)