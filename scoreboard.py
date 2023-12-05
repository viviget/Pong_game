from turtle import Turtle
class Scoreboard(Turtle):
     def __init__(self):
         super().__init__()
         self.r_score = 0
         self.l_score = 0
         self.hideturtle()
         self.penup()
         self.color('white')
         self.goto(0, 200)
         self.write(arg=f'{self.l_score} : {self.r_score}', align='center', font=('Courier', 70, 'normal'))

     def l_scoreplus(self):
         self.l_score+=1
         self.clear()
         self.write(arg=f'{self.l_score} : {self.r_score}', align='center', font=('Courier', 70, 'normal'))
     def r_scoreplus(self):
         self.r_score+=1
         self.clear()
         self.write(arg=f'{self.l_score} : {self.r_score}', align='center', font=('Courier', 70, 'normal'))
