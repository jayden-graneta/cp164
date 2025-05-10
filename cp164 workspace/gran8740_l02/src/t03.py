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
from Stack_array import Stack
from utilities import stack_to_array
from utilities import array_to_stack
# Constants

stack = Stack()
x = [1, 2, 3, 4, 5]
y = []

array_to_stack(stack, x)
stack_to_array(stack, y)

print(y)
