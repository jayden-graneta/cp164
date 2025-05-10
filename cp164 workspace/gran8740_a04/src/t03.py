"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Jayden Graneta
ID: 169058740
Email: gran8740@mylaurier.ca
__updated__ = "2024-02-04"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue
from functions import queue_split_alt
# Constants

q = Queue()

for x in range(10):
    q.insert(x)

print(q._values)
target1, target2 = queue_split_alt(q)


print(target1._values, target2._values)
