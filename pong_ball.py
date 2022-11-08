from turtle import Turtle


class CreateBall(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.y_position = 10
        self.x_position = 10

    def move_ball(self):
        x_pos = self.xcor() + self.x_position
        y_pos = self.ycor() + self.y_position
        self.goto(x_pos, y_pos)

    def change_y(self):
        self.y_position *= -1

    def change_x(self):
        self.x_position *= -1

    def change_direction(self):
        self.x_position -= 20
        self.y_position -= 20
