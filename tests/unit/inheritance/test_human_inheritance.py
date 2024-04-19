import unittest

from models import Human, Character, Commander, Astronaut, Alien

import unittest


class TestHumanInheritance(unittest.TestCase):
    def test_human_base_class(self):
        """Check if Human directly inherits from Character"""
        self.assertTrue(issubclass(Human, Character))
        self.assertEqual(Human.__bases__, (Character,))

    def test_human_method_inheritance(self):
        """Check that fight method is overridden in Human"""
        self.assertNotEqual(Human.fight.__qualname__, 'Character.fight')
        self.assertEqual(Human.fight.__qualname__, 'Human.fight')

        """Check that __str__ method is overridden in Human"""
        self.assertNotEqual(Human.__str__.__qualname__, 'Character.__str__')
        self.assertEqual(Human.__str__.__qualname__, 'Human.__str__')

        """Check inheritance in subclasses of Human"""
        self.assertTrue(issubclass(Astronaut, Human))
        self.assertTrue(issubclass(Commander, Human))

        """Ensure Astronaut and Commander have not redefined fight unnecessarily"""
        self.assertEqual(Astronaut.fight.__qualname__, 'Human.fight')
        self.assertEqual(Commander.fight.__qualname__, 'Human.fight')

        """Check for specific method overriding in subclasses"""
        self.assertEqual(Astronaut.__str__.__qualname__, 'Astronaut.__str__')
        self.assertEqual(Commander.__str__.__qualname__, 'Commander.__str__')

    def test_advanced_tech_inheritance(self):
        """Verify that Alien does not share the same base class method implementations"""
        self.assertNotEqual(Alien.fight.__qualname__, 'Human.fight')
        self.assertNotEqual(Alien.__str__.__qualname__, 'Human.__str__')
        self.assertEqual(Alien.__gt__.__qualname__, 'Alien.__gt__')


if __name__ == '__main__':
    unittest.main()
