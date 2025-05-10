"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Jayden Graneta
ID: 169058740
Email: gran8740@mylaurier.ca
__updated__ = "2024-03-09"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST
from morse import fill_code_bst, DATA2
# Constants

bst = BST()
fill_code_bst(bst, DATA2)
for value in bst.inorder():
    print(value)
