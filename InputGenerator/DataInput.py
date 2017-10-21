import random
from .Direction import Direction

class DataInput:
    def __init__(self, this_direction):
        self.direction = this_direction
        self.max_wait = 0
        self.avg_wait = 0
        self.num_cars_waiting = 0

    def randomize(self):
        self.num_cars_waiting = random.randint(0, 10)
        if self.num_cars_waiting == 0:
            self.avg_wait = 0
            self.max_wait = 0
        else:
            self.avg_wait = random.randint(1, 60)
            self.max_wait = random.randint(self.avg_wait, self.avg_wait + 90)

    def get_cost(self):
        max_wait_cost = (self.max_wait - 100) * 3
        max_wait_cost = max_wait_cost if max_wait_cost > 0 else 0
        return self.avg_wait * self.num_cars_waiting + max_wait_cost

    def get_inputs(self):
        return [self.max_wait, self.avg_wait, self.num_cars_waiting]

    def to_string(self):
        tuple_rep = (self.max_wait, self.avg_wait, self.num_cars_waiting)
        return str(tuple_rep)