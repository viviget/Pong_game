from turtle import Turtle

MOVE_DISTANSE = 30

class Paddle(Turtle):
    def __init__(self, position):
        self.position=position
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('white')
        self.goto(position)

    def up(self):
        y_cor = self.ycor() + MOVE_DISTANSE
        self.goto(self.xcor(), y_cor)
    def down(self):
        y_cor = self.ycor() - MOVE_DISTANSE
        self.goto(self.xcor(), y_cor)
