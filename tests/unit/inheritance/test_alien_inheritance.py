import unittest

from models import Alien, Character

import unittest


class TestAlienInheritance(unittest.TestCase):
    def test_alien_base_class(self):
        """Check if Alien correctly inherits from Character"""
        self.assertTrue(issubclass(Alien, Character))
        self.assertEqual(Alien.__bases__, (Character,))

    def test_alien_method_overriding(self):
        """Check if __str__ method is correctly overridden in Alien"""
        self.assertNotEqual(Alien.__str__.__qualname__, 'Character.__str__')
        self.assertEqual(Alien.__str__.__qualname__, 'Alien.__str__')

        """Ensure __gt__ method is specifically tailored for Alien"""
        self.assertEqual(Alien.__gt__.__qualname__, 'Alien.__gt__')

        """Fight method should be inherited and not overridden if it behaves the same"""
        self.assertEqual(Alien.fight.__qualname__, 'Character.fight')

    def test_advanced_tech_property(self):
        """Ensure advancedTech property is specific to Alien and correctly setup"""
        alien = Alien("Zorg", 3, True)
        self.assertTrue(hasattr(alien, 'advancedTech'))
        self.assertTrue(alien.advancedTech)

        """Attempt to set advancedTech and check for type enforcement"""
        with self.assertRaises(ValueError):
            alien.advancedTech = "not a boolean"

        """Check that setting to a correct value works"""
        alien.advancedTech = False
        self.assertFalse(alien.advancedTech)


if __name__ == '__main__':
    unittest.main()
