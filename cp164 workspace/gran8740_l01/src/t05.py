"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Jayden Graneta
ID: 169058740
Email: gran8740@mylaurier.ca
__updated__ = "2024-01-13"
-------------------------------------------------------
"""
# Imports
from Food_utilities import read_foods

# Constants
fh = open('foods.txt', 'r')
foods = read_foods(fh)
print(foods)
fh.close()
