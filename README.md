# Traffic-Escape
"Traffic Escape using turtle is a thrilling and intense game that will test your agility and strategic thinking as you navigate through a chaotic urban jungle. Take control of your trusty turtle and embark on a daring escape from the relentless traffic that surrounds you

Features
Easy and intuitive gameplay.
Avoid collisions and navigate through traffic.
Simple controls using just arrow key(Up).
Increasing difficulty as you progress.
Track your high score and try to beat it.

How to Play
Use the arrow key.
Navigate through the traffic, avoiding collisions.
Reach the endpoint without crashing to score points.
The game ends if you collide with another car.
Challenge yourself to beat your high score.

Requirements
Python 3.x

Feel free to customize the README file further based on your specific game details and requirements. Enjoy playing Traffic Escape and have fun escaping the traffic!

NOTE:
1. Please disregard the issue where the cars are too close or overlapping with each other. I could have checked for overlaps and repositioned the cars to different positions, but that could have caused collisions with other cars in the list_of_cars.
To prevent collisions with all the cars, the spawning of cars should either be at a fixed rate or at fixed positions. For example, if you use a distance of 10 paces between cars, you can adjust it to 30 paces to ensure no overlaps. However, keep in mind that increasing the distance will significantly impact the speed of the cars.
In our current example, neither of these considerations have been taken into account.

2. Please note that if you collide with a car horizontally (in the x-direction), the car will overlap with your vehicle. This means that the program will not end immediately upon collision, as the overlap is due to the different height and width of the car GIF images compared to the fixed size of the turtle.
The turtle size is set to a fixed value of 20 pixels by 20 pixels. Therefore, collision detection may not be entirely accurate, as it does not consider the actual dimensions of the car image

3. Also you can add high score mechanism using txt file

4. # user_car is turtle
