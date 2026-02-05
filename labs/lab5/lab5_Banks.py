"""
Jalen Banks
Feb 10, 2026
Lab 5: Functions in Python
"""
import math
from lab5_functions_Banks import *

print("\n--- Example 1: user defined Functions in Python ---\n")
w = 10
length = 2
a = area_rectangle(length, w)
print(f"The area of a rectangle of {length} length and width {w} is {a}\n")
print_area_result(length, w)

print("\n--- Example 2: calculating the distance between 2 points ---\n")
x1 = collectnum('x1')
x2 = collectnum('x2')
y1 = collectnum('y1')
y2 = collectnum('y2')

#testing
#print(f"({x1}, {y1}) and ({x2}, {y2})")

#testing
#print(f"distance:{calculate_distance(x1, y1, x2, y2)} ")

distance = calculate_distance(x1, x2, y1, y2)
print_distance_result(x1, x2, y1, y2, distance)

print("\n--- EXCERCISE---\n")