from turtle import Turtle
TURTLE_COLOR = "black"


class UserCar(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color(TURTLE_COLOR)
        self.penup()
        self.setheading(90)
        self.goto(0, -283)

    def move(self):
        """moves the turtle/user_car forward by 10 paces"""
        self.forward(10)

    def goto_starting_point(self):
        """makes turtle/user_car go back to initial/starting point"""
        self.goto(0, -283)
