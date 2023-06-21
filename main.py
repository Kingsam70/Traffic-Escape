from turtle import Screen
from user_car import UserCar
from car_manager import CarManager, list_of_cars
from scoreboard import ScoreBoard
import time
from random import randint

BG_COLOR = "pink"
should_end = False
PROBABILITY_OF_SPAWNING = 5

screen = Screen()
screen.bgcolor(BG_COLOR)
screen.setup(700, 600)
screen.title("My Game")

# Below for adding all the car gif's into the turtle screen to make it work
for cars in list_of_cars:
    screen.addshape(cars)

screen.tracer(0)
screen.listen()

user_car = UserCar()
scoreboard = ScoreBoard()
car_manager = CarManager()

screen.onkeypress(fun=user_car.move, key="Up")
car_manager.generate_car()

while True:
    screen.update()
    time.sleep(.1)

    # Generation of the cars
    if randint(0, PROBABILITY_OF_SPAWNING) == 0:  # In order to limit the spawning of the cars, basically now the spawning probability will get reduced by 5 times
        car_manager.generate_car()

    car_manager.move_cars()

    # If turtle touches the finishing line
    if user_car.ycor() > 280:
        user_car.goto_starting_point()  # Sends turtle back to initial point
        car_manager.increase_speed()
        scoreboard.increase_score()

        # Below to increase the probability of spawning after each + 4 in score
        if scoreboard.score % 4 == 0:
            PROBABILITY_OF_SPAWNING -= 1

    # Checking if turtle and cars are about to collide and if they did, it should end the program
    for car in car_manager.car_list:
        if user_car.distance(car) < 25:
            should_end = True
            break  # Breaks from the for loop

    # Ending the program
    if should_end:
        scoreboard.game_over()
        break  # Breaks from the actual while loop

    # Delete the cars which are far beyond the right edge of the screen in order to make it work well
    for car in car_manager.car_list:
        if car.xcor() > 380:
            car_manager.car_list.remove(car)
            car.goto(1000, 1000)  # In order to remove trash from the right edge of the screen, (you'll see vanishing)



screen.exitonclick()
