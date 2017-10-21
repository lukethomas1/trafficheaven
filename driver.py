from time import sleep
from InputGenerator.LightSimulator import LightSimulator

new_car_chance = 0.1
max_cars_per_chance = 3
sim = LightSimulator(new_car_chance, max_cars_per_chance)

max_turns = 500
curr_turns = 0

while curr_turns < max_turns:
    sim.update()
    curr_turns += 1
    sleep(3)