from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0,250)
        self.color('white')
        self.write(f'Score: {self.score}' , align='center' , font = ('Courier',16,'normal'))
        self.hideturtle()

    def refresh(self):
        self.score+=1
        self.clear()
        self.write(f'Score: {self.score}' , align='center' , font = ('Courier',16,'normal'))
        
