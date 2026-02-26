"""
Jalen Banks
lab 9, Unit Testing
Feb 26. 2026
"""

import unittest
from employee import *

class TestEmployee(unittest.TestCase):
    # create a test template (instance for the class) 
    def setUp(self):
        self.employee1 = Employee("Jalen", "Banks", 110000)
    
    #test if email format is working properly 
    def test_emailemployee(self):
        self.assertEqual(self.employee1.emailemployee, "Jalen.Banks@email.com")
    
    # update information and test if email format is working properly after update
        self.employee1.first = "John"
        self.employee1.last = "Smith"
        self.assertEqual(self.employee1.emailemployee, "John.Smith@email.com")
    
    # test the raise
    def test_apply_raise(self):
        self.employee1.apply_raise()
        self.assertEqual(self.employee1.salary, 115500)

    # increase salary
        self.employee1.salary = 120000
        self.employee1.apply_raise()
        self.assertEqual(self.employee1.salary, 126000)

if __name__ == '__main__':
    unittest.main()