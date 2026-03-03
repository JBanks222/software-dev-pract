"""
Jalen Banks
March 3, 2026
Lab 10 , unit testing using pytest
"""
import pytest


import pytest


def add(a,b):
    """Returns the sum of a and b."""
    return a + b

def subtract(a,b):
    return a-b

# testing
"""
print(add(2,3)) # 5
print(add(-8,5)) # -3
print(subtract(7,5)) # 2
print(subtract(-7,5)) # -12
print(subtract(-7,-5)) # -2
"""
# lab excercise 1: basic testing

def divide(a,b):
    if (b==0):
        raise ValueError("Can't divide by zero")
    return a / b

#local testing
# print(divide(6,2)) # 3.0
# print(divide(3,0)) # ValueError: Can't divide by zero

# lab excercise 2: password validation: 8+ characters, at least 1 number and can't contanin special characters like %,$, or space
def validate_password(password):
    password.strip() # remove leading and trailing whitespace
    special_character = '%' in password or '$' in password or ' ' in password
    if len(password)<8 or special_character:
        return False
    return True

# local testing
print(validate_password("peterpan")) 
print(validate_password("peter pan"))
print(validate_password("peterpan1"))
print(validate_password("peter%pan"))
print(validate_password("peter$pan"))
print(validate_password("peterpan "))   

# lab excercise 3: test if a number is even

def is_even(n):
    return n % 2 == 0 and n != 0

# local testing
print(is_even(8)) # True
print(is_even(-5)) # False
print(is_even(0)) # False
print(is_even(-12)) # True
print(is_even(11)) # False

