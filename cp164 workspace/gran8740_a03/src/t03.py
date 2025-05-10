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
from functions import stack_reverse
from utilities import array_to_stack
from Stack_array import Stack

s1 = Stack()
array_to_stack(s1, [3, 6, 1, 7, 9, 14])
print(s1._values)
stack_reverse(s1)

print(s1._values)
