"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Jayden Graneta
ID: 169058740
Email: gran8740@mylaurier.ca
__updated__ = "2024-01-28"
-------------------------------------------------------
"""
# Imports
from functions import stack_maze
from Stack_array import Stack


maze = {'Start': ['A'], 'A': ['B', 'C'], 'B': ['D', 'E'], 'C': [],
        'D': [], 'E': ['F', 'X'], 'F': ['G', 'H'], 'G': [], 'H': []}
path = stack_maze(maze)
print("Path found:", path)
