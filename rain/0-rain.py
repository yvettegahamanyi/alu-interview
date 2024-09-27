#!/usr/bin/python3
"""
Given a list of non-negative integers representing the heights of walls with
unit width 1, as if viewing the cross-section of a relief map, calculate how
many square units of water will be retained after it rains.

Function:
    - rain(walls): returns the total amount of rainwater retained given a list
    of walls

"""

def rain(walls):
    
    """
    Parameters:
        - walls (List[int]): a list of non-negative integers
        to represent the height of the wall
    Example:
        walls = [0, 1, 0, 2, 0, 3, 0, 4]
        print(rain(walls)) = 6

        walls = [2, 0, 0, 4, 0, 0, 1, 0]
        print(rain(walls))= 6

    """
    if not walls:
        return 0

    n = len(walls)
    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = walls[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], walls[i])

    right_max[n - 1] = walls[n - 1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i + 1], walls[i])

    water_retained = 0
    for i in range(n):
        water_retained += min(left_max[i], right_max[i]) - walls[i]

    return water_retained
