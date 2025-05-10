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
from utilities import array_to_stack
from Stack_array import Stack

x = Stack()
s1 = Stack()
s2 = Stack()
array_to_stack(s1, [5, 8, 12, 8])
array_to_stack(s2, [3, 6, 1, 7, 9, 14])
x.combine(s1, s2)

print(x._values)
