from models.character import Character

import unittest


class TestCharacterConstructor(unittest.TestCase):
    def test_strength_clamping(self):
        """Test that strength is clamped to the maximum value of 5"""
        char_high = Character("HighStr", 10)
        self.assertEqual(char_high.strength, 5)

        """Test that strength is clamped to the minimum value of 0"""
        char_low = Character("LowStr", -1)
        self.assertEqual(char_low.strength, 0)

    def test_strength_initial_values(self):
        """Test normal strength initialization within the allowed range"""
        char_normal = Character("Normal", 3)
        self.assertEqual(char_normal.strength, 3)

    def test_type_safety_name(self):
        """Test that providing a non-string type for name raises an error"""
        with self.assertRaises(TypeError):
            char_wrong_name = Character(123, 3)

    def test_type_safety_strength(self):
        """Test that providing a non-numeric type for strength raises an error"""
        with self.assertRaises(TypeError):
            char_wrong_strength = Character("Name", "Strong")


if __name__ == '__main__':
    unittest.main()
