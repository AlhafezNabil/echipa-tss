import unittest

from models import Alien


class TestAlienProperties(unittest.TestCase):
    def setUp(self):
        self.alien1 = Alien("Zorblatt", 5, True)
        self.alien2 = Alien("GlipGlop", 3, False)

    def test_advanced_tech_initial_value(self):
        """Test the initial values of advancedTech"""
        self.assertTrue(self.alien1.advancedTech)
        self.assertFalse(self.alien2.advancedTech)

    def test_advanced_tech_setter(self):
        """Test the setter for advancedTech"""
        self.alien1.advancedTech = False
        self.assertFalse(self.alien1.advancedTech)
        self.alien2.advancedTech = True
        self.assertTrue(self.alien2.advancedTech)

    def test_advanced_tech_setter_invalid_type(self):
        """Test setting an incorrect type for advancedTech"""
        with self.assertRaises(ValueError):
            self.alien1.advancedTech = "yes"

    def test_comparison_with_advanced_tech(self):
        """Test comparison based on advancedTech"""
        self.alien2.advancedTech = True
        self.assertFalse(self.alien1 < self.alien2)
        self.assertTrue(self.alien2.strength < self.alien1.strength)

    def test_comparison_without_advanced_tech(self):
        """Test comparison when only one has advancedTech"""
        self.assertTrue(self.alien1 > self.alien2)


if __name__ == '__main__':
    unittest.main()
