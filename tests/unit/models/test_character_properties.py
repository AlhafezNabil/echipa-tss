import unittest

from models import Character


class TestCharacterProperties(unittest.TestCase):
    def test_initial_strength_values(self):
        """Test strength values are clamped within the allowed range"""
        char_high = Character("High", 10)
        char_low = Character("Low", -1)
        self.assertEqual(char_high.strength, 5)
        self.assertEqual(char_low.strength, 0)

    def test_strength_type_error(self):
        """Test that setting strength to a non-numeric value raises an error"""
        char = Character("Tester", 3)
        with self.assertRaises(ValueError) as context:
            char.strength = "strong"
        self.assertIn("Strength must be a number.", str(context.exception))

    def test_strength_range_error(self):
        """Test that setting strength outside the range [0, 5] raises an error"""
        char = Character("Tester", 3)
        with self.assertRaises(ValueError) as context:
            char.strength = 7
        self.assertIn("Strength must be between 0 and 5.", str(context.exception))

    def test_name_type_error(self):
        """Test that setting name to a non-string raises an error"""
        char = Character("ValidName", 2)
        with self.assertRaises(ValueError) as context:
            char.name = 12345
        self.assertIn("Name must be a string.", str(context.exception))
