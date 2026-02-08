""""
Jalen Banks
Feb 10, 2026
Lab 5: Functions in Python
"""
import math
# example 1: function that returns a value
def area_rectangle(length, width):
    """Calculate the area of a rectangle."""
    return length * width
# void function that does not return anything
def print_area_result(length, width):
    """Calculate and print the area of a rectangle."""
    area = area_rectangle(length, width)
    print(f"The area of a rectangle with length {length} and width {width} is {area}\n")

# Example 2:calculate the distance between two points
# distance formula: d = sqrt((x2 - x1)^2 + (y2 - y1)^2)
# function 1) collect a number between 1 and 10

def collectnum(point):
    num = int(input(f"Enter a number for {point} (between 1 and 10): "))
    # use a loop to recollect the number if it is not between 1 and 10
    while(num < 1 or num > 10):
        num = int(input("Invalid input!. Enter a number between 1 and 10: "))
    return num
def calculate_distance(x1, y1, x2, y2):
    return math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))

# function to print the result
def print_distance_result(x1, y1, x2, y2, distance):
    print(f"The distance between the points ({x1}, {y1}) and ({x2}, {y2}) is {round(distance)}\n")

# Exercise: Guess a number
import random

def generate_random_number(minimum, maximum):
    """Generate and return a random integer between minimum and maximum."""
    return random.randint(minimum, maximum)

def compare_guess(random_number, guess):
    """Compare the guess number with the random number and print the result."""
    if random_number < guess:
        print("The number is smaller than the guess number")
    elif random_number > guess:
        print("The number is bigger than the guess number")
    else:
        print("You got it!")
