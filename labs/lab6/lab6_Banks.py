"""
Jalen Banks
Feb 10 
classes and objects and methods
"""
import matplotlib.pyplot as plt

print("\n-----Example 1: classes-----\n")
# a class is like a blueprint of something
# using the class, we can create a different instance of an object
# data attributes (properies) are values that represent the state of an object
# methods are functions of an object

class Circle(object):
    def __init__(self, radius, color):
        self.r = radius
        self.c = color 

    # method to add value to the radius
    def add_radius(self, plusradius):
        self.r += plusradius
        return self.r

class Rectangle(object):
    def __init__(self, width, height, color):
        self.w = width
        self.h = height
        self.c = color
    # method to calculate and return the area of the rectangle
    def area(self):
        return self.w * self.h
    # method to calculate the perimeter of the rectangle
    def perimeter(self):
        return 2 * (self.w + self.h)
    # method to draw the rectangle using matplotlib
    def draw_rectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.w, self.h, color=self.c))
        plt.axis('scaled') # this keeps the aspect ratio equal
        plt.show()

# create an instance of a object
circle1 = Circle(5, "red")
circle2 = Circle(2, "blue")
rectangle1 = Rectangle(5, 4, "green") 
rectangle2 = Rectangle(3, 7, "yellow")

#accessing the data in an object
print(f"color of circle2 is {circle2.c}")
print(f"area of rectangle1 is {rectangle1.w * rectangle1.h}")

# modify data in an object
circle2.c = "orange"
print(f"color of circle2 after modification is {circle2.c}")

print(f"radius of circle2 is {circle2.r}")

# call method add_radius in circle2 and pass 6
circle2.add_radius(6)
print(f"radius of circle2 after adding 6 is {circle2.r}")

# call methods in class rectangle
print(f"area of rectangle 1 = {rectangle1.area()}")
print(f"the area of rectangle 2 = {rectangle2.area()}") 

#draw rectangle2
rectangle1.draw_rectangle()

print("\n-----EXCERCISE: Bank Account Class-----\n")