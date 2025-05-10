"""
-------------------------------------------------------
Array version of the List ADT.
-------------------------------------------------------
Author: Jayden Graneta
ID:     169058740
Email:  gran8740@mylaurier.ca
__updated__ = "2024-06-12"
-------------------------------------------------------
"""
# pylint: disable=E0303
# pylint: disable=E1128
# pylint: disable=E2515
# pylint: disable=W0212
# pylint: disable=W0613

# Imports
from copy import deepcopy


class List:
    """
    Implements an array-based List ADT.
    """

    def rotate_right(self, n):
        """
        -------------------------------------------------------
        Rotates position of elements in self. When finished elements
        in self are rotated n positions to the right.
        n may be positive, negative, or 0
        Use: source.rotate_right(n)
        -------------------------------------------------------
        Parameters:
            n - amount to rotate List elements to the right (int)
        Returns‌​‌​​​​‌​​‌‌‌​‌​​​​‌‌​‌‌​‌​​:
            None
        -------------------------------------------------------
        """

        # your code here
        for x in range(0, n):
            rear = self._values[len(self._values) - 1]
        for i in range(len(self._values), -1, -1, -1):
            self._values[i] = self._values[i - 1]
            self._values[0] = rear

        return

    def adjacents_count(self):
        """
        -------------------------------------------------------
        Returns the count of the largest number of adjacent values in source.
        Use: count = source.adjacents_count(n)
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌‌​‌​​​​‌‌​‌‌​‌​​:
            count - the count of the largest number of adjacent values
                in source (int >= 0)
        -------------------------------------------------------
        """

        # your code here
        count = 0
        num = 0
        temp = 0
        x = 0

        while len(self._values) != 0:
            num = self._values[x]
            for i in range(len(self._values)):
                if num == self._values[i]:
                    temp += 1
            if temp > count:
                count = temp
            x += 1

        return count

    """
    DO NOT CHANGE CODE BELOW THIS LINE
    =======================================================================
    """

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty list.
        Use: source = List()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌‌​‌​​​​‌‌​‌‌​‌​​:
            a new List object (List)
        -------------------------------------------------------
        """
        self._values = []

    def append(self, value):
        """
        ---------------------------------------------------------
        Adds a copy of value to the end of source.
        Use: source.append(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (*)
        Returns‌​‌​​​​‌​​‌‌‌​‌​​​​‌‌​‌‌​‌​​:
            None
        -------------------------------------------------------
        """
        self._values = self._values + [deepcopy(value)]
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through source
        from front to rear.
        Use: for v in source:
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌‌​‌​​​​‌‌​‌‌​‌​​:
            value - the next value in source (*)
        -------------------------------------------------------
        """
        for value in self._values:
            yield value
