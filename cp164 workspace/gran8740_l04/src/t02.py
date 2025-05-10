"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Jayden Graneta
ID: 169058740
Email: gran8740@mylaurier.ca
__updated__ = "2024-02-03"
-------------------------------------------------------
"""
# Imports
from List_array import List
from utilities import array_to_list
from utilities import list_to_array

x = List()
y = [2, 4, 6, 8, 10]
array_to_list(x, y)
print(x._values, y)

target = []
list_to_array(x, target)
print(x._values, target)
