import unittest

from models import Human


class TestHumanConstructor(unittest.TestCase):
    def test_strength_clamping(self):
        """Test that strength is clamped to the maximum value of 5"""
        human_high = Human("John", 6, "Earth")
        self.assertEqual(human_high.strength, 5)

        """Test that strength is clamped to the minimum value of 0"""
        human_low = Human("Jane", -1, "Earth")
        self.assertEqual(human_low.strength, 0)

    def test_strength_initial_values(self):
        """Test normal strength initialization within the allowed range"""
        human_normal = Human("Alice", 4, "Mars")
        self.assertEqual(human_normal.strength, 4)

    def test_planet_initialization(self):
        """Ensure the planet is correctly initialized as a string"""
        human = Human("Bob", 3, "Venus")
        self.assertEqual(human.planet, "Venus")

    def test_invalid_planet_type(self):
        """Ensure setting an incorrect type for planet raises an error"""
        with self.assertRaises(TypeError):
            human_wrong_planet = Human("Carl", 3, 123)

    def test_invalid_strength_type(self):
        """Ensure that providing a non-numeric type for strength raises an error"""
        with self.assertRaises(TypeError):
            human_wrong_strength = Human("Diana", "strong", "Jupiter")


if __name__ == '__main__':
    unittest.main()
