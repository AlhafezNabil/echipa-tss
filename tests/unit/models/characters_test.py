import unittest

from models.alien import Alien
from models.astronaut import Astronaut
from models.character import Character
from models.commander import Commander
from models.human import Human


class CharactersTest(unittest.TestCase):
    def test_character_initialization(self):
        """Test the initialization of the Character class"""
        char = Character("Test", 5)
        self.assertEqual(char.name, "Test")
        self.assertEqual(char.strength, 5)

    def test_alien_technology(self):
        """Test the special logic for Alien technology advantage"""
        alien1 = Alien("Alien1", 3, True)
        alien2 = Alien("Alien2", 4, False)
        self.assertTrue(alien1 > alien2)

    def test_human_cannot_fight_human(self):
        """Ensure Humans cannot fight each other"""
        human1 = Human("Human1", 3, "Earth")
        human2 = Human("Human2", 4, "Earth")
        with self.assertRaises(ValueError):
            human1.fight(human2)

    def test_commander_crew_management(self):
        """Test adding crew to a Commander"""
        commander = Commander("Cmdr", 3, "Mars")
        astronaut = Astronaut("Astro", 2, "Mars")
        commander.add_crew_member(astronaut)
        self.assertIn(astronaut, commander.crew)

    def test_values_range_character(self):
        """Test to ensure that strength does not exceed the limits [0,5]"""
        char1 = Character("Char1", 6)
        self.assertEqual(char1.strength, 5)

        char2 = Character("Char2", -1)
        self.assertEqual(char2.strength, 0)

    def test_value_types_character(self):
        """Test to ensure that initializing with wrong types raises an error or is handled"""
        with self.assertRaises(TypeError):
            char = Character(123, 5)

        with self.assertRaises(TypeError):
            char = Character("Char", "high")

    def test_alien_constructor(self):
        """Test for alien with correct boundary strength values and advanced tech flag"""
        alien = Alien("Alien1", 5.5, True)
        self.assertEqual(alien.strength, 5)
        self.assertTrue(isinstance(alien.advancedTech, bool))

    def test_human_constructor(self):
        """Humans should not accept invalid planet names (type checking)"""
        with self.assertRaises(TypeError):
            human = Human("Human1", 3, 123)


if __name__ == '__main__':
    unittest.main(verbosity=2)
    # captured_output = io.StringIO()
    # sys.stdout = captured_output
    # unittest.main(verbosity=2)
    # sys.stdout = sys.__stdout__
    # captured_output.getvalue()
