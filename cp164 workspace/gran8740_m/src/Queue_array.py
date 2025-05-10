"""
-------------------------------------------------------
Array version of the Queue ADT.
-------------------------------------------------------
Author: Jayden Graneta
ID:     169058740
Email:  gran8740@mylaurier.ca
__updated__ = "2024-06-11"
-------------------------------------------------------
"""
# pylint: disable=E0303
# pylint: disable=E1128
# pylint: disable=E2515
# pylint: disable=W0212
# pylint: disable=W0613

# Imports
from copy import deepcopy

"""
DO NOT CHANGE CODE BELOW THIS LINE
=======================================================================
"""


class Queue:
    """
    -------------------------------------------------------
    Implements an array-based Queue ADT.
    -------------------------------------------------------
    """

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty Queue. Data is stored in a Python list.
        Use: source = Queue()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌‌​‌​​​​‌‌​‌‌​‌​​:
            a new Queue object (Queue)
        -------------------------------------------------------
        """
        self._values = []

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if source is empty.
        Use: b = source.is_empty()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌‌​‌​​​​‌‌​‌‌​‌​​:
            True if source is empty, False otherwise.
        -------------------------------------------------------
        """
        return len(self._values) == 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of source.
        Use: n = len(source)
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌‌​‌​​​​‌‌​‌‌​‌​​:
            the number of values in source (int >= 0)
        -------------------------------------------------------
        """
        return len(self._values)

    def insert(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the rear of source.
        Use: source.insert(value)
        -------------------------------------------------------
        Parameters:
            value - data (*)
        Returns‌​‌​​​​‌​​‌‌‌​‌​​​​‌‌​‌‌​‌​​:
            None
        -------------------------------------------------------
        """
        self._values.append(deepcopy(value))
        return

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns the front value from source.
        Use: value = source.remove()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌‌​‌​​​​‌‌​‌‌​‌​​:
            value - the value at the front of source, the value is
                removed from source (*)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot remove from an empty queue"

        value = self._values.pop(0)
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the front of source.
        Use: value = source.peek()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌‌​‌​​​​‌‌​‌‌​‌​​:
            value - a copy of the value at the front of source,
                the value is not removed from source (*)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot peek at an empty queue"

        value = deepcopy(self._values[0])
        return value

    def __iter__(self):
        """
        FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through source
        from front to rear.
        Use: for value in source:
        -------------------------------------------------------
        Yields:
            value - the next value in source (*)
        -------------------------------------------------------
        """
        for value in self._values:
            yield value
