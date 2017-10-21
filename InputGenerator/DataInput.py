import random
from .Direction import Direction

class DataInput:
    def __init__(self, this_direction):
        self.direction = this_direction
        self.max_wait = 0
        self.avg_wait = 0
        self.num_cars_waiting = 0

    # update self.max_wait, self.avg_wait, self.num_cars_waiting based on
    # currently waiting cars
    def update(self, waiting_cars_list):
        self.max_wait = 0
        sum_waits = 0
        for car in waiting_cars_list:
            sum_waits += car.time_waited
            if car.time_waited > self.max_wait:
                self.max_wait = car.time_waited
        if len(waiting_cars_list) == 0:
            self.avg_wait = 0
        else:
            self.avg_wait = sum_waits / len(waiting_cars_list)
        self.num_cars_waiting = len(waiting_cars_list)
        

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