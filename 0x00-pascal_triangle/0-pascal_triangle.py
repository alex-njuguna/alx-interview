#!/usr/bin/python3
"""
pascal's triangle
"""


def pascal_triangle(n):
    """
    create a pascal triangle size of n
    """
    triangle = []
    if n > 0:
        for i in range(1, n + 1):
            level = []
            C = 1
            for j in range(1, i + 1):
                level.append(C)
                C = C * (i - j) // j
            triangle.append(level)
    return triangle
