#!/usr/bin/python3

import math

def combination(n, r):
    """function to calculate binomial coefficient"""
    return int((math.factorial(n)) / ((math.factorial(r)) * math.factorial(n - r)))


def pascal_triangle(n):
    """ Function returns a list of lists of integers
    representing the Pascal’s triangle of n"""
    result = []
    for count in range(n):
        row = []
        for element in range(count + 1):
            row.append(combination(count, element))
        result.append(row)
    return result
