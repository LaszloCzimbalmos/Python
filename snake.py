from turtle import Turtle, Screen

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        x = 0
        for i in range(3):
            self.add_segment(x, 0)
            x-=20

    def add_segment(self, xcor, ycor):
        t = Turtle(shape='square')
        t.color('white')
        t.up()
        t.setpos(x=xcor, y=ycor)
        self.segments.append(t)

    def extend(self):
        self.add_segment(xcor=self.segments[-1].xcor(), ycor=self.segments[-1].ycor())

    def move(self):
        for pos in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[pos - 1].xcor()
            new_y = self.segments[pos - 1].ycor()
            self.segments[pos].goto(new_x, new_y)

        self.head.forward(20)

    #movements
    def up(self):
        if(self.head.heading() != DOWN):
            self.head.setheading(UP)

    def down(self):
        if (self.head.heading() != UP):
            self.head.setheading(DOWN)

    def right(self):
        if (self.head.heading() != LEFT):
            self.head.setheading(RIGHT)

    def left(self):
        if (self.head.heading() != RIGHT):
            self.head.setheading(LEFT)
