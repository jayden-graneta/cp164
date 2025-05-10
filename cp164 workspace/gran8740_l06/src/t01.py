"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Jayden Graneta
ID: 169058740
Email: gran8740@mylaurier.ca
__updated__ = "2024-02-17"
-------------------------------------------------------
"""
# Imports
from List_linked import List
# Constants

list1 = List()
list1.prepend(1)
list1.append(2)
list1.insert(2, 3)
list1.append(4)

for value in list1:
    print(value)

print(list1.count(4))
print(list1.max())
print(list1.min())
print(list1.find(3))

for x in list1:
    print('removed:', x)
    list1.remove(x)
