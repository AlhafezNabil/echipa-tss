import unittest

from models import Character


class TestCharacterGreaterOperator(unittest.TestCase):
    def test_greater_operator(self):
        char1 = Character("Alice", 3)
        char2 = Character("Bob", 5)
        char3 = Character("Charlie", 1)

        # Test that Bob is stronger than Alice
        self.assertTrue(char2 > char1, "Bob should be stronger than Alice")

        # Test that Charlie is not stronger than Alice
        self.assertFalse(char3 > char1, "Charlie should not be stronger than Alice")

        # Test that Charlie is not stronger than Bob
        self.assertFalse(char3 > char2, "Charlie should not be stronger than Bob")


if __name__ == '__main__':
    unittest.main()
