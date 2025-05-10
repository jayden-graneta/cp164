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
from utilities import array_to_stack
# Constants

stack = Stack()
x = [11, 22, 33, 44]

array_to_stack(stack, x)

for x in range(5):
    print(stack.peek())
    stack.pop()
