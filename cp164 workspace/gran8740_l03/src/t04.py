"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Jayden Graneta
ID: 169058740
Email: gran8740@mylaurier.ca
__updated__ = "2024-01-27"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_array import Priority_Queue
from utilities import priority_queue_test

fh = open('foods.txt', 'r')

print(priority_queue_test(fh))

fh.close()
