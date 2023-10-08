
from car import Car

class NubbinBattery(Car):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date.year
        self.current_date = current_date.year

    def battery_should_be_serviced(self):
        return self.current_date - self.last_service_date < 4
