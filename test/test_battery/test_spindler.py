import unittest
from datetime import date

from engine.spindler_battery import SpindlerBattery


class TestSplinderBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2022-05-15")
        last_service_date = date.fromisoformat("2016-01-25")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2019-01-10")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())