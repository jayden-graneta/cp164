"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Jayden Graneta
ID: 169058740
Email: gran8740@mylaurier.ca
__updated__ = "2024-02-26"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
# Constants

x = Stack()

x.push(44)
x.push(55)
x.push(11)
x.push(33)
x.push(22)
print(x._values)

x.reverse()
print(x._values)

'''
for i in x:
    print(x.peek())
    x.pop
    print(x._values)
'''
