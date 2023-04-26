import unittest
from src.main import sqrt
from src.main import sort_list_asc

class TestSqrt(unittest.TestCase):
    def test_calc_correct_perfect_square(self):
        res = sqrt(9)
        self.assertEqual(res, 3)
        
    def test_negative(self):
        with self.assertRaises(Exception) as context:
            sqrt(-9)
        self.assertTrue('can not calc sqrt of negative number' in str(context.exception))

    def test_non_int(self):
        with self.assertRaises(Exception) as context:
            sqrt(9.0)
        self.assertTrue('input to sqrt is not integer' in str(context.exception))
        
    def test_calc_correct_non_perfect_square(self):
        res = sqrt(5)
        self.assertEqual(res, 2.25)

class TestReverseList(unittest.TestCase):
    def test_sort_correct(self):
        res = sort_list_asc([1,2,3])
        self.assertEqual(res, [3,2,1])

    def test_non_list_input(self):
        with self.assertRaises(Exception) as context:
            sort_list_asc(3)
        self.assertTrue('input to reverse_list is not a list' in str(context.exception))

    def test_list_with_single_element(self):
        res = sort_list_asc([3])
        self.assertEqual(res, [3])

if __name__== '__main__':
    unittest.main()