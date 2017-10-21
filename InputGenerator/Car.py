class Car:
    def __init__(self, seconds_away):
        self.seconds_away = seconds_away
        self.time_waited = 0

    def update(self):
        if self.seconds_away > 0:
            self.seconds_away = self.seconds_away - 1
        else:
            self.time_waited = self.time_waited + 1