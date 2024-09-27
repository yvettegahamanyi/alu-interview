#!/usr/bin/python3
"""
Given a list of non-negative integers representing the heights of walls with
unit width 1, as if viewing the cross-section of a relief map, calculate how
many square units of water will be retained after it rains.

Function:
    - rain(walls): returns the total amount of rainwater retained given a list
    of walls.
"""


def rain(walls):
    """
    Parameters:
        - walls (List[int]): a list of non-negative integers
          to represent the height of the walls.
    
    Returns:
        - int: The total amount of water retained.
    
    Example:
        walls = [0, 1, 0, 2, 0, 3, 0, 4]
        print(rain(walls))  # Output: 6

        walls = [2, 0, 0, 4, 0, 0, 1, 0]
        print(rain(walls))  # Output: 6
    """
    if not walls:
        return 0
    
    n = len(walls)
    
    # Arrays to store the maximum height to the left and right of each wall
    left_max = [0] * n
    right_max = [0] * n
    
    # Fill left_max array
    left_max[0] = walls[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], walls[i])
    
    # Fill right_max array
    right_max[-1] = walls[-1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], walls[i])
    
    # Calculate trapped water
    total_water = 0
    for i in range(n):
        water_at_wall = min(left_max[i], right_max[i]) - walls[i]
        if water_at_wall > 0:
            total_water += water_at_wall
    
    return total_water
