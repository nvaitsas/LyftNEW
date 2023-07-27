from Serviceable import Serviceable
from datetime import date

class Battery(Serviceable):
    pass

class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        return (self.current_date - self.last_service_date).days >= 180

class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        return (self.current_date - self.last_service_date).days >= 365
