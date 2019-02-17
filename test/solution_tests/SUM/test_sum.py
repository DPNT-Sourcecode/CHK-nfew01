import unittest
from lib.solutions.SUM import sum_solution


class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum_solution.compute(1, 2), 3)
        self.assertEqual(sum_solution.compute(1.03, 2.089), 'inputs must be integers in the range 1-100')
        self.assertEqual(sum_solution.compute(513, 209), 'inputs must be integers in the range 1-100')
        self.assertEqual(sum_solution.compute(-3, -5), 'inputs must be integers in the range 1-100')
