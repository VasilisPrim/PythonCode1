
import math

def circle_area(radius):
    return math.pi*radius**2

def circle_circumference(radius):
    return 2*math.pi*radius

def cylinder_area(height, radius):
    return 2*circle_area(radius) + circle_circumference(radius)*height





