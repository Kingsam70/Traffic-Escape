from turtle import Turtle, Screen
from random import randint, choice

# Below car is 60*30
list_of_cars = [f"./Cars/cargif{n + 1}.gif" for n in range(6)]


class CarManager:
    def __init__(self):
        self.car_list = []
        self.move_distance = 10

    def generate_car(self):
        """generates a random car beyond the screen"""
        tim = Turtle()
        tim.shape(choice(list_of_cars))
        tim.setheading(0)
        tim.penup()
        tim.goto(-370, randint(-250, 260))  # Sending a car on the left side of the screen
        self.car_list.append(tim)

    def move_cars(self):
        """moves the cars in cars_list forward by 10 paces"""
        for car in self.car_list:
            car.forward(self.move_distance)

    def increase_speed(self):
        """increment in speed by +5 """
        self.move_distance += 5

