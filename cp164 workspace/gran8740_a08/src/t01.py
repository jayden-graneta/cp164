"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Jayden Graneta
ID: 169058740
Email: gran8740@mylaurier.ca
__updated__ = "2024-03-16"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST
# Constants

val = BST()
x = 1

for x in range(5):
    val.insert(x)
    x += 10
    print(val.levelorder())

print(val.levelorder())

for x in range(5):
    val.remove(x)
    print(val.levelorder())
