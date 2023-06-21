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





# Please ignore the issue where the cars are so near or overlaping with each other i could have just checked for
# overlaping and repositioned that very car to different position but it could have overlaped to another car in
# list_of_cars, In order to prevent collisions with all the cars the spawning of cars should be at a fixed rate or
# the spawning should be at a fixed place meaning spawining should only take place at pre defined positions
# if using 10 pace distance if you'd use 30 it'll be fixed but the speed of the cars will hugely impace(increase)
# , In our example neither of the two are taken under consideration


# also pls bear that if you collide with a car in x-direction/horizontally the car will overlap you meaning you'll get
# into the car, meaning the programm will not end on touching cause due to different height and width of the gif car
# images also turtle size is fixed i.e 20*20

# Also you can add high score mechanism using txt file but not felt the need

# Turtle cannot move backwards