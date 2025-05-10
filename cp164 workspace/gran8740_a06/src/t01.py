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
from Queue_linked import Queue
# Constants

queue = Queue()

for x in range(5):
    queue.insert(x+1)
    print(x+1)

print('empty:', queue.is_empty())
print('Front value:', queue._front._value)
print('Rear Value:', queue._rear._value)
