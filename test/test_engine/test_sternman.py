import unittest
from engine.sternman_engine import SternmanEngine

class SternmanTest(unittest.TestCase):
    def test_service_needed(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.engine_should_be_serviced())

    def test_service_not_needed(self):
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.engine_should_be_serviced())