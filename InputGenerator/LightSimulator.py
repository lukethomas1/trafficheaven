import random
from .StopLight import StopLight
from .Direction import Direction
from .Car import Car

class LightSimulator:
    def __init__(self, new_car_chance, max_cars_per_chance):
        self.new_car_chance = new_car_chance
        self.max_cars_per_chance = max_cars_per_chance
        self.light = StopLight(10)

    def update(self):
        print()
        self.light.update()
        best_move = self.light.get_output()
        self.light.change_light_direction(best_move)
        print("Best move: " + str(best_move))
        self.generate_new_cars()
        self.light.print_state_costs()

    def generate_new_cars(self):
        new_cars = {}
        for direction in Direction:
            new_cars[direction] = []
            seconds_away = 5
            num_cars = random.randint(1, self.max_cars_per_chance)
            if random.random() < self.new_car_chance:
                print("Generating " + str(num_cars) + " incoming cars towards "\
                + str(direction) + "!")
                for car_index in range(num_cars):
                    this_car = Car(seconds_away + car_index)
                    self.light.add_incoming_car(direction, this_car)

    def get_inputs(self):
        return self.light.get_input()

    def get_outputs(self):
        return self.light.get_output()