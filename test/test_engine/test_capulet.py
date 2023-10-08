import unittest
from engine.capulet_engine import CapuletEngine

class CapuletTest(unittest.TestCase):
    def test_service_needed(self):
        current_mileage = 40000
        last_service_mileage = 0 
        engine = CapuletEngine(current_mileage,last_service_mileage)
        self.assertTrue(engine.engine_should_be_serviced())

    def test_service_not_needed(self):
        current_mileage = 25000
        last_service_mileage = 0 
        engine = CapuletEngine(current_mileage,last_service_mileage)
        self.assertFalse(engine.engine_should_be_serviced())