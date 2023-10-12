from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.print_score = Turtle()
        self.print_score.goto(0, 270)
        self.print_score.color("white")
        self.print_score.hideturtle()
        self.print_score.write(f"Score: {self.score}", False, align="center", font=('Arial', 20, 'normal'))

    def increment_score(self):
        self.score += 1
