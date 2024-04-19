import unittest

from models import Alien


class TestAlienGreaterOperator(unittest.TestCase):
    def test_greater_operator(self):
        # Create Aliens with varying strengths and technology statuses
        alien1 = Alien("Zygon", 4, True)
        alien2 = Alien("Xilox", 5, True)
        alien3 = Alien("Nargon", 4, False)

        # Test where technology makes a difference
        self.assertTrue(alien1 > alien3, "Zygon with tech should be stronger than Nargon without tech")

        # Test where technology does not make a difference
        self.assertFalse(alien3 > alien1, "Nargon without tech should not be stronger than Zygon with tech")

        # Test where strength and technology are the same
        self.assertFalse(alien1 > alien2, "Zygon should not be stronger than Xilox with the same tech level")
        self.assertTrue(alien2 > alien1, "Xilox should be stronger than Zygon since he has more strength")


if __name__ == '__main__':
    unittest.main()
