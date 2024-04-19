import unittest

from models import Character


class TestCharacterStr(unittest.TestCase):
    def test_str_method(self):
        """Create a Character with specific attributes"""
        character = Character("John Doe", 3)

        """Check if __str__ produces the correct format"""
        self.assertEqual(str(character), "John Doe 3")
