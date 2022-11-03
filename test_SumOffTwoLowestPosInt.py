import unittest
import SumOffTwoLowestPosInt

class TestSumOffTwoLowestPosInt(unittest.TestCase):

    def test_sum(self):
        self.assertEquals(SumOffTwoLowestPosInt.sum_two_smallest_numbers([5, 8, 12, 18, 22]), 13)

if __name__ == '__main__':
    unittest.main