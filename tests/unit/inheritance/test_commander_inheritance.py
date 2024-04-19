import unittest

from models import Commander, Astronaut, Human
import unittest


class TestCommanderInheritance(unittest.TestCase):
    def test_commander_inheritance(self):
        """Check if Commander correctly inherits from Human"""
        self.assertTrue(issubclass(Commander, Human))
        self.assertEqual(Commander.__bases__, (Human,))

    def test_commander_method_overriding(self):
        """Ensure __str__ method is specifically tailored for Commander"""
        self.assertEqual(Commander.__str__.__qualname__, 'Commander.__str__')
        """__gt__ should be inherited and not overridden"""
        self.assertEqual(Commander.__gt__.__qualname__, 'Character.__gt__')

    def test_commander_specific_methods(self):
        """Check specific behaviors that should only exist in Commander"""
        commander = Commander("Picard", 4, "Earth")
        self.assertIn("crew", dir(commander))  # Ensure 'crew' attribute exists
        """Check addition of crew members"""
        astronaut = Human("Riker", 3, "Earth")  # This should raise a ValueError
        with self.assertRaises(ValueError):
            commander.add_crew_member(astronaut)

        output = commander.__str__()
        expected_output = "Commander Picard from Earth with strength 4 and with crew []"
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()
