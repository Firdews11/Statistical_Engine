import unittest
from src.stat_engine import StatEngine

class TestStatEngine(unittest.TestCase):

    def test_mean(self):
        engine = StatEngine([1, 2, 3])
        self.assertEqual(engine.get_mean(), 2)

    def test_median_even(self):
        engine = StatEngine([1, 2, 3, 4])
        self.assertEqual(engine.get_median(), 2.5)

    def test_median_odd(self):
        engine = StatEngine([1, 2, 3])
        self.assertEqual(engine.get_median(), 2)

    def test_empty(self):
        with self.assertRaises(ValueError):
            StatEngine([])

    def test_std(self):
        engine = StatEngine([2, 4, 6])
        self.assertAlmostEqual(engine.get_standard_deviation(), 2.0)

if __name__ == "__main__":
    unittest.main()
    