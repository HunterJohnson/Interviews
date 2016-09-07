""" 

problem 15 

Starting in the top left corner of a  grid and
moving only down and right, there are 6 routes to the bottom right corner.

How many routes are there through a 20x20 grid?
"""

def route_num(cube_size):
    L = [1] * cube_size
    for i in range(cube_size):
        for j in range(i):
            L[j] = L[j]+L[j-1]
        L[i] = 2 * L[i - 1]
    return L[cube_size - 1]