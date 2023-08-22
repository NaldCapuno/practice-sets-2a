'''
Calculate the area of a triangle using Heron's formula

Args:
    a, b, c - length of the sides a, b, and c

Return:
    Calculated are of triangle
'''

def triangle_area(a: float, b: float, c: float) -> float:
    # calculate semi-perimeter
    s = (a + b + c) / 2

    # calculate area
    area = (s * (s - a) * (s - b) * (s - c)) ** 1/2

    return area
