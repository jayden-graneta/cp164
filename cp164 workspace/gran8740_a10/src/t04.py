"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Jayden Graneta
ID: 169058740
Email: gran8740@mylaurier.ca
__updated__ = "2024-03-30"
-------------------------------------------------------
"""
# Imports
from Sorts_Deque_linked import Sorts
from Deque_linked import Deque
# Constants

x = Deque()
x.insert_rear(1)
x.insert_rear(3)
x.insert_rear(2)


Sorts.gnome_sort(x)
for val in x:
    print(val)
