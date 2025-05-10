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
from utilities import pq_to_array
from utilities import array_to_pq

# Constants

target = []
q = Priority_Queue()
my_list = [10, 3, 4, 5]

array_to_pq(q, my_list)
print(q._values)

pq_to_array(q, target)
print(target)
