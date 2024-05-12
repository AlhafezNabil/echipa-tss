import unittest

from models import Character
from models.alien import Alien
from models.human import Human


class TestAlienHuman(unittest.TestCase):

    def test_alien_technology(self):
        alien = Alien("Zorg", 3, True)
        self.assertTrue(alien.advancedTech)

    def test_invalid_alien_technology_type(self):
        with self.assertRaises(ValueError):
            Alien("Zorg", 3, "yes")

    def test_human_planet(self):
        human = Human("John Doe", 2, "Earth")
        self.assertEqual(human.planet, "Earth")

    def test_invalid_human_planet_type(self):
        with self.assertRaises(TypeError):
            Human("John Doe", 2, 404)


class TestCharacterInteraction(unittest.TestCase):

    def test_fight_winner(self):
        char1 = Character("Hero", 5)
        char2 = Character("Villain", 3)
        char1.fight(char2)
        self.assertEqual(char1.strength, 5)
        self.assertEqual(char2.strength, 3)

    def test_fight_strength_increase(self):
        char1 = Character("Hero", 4)
        char2 = Character("Villain", 3)
        char1.fight(char2)
        self.assertEqual(char1.strength, 5)


if __name__ == '__main__':
    unittest.main()
