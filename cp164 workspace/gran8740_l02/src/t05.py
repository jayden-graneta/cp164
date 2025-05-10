"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Jayden Graneta
ID: 169058740
Email: gran8740@mylaurier.ca
__updated__ = "2024-01-19"
-------------------------------------------------------
"""
# Imports
from utilities import stack_test
from Food_utilities import read_foods
# Constants


fh = open('food.txt', 'r')
foods = read_foods(fh)
stack = stack_test(foods)

fh.close()
