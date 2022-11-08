from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self,):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0

    def r_update(self):
        self.clear()
        self.goto(150, 265)
        self.write(arg=f"{self.r_score}", font=('Arial', 25, "normal"), move=False, align="center")

    def l_update(self):
        self.clear()
        self.goto(-150, 265)
        self.write(arg=f"{self.l_score}", font=('Arial', 25, "normal"), move=False, align="center")

    def l_count(self):
        self.l_score += 1

    def r_count(self):
        self.r_score += 1
