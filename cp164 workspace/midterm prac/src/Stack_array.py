"""
-------------------------------------------------------
Array version of the Stack ADT.
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2024-02-26"
-------------------------------------------------------
"""
# Imports
from copy import deepcopy


class Stack:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty stack. Data is stored in a Python list.
        Use: stack = Stack()
        -------------------------------------------------------
        Returns:
            a new Stack object (Stack)
        -------------------------------------------------------
        """
        self._values = []

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source stacks into the current target stack. 
        When finished, the contents of source1 and source2 are 
        interlaced into target and source1 and source2 are empty.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based stack (Stack)
            source2 - an array-based stack (Stack)
        Returns:
            None
        -------------------------------------------------------
        """
        while source1._values or source2._values:

            if source1._values:
                self._values.append(source1._values.pop())

            if source2._values:
                self._values.append(source2._values.pop())
        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the stack is empty.
        Use: b = stack.is_empty()
        -------------------------------------------------------
        Returns:
            True if stack is empty, False otherwise
        -------------------------------------------------------
        """
        # Your code here

        return len(self._values) == 0

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the value at the top of the stack.
        Attempting to peek at an empty stack throws an exception.
        Use: value = stack.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the top of stack (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot peek at an empty stack'

        # Your code here

        return deepcopy(self._values[-1])

    def pop(self):
        """
        -------------------------------------------------------
        Pops and returns the top of stack. The value is removed
        from the stack. Attempting to pop from an empty stack
        throws an exception.
        Use: value = stack.pop()
        -------------------------------------------------------
        Returns:
            value - the value at the top of stack (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot pop from an empty stack'

        value = self._values.pop()

        return value

    def push(self, value):
        """
        -------------------------------------------------------
        Pushes a copy of value onto the top of the stack.
        Use: stack.push(value)
        -------------------------------------------------------
        Parameters:
            value - value to be added to stack (?)
        Returns:
            None
        -------------------------------------------------------
        """
        self._values.append(deepcopy(value))

        return

    def reverse(self):
        """
        -------------------------------------------------------
        Reverses the contents of the source stack.
        Use: stack.reverse()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        items = []
        while not self.is_empty():
            items.append(self.pop())
        for item in items:
            self.push(item)

        return

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source stack into separate target stacks with values 
        alternating into the targets. At finish source stack is empty.
        (iterative algorithm)
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (Stack)
            target2 - contains other alternating values from source (Stack)
        -------------------------------------------------------
        """
        target1 = Stack()
        target2 = Stack()
        left = True
        if len(self._values) > 0:
            while len(self._values) > 0:
                if left:
                    target1._values.append(self._values.pop())
                else:
                    target2._values.append(self._values.pop())
                left = not left
        return target1, target2

    def __iter__(self):
        """
        FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the stack
        from top to bottom.
        Use: for value in stack:
        -------------------------------------------------------
        Returns:
            value - the next value in the stack (?)
        -------------------------------------------------------
        """
        for value in self._values[::-1]:
            yield value
