"""
Jalen Banks
March 3, 2026
Lab 10 , unit testing using pytest
"""

import pytest

from calculator import *

def test_add():
    assert add(2,3) == 5
    assert add(-8,5) == -3

def test_subtract():
    assert subtract(-7,-5) == -2 

# lab excercise 1
def test_divide():
    assert divide(10,2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(3,0)
  
# lab excercise 3
# parametrized tests allow us to run the same test function with different sets of input data. This is useful for testing a function with multiple inputs without having to write separate test functions for each case. We can use the @pytest.mark.parametrize decorator to achieve this.
@pytest.mark.parametrize("n, expected"
                         , [
                             (8, True),
                             (-5, False),
                             (0, False),
                             (-12, True),
                             (11, False)
                         ])
def test_is_even(n, expected):
    assert is_even(n) == expected

# lab excercise 4 - password validation
@pytest.mark.parametrize(
    "password, expected",
    [
        ("peterpan", True),
        ("peter", False),
        ("peter pan", False),
    ],
)
def test_validate_password(password, expected):
    assert validate_password(password) is expected

