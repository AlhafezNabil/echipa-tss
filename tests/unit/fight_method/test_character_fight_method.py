from models.character import Character

import unittest

from io import StringIO
import sys


class TestCharacterFightMethod(unittest.TestCase):
    def setUp(self):
        # Redirect stdout to capture prints
        self.held, sys.stdout = sys.stdout, StringIO()

    def tearDown(self):
        # Restore stdout
        sys.stdout = self.held

    def test_fight_method(self):
        # Create Characters with varying strengths
        char1 = Character("Alice", 3)
        char2 = Character("Bob", 5)
        char3 = Character("Charlie", 2)

        # Alice fights Bob, Bob should win
        char1.fight(char2)
        self.assertEqual(sys.stdout.getvalue().strip(), "Bob wins and now has strength 5")
        self.assertEqual(char2.strength, 5)

        # Reset stdout
        sys.stdout = StringIO()

        # Charlie fights Alice, Alice should win
        char3.fight(char1)
        self.assertEqual(sys.stdout.getvalue().strip(), "Alice wins and now has strength 3")
        self.assertEqual(char1.strength, 3)

        # Reset stdout
        sys.stdout = StringIO()

        # Bob fights Charlie, Bob should win and increase strength
        char2.fight(char3)
        self.assertEqual(sys.stdout.getvalue().strip(),
                         "Bob wins and now has strength 5")  # Bob is already at max strength
        self.assertEqual(char2.strength, 5)


if __name__ == '__main__':
    unittest.main()
