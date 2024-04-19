import unittest

from models import Alien


class TestAlienConstructor(unittest.TestCase):
    def test_strength_clamping(self):
        """Test that strength is clamped to the maximum value of 5"""
        alien_high = Alien("Xal'atath", 7, True)
        self.assertEqual(alien_high.strength, 5)

        """Test that strength is clamped to the minimum value of 0"""
        alien_low = Alien("Zarvox", -3, False)
        self.assertEqual(alien_low.strength, 0)

    def test_strength_initial_values(self):
        """Test normal strength initialization within the allowed range"""
        alien_normal = Alien("Klaxxi", 4, True)
        self.assertEqual(alien_normal.strength, 4)

    def test_advanced_tech_type(self):
        """Test that the advancedTech attribute is correctly initialized"""
        alien_tech = Alien("Mogor", 2, True)
        self.assertTrue(isinstance(alien_tech.advancedTech, bool))

    def test_advanced_tech_type_error(self):
        """Test that providing a non-boolean type for advancedTech raises an error"""
        with self.assertRaises(ValueError):
            alien_wrong_tech = Alien("Kilrogg", 3, "yes")


if __name__ == '__main__':
    unittest.main()
