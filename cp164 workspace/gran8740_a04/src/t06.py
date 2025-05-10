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
from Priority_Queue_array import Priority_Queue
# Constants

q = Priority_Queue()

for x in range(10):
    q.insert(x)

print(q._values)
t1, t2 = q.split_key(5)
print(t1._values, t2._values)
