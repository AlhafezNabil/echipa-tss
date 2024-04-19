import unittest

from models import Astronaut


class TestAstronautProperties(unittest.TestCase):
    def setUp(self):
        self.astronaut = Astronaut("Neil", 4, "Mars")

    def test_planet_initial_value(self):
        """Ensure the planet is correctly initialized"""
        self.assertEqual(self.astronaut.planet, "Mars")

    def test_planet_set_correctly(self):
        """Ensure the planet property can be updated correctly"""
        self.astronaut.planet = "Jupiter"
        self.assertEqual(self.astronaut.planet, "Jupiter")

    def test_planet_set_incorrect_type(self):
        """Ensure setting an incorrect type for planet raises an error"""
        with self.assertRaises(ValueError):
            self.astronaut.planet = 987

    def test_strength_within_bounds(self):
        """Ensure strength adheres to bounds set in Human"""
        with self.assertRaises(ValueError):
            self.astronaut.strength = 6
        with self.assertRaises(ValueError):
            self.astronaut.strength = -1


    def test_invalid_strength_type(self):
        """Test setting an invalid type for strength"""
        with self.assertRaises(ValueError):
            self.astronaut.strength = "high"
