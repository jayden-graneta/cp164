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

q1 = Queue()
q2 = Queue()
q2.insert(1)
q1.insert(10)

equals = q1 == q2

print(equals)
