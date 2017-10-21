import operator
from .Direction import Direction
from .DataInput import DataInput
from .LightState import LightState

class StopLight:
    def __init__(self, minimum_direction_seconds):
        # Minimum seconds until the light can change direction again
        self.minimum_seconds_left = minimum_direction_seconds

        # self.current_state = LightState
        self.current_state = LightState.North

        # self.previous_state = LightState
        self.previous_state = None

        # self.next_state = LightState
        self.next_state = None

        # self.minimum_seconds_left = integer
        self.minimum_seconds_left = 0

        # self.is_yellow = Boolean
        self.is_yellow = False

        # self.yellow_seconds_left = integer, between 0 and 3
        self.yellow_seconds_left = 0

        # self.waiting_lists[Direction] = List(Car)
        self.waiting_lists = {}
        for direction in Direction:
            self.waiting_lists[direction] = []

        # self.incoming_cars[Direction] = List(Car)
        self.incoming_cars = {}
        for direction in Direction:
            self.incoming_cars[direction] = []

        # self.direction_inputs[Direction] = DataInput
        self.direction_inputs = {}
        for direction in Direction:
            self.direction_inputs[direction] = DataInput(direction)

        # self.costs[Direction] = integer
        self.costs = {}
        for direction in Direction:
            self.costs[direction] = 0

        # self.state_costs[LightState] = integer
        self.state_costs = {}
        for state in LightState:
            self.state_costs[state] = 0

    def update(self):
        # The light must remain a certain direction until this is 0
        if self.minimum_seconds_left > 0:
            self.minimum_seconds_left = self.minimum_seconds_left - 1

        # Keep track of outgoing cars so we can pipe them to the next StopLight
        outgoing_cars = {}
        for direction in Direction:
            outgoing_cars[direction] = []

        # Remove one car per waiting queue that can go
        for direction in self.current_state.value:
            if len(self.waiting_lists[direction]) > 0:
                self.waiting_lists[direction].pop(0)

        # update() every car that is waiting
        for waiting_list in self.waiting_lists.values():
            for car in waiting_list:
                car.update()

        # update() every car that is incoming, important that this is after
        # updating the waiting cars
        for direction in self.incoming_cars.keys():
            for car in self.incoming_cars[direction]:
                car.update()
                # If the car got to the light, switch the list it is in
                if car.seconds_away == 0:
                    self.incoming_cars[direction].remove(car)
                    # If the light is red, add it to the waiting list
                    if direction not in self.current_state.value:
                        self.waiting_lists[direction].append(car)
                    # If there are cars in line, this car can't blast through,
                    # add it to the waiting list
                    elif len(self.waiting_lists[direction]) > 0:
                        self.waiting_lists[direction].append(car)

        # Update the costs after updating the waiting and incoming car lists
        for direction in self.direction_inputs.keys():
            self.direction_inputs[direction].update(self.waiting_lists[direction])

        # Update cost functions
        self.calc_costs()
        
        if self.is_yellow:
            self.yellow_seconds_left = self.yellow_seconds_left - 1
            if self.yellow_seconds_left == 0:
                self.is_yellow = False
                self.previous_state = self.current_state
                self.current_state = self.next_state
                self.next_state = None
                self.minimum_seconds_left = 10

        return outgoing_cars

    def add_incoming_car(self, direction, car):
        self.incoming_cars[direction].append(car)

    def change_light_direction(self, new_light_state):
        if self.minimum_seconds_left <= 0 and not self.is_yellow:
            print("Changing light state to " + str(new_light_state))
            self.next_state = new_light_state
            self.is_yellow = True
            self.yellow_seconds_left = 3
        else:
            print("Couldn't change light state: " + str(self.minimum_seconds_left) + " seconds left!")

    def randomize(self):
        for key in self.direction_inputs.keys():
            self.direction_inputs[key].randomize()

    def calc_costs(self):
        for key in self.direction_inputs.keys():
            self.costs[key] = self.direction_inputs[key].get_cost()

    def determine_correct_state(self):
        for state in LightState:
            self.state_costs[state] = 0
            for key in state.value:
                self.state_costs[state] += self.costs[key]
        sorted_costs = sorted(self.state_costs.items(), key=operator.itemgetter(1))
        return sorted_costs[-1][0]

    # Get input for machine learning
    def get_input(self):
        input_list = []
        for key in self.costs:
            input_list += self.direction_inputs[key].get_inputs()
        return input_list
    
    # Get "correct" output for machine learning
    def get_output(self):
        return self.determine_correct_state()

    def print_costs(self):
        for key in self.costs:
            print(key.name + ": ")
            print("Inputs: " + str(self.direction_inputs[key].to_string()))
            print("Cost: " + str(self.costs[key]))
            print()

    def print_state_costs(self):
        for key in self.state_costs:
            print(str(key) + ": " + str(self.state_costs[key]))