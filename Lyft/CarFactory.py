from Car import Car, CapuletEngine, SternmanEngine, WilloughbyEngine
from Battery import Battery, SpindlerBattery, NubbinBattery

class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = SternmanEngine(False)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on):
        engine = WilloughbyEngine(last_service_date, current_date)
        return Car(engine, None)

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_date, current_date)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)
