from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        self.hideturtle()
        self.penup()
        self.goto(-280, 270)
        self.write(f"Score: {self.score}", move=False, align="left", font=("Arial", 18, "normal"))

    def increase_score(self):
        """increases the score when turtle reaches the finish line"""
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", move=False, align="left", font=("Arial", 18, "normal"))

    def game_over(self):
        """game over displayed on the screen"""
        self.home()
        self.write("GAME OVER", move=False, align="center", font=("Arial", 30, "normal"))

