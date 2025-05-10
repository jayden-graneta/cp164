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
from utilities import array_to_list
from List_array import List
# Constants

my_list = List()
s = [1, 2, 3, 4, 5]
array_to_list(my_list, s)
print(my_list._values)
my_list.clean()
print(my_list._values)

t = List()
s1 = [1, 2, 3, 4, 5]
s2 = List()
array_to_list(s2, s1)
t.combine(my_list, s2)

print(t._values)
t1, t2 = t.split()
print(t1._values, t2._values)

u = List()
l1 = List()
array_to_list(l1, [1, 2, 3, 4, 5])
u.union(l1, t2)
print(l1._values)
