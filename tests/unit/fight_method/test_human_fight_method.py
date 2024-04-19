from models import Human

import unittest
from io import StringIO
import sys


class TestHumanFightMethod(unittest.TestCase):
    def setUp(self):
        # Redirect stdout to capture prints
        self.held, sys.stdout = sys.stdout, StringIO()

    def tearDown(self):
        # Restore stdout
        sys.stdout = self.held

    def test_fight_method_humans(self):
        # Create Humans
        human1 = Human("Alice", 3, "Earth")
        human2 = Human("Bob", 4, "Earth")

        # Attempt to make them fight
        with self.assertRaises(ValueError):
            human1.fight(human2)
        self.assertEqual(sys.stdout.getvalue().strip(), "Humans cannot fight among each other.")

        # Reset stdout
        sys.stdout = StringIO()

    def test_fight_method_with_character(self):
        # Create a Human and a Character
        human = Human("Alice", 3, "Earth")
        alien = Human("Charlie", 2, "Mars")  # Technically a Human, should also not fight

        # Humans should not fight each other
        with self.assertRaises(ValueError):
            human.fight(alien)
        self.assertEqual(sys.stdout.getvalue().strip(), "Humans cannot fight among each other.")


if __name__ == '__main__':
    unittest.main()
