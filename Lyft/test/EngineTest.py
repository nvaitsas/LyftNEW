import unittest
from Engine import CapuletEngine, SternmanEngine, WilloughbyEngine

class CapuletEngineTest(unittest.TestCase):
    def test_needs_service_true(self):
        engine = CapuletEngine(10000, 13000)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        engine = CapuletEngine(10000, 11000)
        self.assertFalse(engine.needs_service())

class SternmanEngineTest(unittest.TestCase):
    def test_needs_service_true(self):
        engine = SternmanEngine(True)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        engine = SternmanEngine(False)
        self.assertFalse(engine.needs_service())

class WilloughbyEngineTest(unittest.TestCase):
    def test_needs_service_true(self):
        engine = WilloughbyEngine(2000, 6000)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        engine = WilloughbyEngine(2000, 3000)
        self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main()
