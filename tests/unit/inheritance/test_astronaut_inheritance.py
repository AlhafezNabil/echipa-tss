import unittest

from models import Astronaut, Human

import unittest


class TestAstronautInheritance(unittest.TestCase):
    def test_astronaut_inheritance(self):
        """Check if Astronaut correctly inherits from Human"""
        self.assertTrue(issubclass(Astronaut, Human))
        self.assertEqual(Astronaut.__bases__, (Human,))

    def test_astronaut_method_overriding(self):
        """Ensure __str__ method is correctly tailored for Astronaut"""
        self.assertEqual(Astronaut.__str__.__qualname__, 'Astronaut.__str__')
        """__gt__ should be inherited and not overridden if it behaves as needed"""
        self.assertEqual(Astronaut.__gt__.__qualname__, 'Character.__gt__')

    def test_astronaut_specific_methods(self):
        """Astronaut may have specific methods that should not be in Human"""
        astronaut = Astronaut("Neil", 5, "Earth")
        output = astronaut.__str__()
        expected_output = "Astronaut Neil from Earth with strength 5"
        self.assertEqual(output, expected_output)

        """Ensuring the fight method behavior is as expected from Human"""
        other_human = Human("Buzz", 4, "Earth")
        with self.assertRaises(ValueError):
            astronaut.fight(other_human)


if __name__ == '__main__':
    unittest.main()
