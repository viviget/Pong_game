from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        #self.shapesize(outline=6)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1


    def move(self):
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        self.goto(x_cor, y_cor)

    def bounce_y(self):
        #only need to change the Y to another direction.
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1






