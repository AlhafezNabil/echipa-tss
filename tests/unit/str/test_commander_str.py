import unittest

from models import Astronaut, Commander


class TestCommanderStr(unittest.TestCase):
    def test_str_method(self):
        """Create a Commander with specific attributes"""
        commander = Commander("Jane Shepard", 5, "Earth")

        crew_member1 = Astronaut("Garrus", 4, "Earth")
        crew_member2 = Astronaut("Tali", 3, "Earth")
        commander.add_crew_member(crew_member1)
        commander.add_crew_member(crew_member2)

        """Check if __str__ produces the correct format"""
        expected_output = "Commander Jane Shepard from Earth with strength 5 and with crew [Garrus, Tali]"
        self.assertEqual(str(commander), expected_output)
