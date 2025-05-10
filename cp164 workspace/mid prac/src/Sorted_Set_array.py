"""
-------------------------------------------------------
Array version of the Sorted_Set ADT.
-------------------------------------------------------
Author: Jayden Graneta
ID:     169058740
Email:  gran8740@mylaurier.ca
__updated__ = "2024-02-28"
-------------------------------------------------------
"""
# pylint: disable=protected-access

# Imports
from copy import deepcopy


class Sorted_Set:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty Sorted_Set.
        Use: source = Sorted_Set()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌‌​‌​​​​‌‌​‌‌​‌​​:
            Creates a new Sorted_Set object. (Sorted_Set)
        -------------------------------------------------------
        """
        self._values = []

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if source is empty.
        Use: empty = source.is_empty()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌‌​‌​​​​‌‌​‌‌​‌​​:
            True if source is empty, False otherwise. (boolean)
        -------------------------------------------------------
        """
        return len(self._values) == 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in source.
        Use: n = len(source)
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌‌​‌​​​​‌‌​‌‌​‌​​:
            the number of values in source. (int)
        -------------------------------------------------------
        """
        # your code here
        return len(self._values)

    def _binary_search(self, key):
        """
        -------------------------------------------------------
        Searches for the occurrence of key in self.
        Private helper method.
        Use: i = self._binary_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data value (*)
        Returns‌​‌​​​​‌​​‌‌‌​‌​​​​‌‌​‌‌​‌​​:
            i - the index of the only occurrence of key in
                self, -1 if key is not found. (int)
        -------------------------------------------------------
        """
        low = 0
        high = len(self._values) - 1

        while low < high:
            mid = (high - low) // 2 + low

            if key > self._values[mid]:
                low = mid + 1
            else:
                high = mid

        if low == high and self._values[low] == key:
            i = low
        else:
            i = -1
        return i

    def add(self, value):
        """
        -------------------------------------------------------
        If value does not already exist in source, adds a copy of value
        to source. Returns True if value is added, False otherwise.
        Values in source must remain sorted.
        Use: added = source.add(value)
        -------------------------------------------------------
        Parameters:
            value - data (*)
        Returns‌​‌​​​​‌​​‌‌‌​‌​​​​‌‌​‌‌​‌​​:
            added - True if value added to source, False otherwise. (boolean)
        -------------------------------------------------------
        """
        added = True
        # Index of beginning of subarray to search.
        low = 0
        # Index of end of subarray to search.
        high = len(self._values) - 1

        while low <= high and added:
            # Find the middle of the current subarray.
            # (avoids overflow on large values vs (low + high)//2
            mid = (high - low) // 2 + low

            if self._values[mid] == value:
                # value already in set
                added = False
            elif self._values[mid] > value:
                # search the left subarray.
                high = mid - 1
            else:
                # Default: search the right subarray.
                low = mid + 1

        if added:
            self._values.insert(low, deepcopy(value))
        return added

    def discard(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in source that matches key.
        Returns None if key not in source.
        Use: value = source.discard(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data value (*)
        Returns‌​‌​​​​‌​​‌‌‌​‌​​​​‌‌​‌‌​‌​​:
            value - the full value matching key, None otherwise. (*)
        -------------------------------------------------------
        """
        # your code here
        value = None
        x = 0
        end = len(self._values) - 1
        while x <= end:
            middle = (x + end) // 2
            if self._values[middle] == key:
                value = self._values.pop(middle)
                self._values.pop(middle)
            elif key < self._values[middle]:
                end = middle - 1
            else:
                x = middle + 1
        return value

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Returns True if source contains key, False otherwise.
        Use: contains = key in source
        -------------------------------------------------------
        Parameters:
            key - a partial data value (*)
        Returns‌​‌​​​​‌​​‌‌‌​‌​​​​‌‌​‌‌​‌​​:
            True if source contains key, False otherwise. (boolean)
        -------------------------------------------------------
        """
        # your code here
        x = False
        i = 0
        while i < len(self._values) and not x:
            if self._values[i] == key:
                x = True

            i += 1

        return x

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of value in source that matches key.
        Use: value = source.find(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data value (*)
        Returns‌​‌​​​​‌​​‌‌‌​‌​​​​‌‌​‌‌​‌​​:
            value - a copy of the full value matching key, otherwise None (*)
        -------------------------------------------------------
        """
        # your code here
        i = self._binary_search(key)
        value = None
        if i > -1:
            value = deepcopy(self._values[i])
        return value

    def __eq__(self, target):
        """
        -------------------------------------------------------
        Determines whether source == target.
        If source and target are of the same length and contain the same values,
        returns True, otherwise returns False.
        Order is significant.
        Use: equals = source == target
        -------------------------------------------------------
        Parameters:
            target - another sorted set (Sorted_Set)
        Returns‌​‌​​​​‌​​‌‌‌​‌​​​​‌‌​‌‌​‌​​:
            equals - True if source contains the same values
                as target in the same order, otherwise False. (boolean)
        -------------------------------------------------------
        Examples:
            {1,2,3} == {1,2,3}: True
            {1,2,3} == {1,2,4}: False
            {1,2,3} == {1,2,3,4}: False
        -------------------------------------------------------
        """
        # your code here
        equals = True
        if len(self._values) != len(target._values):
            equals = False
        else:
            for i in range(len(self._values)):
                if self._values[i] != target._values[i]:
                    equals = False

        return equals

    def issubset(self, target):
        """
        ---------------------------------------------------------
        Tests whether every value in source is also in target.
        Use: subset = source.issubset(target)
        -------------------------------------------------------
        Parameters:
            target - another Sorted_Set. (Sorted_Set)
        Returns‌​‌​​​​‌​​‌‌‌​‌​​​​‌‌​‌‌​‌​​:
            subset - True if all values in source are also in target,
                False otherwise. (boolean)
        -------------------------------------------------------
        Examples:
            {1,2,3}.issubset({0,1,2,3,4}): True
            {1,2,3}.issubset({1,2,4,5}): False
        -------------------------------------------------------
        """
        # your code here
        x = 0
        y = 0
        subset = True

        while x < len(self._values) and y < len(target._values):
            if self._values[x] < target._values[y]:
                subset = False
            elif self._values[x] == target._values[y]:
                x += 1
                y += 1
            else:
                y += 1

        return subset

    def issuperset(self, target):
        """
        ---------------------------------------------------------
        Test whether every value in target is also in source.
        Use: superset = source.issuperset(target)
        -------------------------------------------------------
        Parameters:
            target - another Sorted_Set. (Sorted_Set)
        Returns‌​‌​​​​‌​​‌‌‌​‌​​​​‌‌​‌‌​‌​​:
            superset - True if all values in target are also in source,
                False otherwise. (boolean)
        -------------------------------------------------------
        Examples:
            {1,2,3}.issuperset({0,1,2,3,4}): False
            {1,2,3,4,5}.issuperset({1,2,4,5}): True
        -------------------------------------------------------
        """
        # your code here
        x = 0
        y = 0
        super_set = True

        while x < len(target._values) and y < len(self._values):
            if target._values[x] < self._values[y]:
                super_set = False
            elif target._values[x] == self._values[y]:
                x += 1
                y += 1
            else:
                y += 1

        return super_set

    def isdisjoint(self, target):
        """
        -------------------------------------------------------
        Return True if source has no values in common with target.
        Sorted_Sets are disjoint if and only if their intersection
        is the empty Sorted_Set.
        Use: disjoint = source.isdisjoint(target)
        -------------------------------------------------------
        Parameters:
            target - a Sorted_Set to compare against source. (Sorted_Set)
        Returns‌​‌​​​​‌​​‌‌‌​‌​​​​‌‌​‌‌​‌​​:
            disjoint - True if source has no values in common with target,
                False otherwise. (boolean)
        -------------------------------------------------------
        Examples:
            {1,2,3}.isdisjoint({4,5,6,7}): True
            {1,2,3}.isdisjoint({1,4,5,6,7}): False
        -------------------------------------------------------
        """
        x = 0
        y = 0
        disjoint = True

        while x < len(self._values) and y < len(target._values):
            if self._values[x] < target._values[y]:
                x += 1
            elif self._values[y] > target._values[y]:
                y += 1
            else:
                disjoint = False

        return disjoint

    def intersection(self, target):
        """
        -------------------------------------------------------
        Return a new Sorted_Set with copies of values common to source and target.
        Order must be preserved.
        Use: new_set = source.intersection(target)
        -------------------------------------------------------
        Parameters:
            target - an array-based sorted set. (Sorted_Set)
        Returns‌​‌​​​​‌​​‌‌‌​‌​​​​‌‌​‌‌​‌​​:
            new_set - the intersection of source and target. (Sorted_Set)
        -------------------------------------------------------
        Examples:
            {1,2,3}.intersection({3,4,5}): {3}
            {1,2,3}.intersection({4,5,6}): {}
        -------------------------------------------------------
        """
        # your code here
        new_set = Sorted_Set()
        x = 0
        y = 0

        while x < len(self._values) and y < len(target._values):
            if self._values[x] < target._values[y]:
                x += 1
            elif self._values[x] > target._values[y]:
                y += 1
            else:
                new_set._values.append(deepcopy(self._values[x]))
                x += 1
                y += 1

        return new_set

    def union(self, target):
        """
        -------------------------------------------------------
        Return a new Sorted_Set with copies of all unique values from source and target.
        Order must be preserved.
        Use: new_set = source.union(target)
        -------------------------------------------------------
        Parameters:
            target - an array-based sorted set (Sorted_Set)
        Returns‌​‌​​​​‌​​‌‌‌​‌​​​​‌‌​‌‌​‌​​:
            new_set - the union of source and target (Sorted_Set)
        -------------------------------------------------------
        Examples:
            {1,2,3}.union({3,4,5}): {1,2,3,4,5}
            {1,2,3}.union({4,5,6}): {1,2,3,4,5,6}
        -------------------------------------------------------
        """
        # your code here
        new_set = Sorted_Set()
        x = 0
        y = 0

        while x < len(self._values) and y < len(target._values):
            if self._values[x] < target._values[y]:
                new_set._values.append(deepcopy(self._values[x]))
                x += 1
            elif self._values[x] > target._values[y]:
                new_set._values.append(deepcopy(target._values[y]))
                y += 1
            else:
                new_set._values.append(deepcopy(self._values[x]))
                x += 1
                y += 1

        while x < len(self._values):
            new_set._values.append(self._values[x])
            x += 1

        while y < len(target._values):
            new_set._values.append(target._values[y])
            y += 1

        return new_set

    def difference(self, target):
        """
        -------------------------------------------------------
        Return a new Sorted_Set with copies of values in source that are not in target.
        Order is preserved.
        Use: new_set = source.difference(target)
        -------------------------------------------------------
        Parameters:
            target - an array-based sorted set. (Sorted_Set)
        Returns‌​‌​​​​‌​​‌‌‌​‌​​​​‌‌​‌‌​‌​​:
            new_set - the difference of source and target. (Sorted_Set)
        -------------------------------------------------------
        Examples:
            {1,2,3}.difference({3,4,5}): {1,2}
            {2,3,4}.difference({1,2,3,4,5}): {}
        -------------------------------------------------------
        """
        # your code here
        new_set = Sorted_Set()
        x = 0
        y = 0

        while x < len(self._values) and y < len(target._values):
            if self._values[x] < target._values[y]:
                new_set._values.append(self._values[x])
                x += 1
            elif self._values[x] > target._values[y]:
                y += 1
            else:
                x += 1
                y += 1

        while x < len(self._values):
            new_set._values.append(self._values[x])
            x += 1
        return new_set

    def symmetric_difference(self, target):
        """
        -------------------------------------------------------
        Return a new set with copies of values in either source or target but not both.
        Order must be preserved.
        Use: new_set = source.symmetric_difference(target)
        -------------------------------------------------------
        Parameters:
            target - an array-based Set. (Set)
        Returns‌​‌​​​​‌​​‌‌‌​‌​​​​‌‌​‌‌​‌​​:
            new_set - the symmetric difference of source and target. (Set)
        -------------------------------------------------------
        Examples:
            {1,2,3}.symmetric_difference({3,4,5}): {1,2,4,5}
            {1,2,3}.symmetric_difference({1,2,3,4,5}): {4,5}
        -------------------------------------------------------
        """
        # your code here
        new_set = Sorted_Set()
        x = 0
        y = 0

        while x < len(self._values) and y < len(target._values):
            if self._values[x] < target._values[y]:
                new_set._values.append(deepcopy(self._values[x]))
                x += 1
            elif self._values[x] > target._values[y]:
                new_set._values.append(deepcopy(target._values[y]))
                y += 1
            else:
                x += 1
                y += 1

        while x < len(self._values):
            new_set._values.append(deepcopy(self._values[x]))
            x += 1

        while y < len(target._values):
            new_set._values.append(deepcopy(target._values[y]))
            y += 1

        return new_set

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through a Sorted_Set
        from front to rear.
        Use: for v in source:
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌‌​‌​​​​‌‌​‌‌​‌​​:
            value - the next value in the Sorted_Set. (*)
        -------------------------------------------------------
        """
        for value in self._values:
            yield value
