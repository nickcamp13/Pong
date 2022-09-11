from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y=0):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x, y)

    def move_up(self):
        if self.ycor() < 240:
            self.goto(x=self.xcor(), y=self.ycor() + 20)

    def move_down(self):
        if self.ycor() > -240:
            self.goto(x=self.xcor(), y=self.ycor() - 20)
