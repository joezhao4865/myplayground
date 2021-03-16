import unittest
'''
this method assumes:
    input of only integer array. Digital strings or float numbers or any other type of input will be ignored
returns:
    a list of even integers at even index position of the original list
'''

def filter_even_number_at_even_idx(nums=[]):
    return [nums[i] for i in range(len(nums)) if isinstance(nums[i], (int,)) and i % 2==0 and nums[i] % 2 == 0]
        

class EvenNumberEvenIndexMethod(unittest.TestCase):
    def setUp(self):
        self.filter_even_numbers = filter_even_number_at_even_idx

    def test_even_num_at_even_idx(self):
        self.assertEqual(self.filter_even_numbers([1,2,2,4,2,6,10,8,4,10]), [2,2,10,4], 'should be [2,2,10,4]')

    def test_even_num_at_even_idx_empty_result(self):
        self.assertEqual(self.filter_even_numbers([1,2,1,2,1,4,1,2,1,10]), [], 'should be empty since no even number at even index postion')

    def test_even_num_at_even_idx_empty_with_empty_input(self):
        self.assertEqual(self.filter_even_numbers([]), [], 'should be empty since input is empty')

    def test_even_num_at_even_idx_invalid_args(self):
        self.assertEqual(self.filter_even_numbers(['1', 2, 2, 4, '4']), [2], 'should be [2]')

    def test_even_num_at_even_idx_with_negative(self):
        self.assertEqual(self.filter_even_numbers([1, 2, -2, -4, 4]), [-2, 4], 'should be [-2, 4]')

    def test_even_num_at_even_idx_zeros_at_even(self):
        self.assertEqual(self.filter_even_numbers([0, 1, 0, 1, 0]), [0, 0, 0], 'should be [0, 0, 0]')

    def test_even_num_at_even_idx_zeros_at_odd(self):
        self.assertEqual(self.filter_even_numbers([1, 0, 1, 0, 1]), [], 'should be []')

    def test_even_num_at_even_idx_zeros(self):
        self.assertEqual(self.filter_even_numbers([0, 0, 0, 0, 0]), [0, 0, 0], 'should be [0, 0, 0]')

    def test_even_num_at_even_idx_all_odd(self):
        self.assertEqual(self.filter_even_numbers([1, -1, 1, 3, -3, -5, 7, 9]), [], 'should be []')
        
    def test_even_num_at_even_idx_float_inputs(self):
        self.assertEqual(self.filter_even_numbers([2.0, 1.5, 2.2, 3.1, 4.2]), [], 'should be []')
    
if __name__ == '__main__':
    unittest.main()
