from turtle import Turtle


class CreateBlock(Turtle):
    def __init__(self, x_position, y_position):
        super().__init__()
        self.x_position = x_position
        self.y_position = y_position
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(self.x_position, self.y_position)

    def move_up(self):
        position = self.ycor() + 20
        self.goto(self.xcor(), position)

    def move_down(self):
        position = self.ycor() - 20
        self.goto(self.xcor(), position)
