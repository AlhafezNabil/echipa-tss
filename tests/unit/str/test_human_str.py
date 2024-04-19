import unittest

from models import Human

import unittest


class TestHumanStr(unittest.TestCase):
    def test_str_method(self):
        """Create a Human object with specific attributes"""
        human = Human("John Doe", 4, "Earth")

        """Check if __str__ produces the correct format"""
        self.assertEqual(str(human), "John Doe from Earth with strength 4")


if __name__ == '__main__':
    unittest.main()
