"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Jayden Graneta
ID: 169058740
Email: gran8740@mylaurier.ca
__updated__ = "2024-02-11"
-------------------------------------------------------
"""
# Imports
from Sorted_List_array import Sorted_List
# Constants

sort_list = Sorted_List()

sort_list.insert(1)
sort_list.insert(2)
sort_list.insert(3)
sort_list.insert(4)
sort_list.insert(5)
print(sort_list._values)
print(sort_list.index(1))
print(sort_list.find(1))
s1 = Sorted_List()
s2 = Sorted_List()
s1.insert(1)
s1.insert(2)
s1.insert(3)
s1.insert(4)
s1.insert(5)
s1.clean()
s2.intersection(sort_list, s1)
print(s1._values)
print(s2._values)
