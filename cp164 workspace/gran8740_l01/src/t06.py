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
from Food_utilities import write_foods, read_foods
# Constants
fh = open("new_foods.txt", "w")
write_foods(fh, foods)
fh.close()
