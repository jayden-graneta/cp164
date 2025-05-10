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
from Queue_array import Queue
from utilities import array_to_queue
from utilities import queue_to_array
from utilities import queue_test
# Constants


q = Queue()
target = []
my_list = [1, 2, 3, 4, 5]

array_to_queue(q, my_list)
print(q._values)
queue_to_array(q, target)
print(target)

print(queue_test(q))
