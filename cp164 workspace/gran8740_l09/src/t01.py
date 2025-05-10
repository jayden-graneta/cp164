"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Jayden Graneta
ID: 169058740
Email: gran8740@mylaurier.ca
__updated__ = "2024-03-15"
-------------------------------------------------------
"""
# Imports
from functions import hash_table
from Hash_Set_array import Hash_Set
from Food_utilities import read_foods
# Constants

fh = "foods.txt"
file = open(fh, "r", encoding="utf-8")
content = read_foods(file)
hash_table(10, content)
