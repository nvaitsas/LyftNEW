import unittest
from Car import Car, CapuletEngine, SternmanEngine, WilloughbyEngine
from Battery import SpindlerBattery, NubbinBattery

class CarTest(unittest.TestCase):
    def test_needs_service_capulet_engine(self):
        engine = CapuletEngine(10000, 13000)
        car = Car(engine, None)
        self.assertTrue(car.needs_service())

    def test_needs_service_sternman_engine(self):
        engine = SternmanEngine(True)
        car = Car(engine, None)
        self.assertTrue(car.needs_service())

    def test_needs_service_willoughby_engine(self):
        engine = WilloughbyEngine(2000, 6000)
        car = Car(engine, None)
        self.assertTrue(car.needs_service())

    def test_needs_service_spindler_battery(self):
        battery = SpindlerBattery(date(2023, 1, 1), date(2023, 7, 1))
        car = Car(None, battery)
        self.assertTrue(car.needs_service())

    def test_needs_service_nubbin_battery(self):
        battery = NubbinBattery(date(2022, 1, 1), date(2023, 7, 1))
        car = Car(None, battery)
        self.assertTrue(car.needs_service())

    def test_needs_service_no_service_needed(self):
        engine = CapuletEngine(10000, 11000)
        battery = NubbinBattery(date(2023, 1, 1), date(2023, 6, 30))
        car = Car(engine, battery)
        self.assertFalse(car.needs_service())

if __name__ == '__main__':
    unittest.main()
