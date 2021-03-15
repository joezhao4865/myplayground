import unittest
'''
this method assumes:
    input of only integers. Digital strings or float numbers or any other type of input will be ignored
returns:
    a list of even integers at even index position of the original list
'''

def filterEvenNumberAtEvenPos(*nums):
    return [nums[i] for i in range(len(nums)) if isinstance(nums[i], (int,)) and i % 2==0 and nums[i] % 2 == 0]
        

class EvenNumberEvenIndexMethod(unittest.TestCase):
    def setUp(self):
        self.filterEvenNumbers = filterEvenNumberAtEvenPos

    def test_evenNumatEvenPos(self):
        self.assertEqual(self.filterEvenNumbers(1,2,2,4,2,6,10,8,4,10), [2,2,10,4], 'should be [2,2,10,4]')

    def test_evenNumberEvenPosEmptyResult(self):
        self.assertEqual(self.filterEvenNumbers(1,2,1,2,1,4,1,2,1,10), [], 'should be empty since no even number at even index postion')

    def test_evenNumberEvenPosEmptyWithEmptyInput(self):
        self.assertEqual(self.filterEvenNumbers(), [], 'should be empty since input is empty')

    def test_evenNumberEvenPosInvalidArgs(self):
        self.assertEqual(self.filterEvenNumbers('1', 2, 2, 4, '4'), [2], 'should be [2]')

    def test_evenNumberEvenPosWithNegative(self):
        self.assertEqual(self.filterEvenNumbers(1, 2, -2, -4, 4), [-2, 4], 'should be [-2, 4]')

    def test_evenNumberEvnPosZerosAtEven(self):
        self.assertEqual(self.filterEvenNumbers(0, 1, 0, 1, 0), [0, 0, 0], 'should be [0, 0, 0]')

    def test_evenNumberEvnPosZerosAtOdd(self):
        self.assertEqual(self.filterEvenNumbers(1, 0, 1, 0, 1), [], 'should be []')

    def test_evenNumberEvnPosZeros(self):
        self.assertEqual(self.filterEvenNumbers(0, 0, 0, 0, 0), [0, 0, 0], 'should be [0, 0, 0]')

    def test_evenNumberEvnPosAllOdd(self):
        self.assertEqual(self.filterEvenNumbers(1, -1, 1, 3, -3, -5, 7, 9), [], 'should be []')
        
    def test_evenNumberEvnPosFloatInputs(self):
        self.assertEqual(self.filterEvenNumbers(2.0, 1.5, 2.2, 3.1, 4.2), [], 'should be []')
    
if __name__ == '__main__':
    unittest.main()
