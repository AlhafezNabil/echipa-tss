import unittest

from models import Human
import unittest


class TestHumanProperties(unittest.TestCase):
    def setUp(self):
        self.human = Human("John Doe", 3, "Earth")

    def test_planet_initial_value(self):
        """Check the initial value of the planet"""
        self.assertEqual(self.human.planet, "Earth")

    def test_planet_set_correctly(self):
        """Check the setter for the planet property"""
        self.human.planet = "Mars"
        self.assertEqual(self.human.planet, "Mars")

    def test_planet_set_incorrect_type(self):
        """Test setting an incorrect type for planet"""
        with self.assertRaises(ValueError):
            self.human.planet = 123

    def test_planet_set_empty_string(self):
        """Test setting an empty string for planet (valid as a string but you might want logic to prevent it)"""
        self.human.planet = ""
        self.assertEqual(self.human.planet, "")
