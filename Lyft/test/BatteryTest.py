import unittest
from Battery import SpindlerBattery, NubbinBattery
from datetime import date

class SpindlerBatteryTest(unittest.TestCase):
    def test_needs_service_true(self):
        battery = SpindlerBattery(date(2023, 1, 1), date(2023, 7, 1))
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        battery = SpindlerBattery(date(2023, 1, 1), date(2023, 3, 1))
        self.assertFalse(battery.needs_service())

class NubbinBatteryTest(unittest.TestCase):
    def test_needs_service_true(self):
        battery = NubbinBattery(date(2022, 1, 1), date(2023, 7, 1))
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        battery = NubbinBattery(date(2023, 1, 1), date(2023, 3, 1))
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()
