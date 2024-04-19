import unittest

from models import Alien, Astronaut


class TestAstronautConstructor(unittest.TestCase):
    def test_strength_clamping(self):
        """Test that strength is clamped to the maximum value of 5"""
        astronaut_high = Astronaut("Neil", 10, "Mars")
        self.assertEqual(astronaut_high.strength, 5)

        """Test that strength is clamped to the minimum value of 0"""
        astronaut_low = Astronaut("Buzz", -1, "Mars")
        self.assertEqual(astronaut_low.strength, 0)

    def test_strength_initial_values(self):
        """Test normal strength initialization within the allowed range"""
        astronaut_normal = Astronaut("Sally", 4, "Mars")
        self.assertEqual(astronaut_normal.strength, 4)

    def test_planet_initialization(self):
        """Ensure the planet is correctly initialized"""
        astronaut = Astronaut("Yuri", 3, "Earth")
        self.assertEqual(astronaut.planet, "Earth")

    def test_invalid_planet_type(self):
        """Ensure setting an incorrect type for planet raises an error"""
        with self.assertRaises(TypeError):
            astronaut_wrong_planet = Astronaut("Valentina", 3, 123)

    def test_invalid_strength_type(self):
        """Ensure setting an incorrect type for strength raises an error"""
        with self.assertRaises(TypeError):
            astronaut_wrong_strength = Astronaut("Michael", "High", "Mars")


if __name__ == '__main__':
    unittest.main()
