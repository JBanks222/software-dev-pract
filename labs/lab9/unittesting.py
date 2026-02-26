"""
Jalen Banks
lab 9, Unit Testing
Feb 26. 2026
"""

import unittest

from calculations import *


# EXAMPLE 1: simple unit testing function

def addtwonumbers(a,b):
    return a + b

#unit testing
class TestAddFunction(unittest.TestCase):
    def test_addtwonumbers(self):
        self.assertEqual(addtwonumbers(1,2), 3) # test that when passing 1 and 2, the result is 3

     #EXAMPLE 2: unit testing calculations.py file
    def test_subtracttwonumbers(self):
        self.assertEqual(subtracttwonumbers(6,4), 2) # test that when passing 6 and 4, the result is 2
        self.assertEqual(subtracttwonumbers(4,6), -2) # test that when passing 4 and 6, the result is -2
        self.assertEqual(subtracttwonumbers(5), 5) # test that when passing 5 , the result is 5
        self.assertEqual(subtracttwonumbers(), 0) # test that when passing no arguments, the result is 0

        # unit test for multiplication function
        def test_multiplytwonumbers(self):
            self.assertEqual(multiplytwonumbers(1,2,3), 6) # test that when passing 1, 2 and 3, the result is 6
            self.assertEqual(multiplytwonumbers(1,-2,3), -6) # test that when passing 1, -2 and 3, the result is -6
            self.assertEqual(multiplytwonumbers(1,-2,3), 6) # test that when passing 1, -2 and 3, the result is 6
            self.assertEqual(multiplytwonumbers(-1,-2,-3), -6) # test that when passing -1, -2 and -3, the result is -6

        # unit test for division function
        def test_division(self):
            self.assertEqual(dividetwonumbers(6,3), 2) # test that when passing 6 and 3, the result is 2
            self.assertAlmostEqual(dividetwonumbers(10,3), 3.3333, places=4) # test that when passing 10 and 3, the result is 3.3333333333333335 unless we round it to 4 decimal places, then the result is 3.3333
        # unit test for division function with division by zero
        def test_division_by_zero(self):
            # assertion none or some known return value
            self.assertIsNone(dividetwonumbers(10,0)) # test that when passing 10 and 0, the result is None
        
        # unit test for value error
            self.assertIsNone(dividetwonumbers(10,"a")) # test that when passing 10 and "a", the result is None
            self.assertIsNone(dividetwonumbers("Peter",2))

        #unit for any other possible errors by mocking
        def test_unexpected_exception(self):
            with self.assertRaises(Exception): # passing none to trigger an exception
                dividetwonumbers() #is basically none, none
                
    




#unit test for subtraction function
if __name__ == '__main__':    
    unittest.main()