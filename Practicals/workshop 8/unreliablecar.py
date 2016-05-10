import random
from taxi import Car


class UnreliableCar(Car):

    def __init__(self, name="", fuel=0, reliability=0):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):

        if random.randint(0, 100) < self.reliability:
            if distance > self.fuel:
                distance_driven = self.fuel
                self.fuel = 0
            else:
                self.fuel -= distance
                distance_driven = distance
            self.odometer += distance_driven
            return distance_driven

        else:
            distance_driven = 0
            return distance_driven


