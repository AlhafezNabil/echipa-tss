import unittest

from models import Astronaut, Commander


class TestCommanderProperties(unittest.TestCase):
    def setUp(self):
        self.commander = Commander("Cmdr. Shepard", 5, "Earth")
        self.astronaut1 = Astronaut("Buzz", 4, "Earth")
        self.astronaut2 = Astronaut("Neil", 3, "Mars")

    def test_initial_crew_empty(self):
        """Test that the crew list is initially empty"""
        self.assertEqual(len(self.commander.crew), 0)

    def test_add_crew_member_valid(self):
        """Test adding a valid crew member"""
        self.commander.add_crew_member(self.astronaut1)
        self.assertIn(self.astronaut1, self.commander.crew)

    def test_add_crew_member_invalid_planet(self):
        """Test adding an astronaut from a different planet"""
        with self.assertRaises(ValueError):
            self.commander.add_crew_member(self.astronaut2)

    def test_crew_property_setter_invalid_type(self):
        """Test setting crew list with an invalid type"""
        with self.assertRaises(ValueError):
            self.commander.crew = [self.astronaut1, "not an astronaut"]

    def test_crew_property_setter_valid(self):
        """Test setting the crew list with valid astronauts from the same planet"""
        self.commander.crew = [self.astronaut1]
        self.assertEqual(len(self.commander.crew), 1)
        self.assertIn(self.astronaut1, self.commander.crew)
