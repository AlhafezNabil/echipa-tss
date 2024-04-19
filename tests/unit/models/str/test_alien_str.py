import unittest

from models import Alien


class TestAlienStr(unittest.TestCase):
    def test_str_method(self):
        """Create an Alien with advanced technology"""
        alien_with_tech = Alien("Zarvox", 4, True)
        self.assertEqual(str(alien_with_tech), "Zarvox 4 with advanced technology")

        """Create an Alien without advanced technology"""
        alien_without_tech = Alien("Klaatu", 2, False)
        self.assertEqual(str(alien_without_tech), "Klaatu 2 without advanced technology")


if __name__ == '__main__':
    unittest.main()
