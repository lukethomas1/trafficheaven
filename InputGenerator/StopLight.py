import operator
from .Direction import Direction
from .DataInput import DataInput
from .LightState import LightState

class StopLight:
    def __init__(self):
        self.direction_inputs = {}
        self.costs = {}
        self.state_costs = {}

    def fill(self):
        for direction in Direction:
            self.direction_inputs[direction] = DataInput(direction)

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

    def get_input(self):
        input_list = []
        for key in self.costs:
            input_list += self.direction_inputs[key].get_inputs()
        return input_list
    
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