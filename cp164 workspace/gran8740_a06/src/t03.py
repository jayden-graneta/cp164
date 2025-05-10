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
from Deque_linked import Deque
# Constants

d = Deque()

for x in range(5):
    d.insert_front(x)
    print(x)

for x in range(5):
    d.insert_rear(x)

for x in range(5):
    print('removed front', d.peek_front())
    d.remove_front()

for x in range(5):
    print('removed rear', d.peek_rear())
    d.remove_rear()
