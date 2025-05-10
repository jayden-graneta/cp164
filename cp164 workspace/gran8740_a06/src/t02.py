"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Jayden Graneta
ID: 169058740
Email: gran8740@mylaurier.ca
__updated__ = "2024-02-18"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_linked import Priority_Queue
# Constants

pq = Priority_Queue()

for x in range(5):
    pq.insert(x+1)
    print(x)

print('EMPTY:', pq.is_empty())

for x in range(5):
    print(pq.peek())
    pq.remove()
