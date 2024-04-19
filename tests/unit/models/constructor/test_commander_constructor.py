import unittest

from models import Commander, Astronaut


class TestCommanderConstructor(unittest.TestCase):
    def test_strength_clamping(self):
        """Test that strength is clamped to the maximum value of 5"""
        commander_high = Commander("HighCmdr", 10, "Venus")
        self.assertEqual(commander_high.strength, 5)

        """Test that strength is clamped to the minimum value of 0"""
        commander_low = Commander("LowCmdr", -3, "Mars")
        self.assertEqual(commander_low.strength, 0)

    def test_strength_initial_values(self):
        """Test normal strength initialization within the allowed range"""
        commander_normal = Commander("CmdrNormal", 4, "Earth")
        self.assertEqual(commander_normal.strength, 4)

    def test_planet_initialization(self):
        """Ensure the planet is correctly initialized"""
        commander = Commander("CmdrPlanet", 3, "Jupiter")
        self.assertEqual(commander.planet, "Jupiter")

    def test_invalid_planet_type(self):
        """Ensure setting an incorrect type for planet raises an error"""
        with self.assertRaises(TypeError):
            commander_wrong_planet = Commander("CmdrWrong", 3, 123)

    def test_crew_initial_empty(self):
        """Test that the crew list is initially empty"""
        commander = Commander("CmdrCrew", 2, "Saturn")
        self.assertEqual(len(commander.crew), 0)

    def test_crew_type_safety(self):
        """Test adding non-Astronauts to the crew raises an error"""
        commander = Commander("CmdrCrew", 3, "Neptune")
        with self.assertRaises(ValueError):
            commander.crew = ["not an astronaut"]

    def test_crew_planet_consistency(self):
        """Test that only astronauts from the same planet can be added"""
        commander = Commander("CmdrPlanet", 4, "Mars")
        astronaut_mars = Astronaut("AstroMars", 3, "Mars")
        astronaut_venus = Astronaut("AstroVenus", 2, "Venus")
        commander.add_crew_member(astronaut_mars)
        with self.assertRaises(ValueError):
            commander.add_crew_member(astronaut_venus)


if __name__ == '__main__':
    unittest.main()
