#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):

    points = sorted([a, b, c])
    largest = points[2]
    rest = points[:2]

    # if the largest side is >= the sum of the other two,
    # this cannot be a triangle
    if largest >= sum(rest):
        raise TriangleError

    if a == b and a == c:
        return 'equilateral'
    
    if a == c or a == b or b == c:
        return 'isosceles'
    else:
        return 'scalene'


# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
