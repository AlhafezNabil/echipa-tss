import unittest

from models import Human
import unittest

import unittest


class TestHumanGreaterOperator(unittest.TestCase):
    def test_greater_operator(self):
        # Create Humans with varying strengths
        human1 = Human("Alice", 4, "Earth")
        human2 = Human("Bob", 6, "Mars")
        human3 = Human("Charlie", 2, "Venus")

        # Test that Bob is stronger than Alice
        self.assertTrue(human2 > human1, "Bob should be stronger than Alice")

        # Test that Charlie is not stronger than Alice
        self.assertFalse(human3 > human1, "Charlie should not be stronger than Alice")

        # Test that Charlie is not stronger than Bob
        self.assertFalse(human3 > human2, "Charlie should not be stronger than Bob")


if __name__ == '__main__':
    unittest.main()
