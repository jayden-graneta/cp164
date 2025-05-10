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
from Sorts_List_linked import Sorts
from List_linked import List
# Constants

l = List()

l.append(1)
l.append(3)
l.append(2)

Sorts.radix_sort(l)

for val in l:
    print(val)
