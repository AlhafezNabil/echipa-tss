import unittest

from models import Astronaut


class TestAstronautStr(unittest.TestCase):
    def test_str_method(self):
        """Create an Astronaut with specific attributes"""
        astronaut = Astronaut("Neil Armstrong", 5, "Moon")

        """Check if __str__ produces the correct format"""
        self.assertEqual(str(astronaut), "Astronaut Neil Armstrong from Moon with strength 5")

