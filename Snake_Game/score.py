from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.setpos(0,270)
        self.ht()
        self.pencolor("white")
        self.write(f"Score: {self.score}", align='center', font=("Times New Roman", "20", "normal"))


    def point(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align='center', font=("Times New Roman", "20", "normal"))

    def game_over(self):
        self.up()
        self.goto(0, 0)
        self.down()
        self.pencolor('red')
        self.write("GAME OVER", align='center', font=("Times New Roman", "30", "normal"))





