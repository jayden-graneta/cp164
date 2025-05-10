"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Jayden Graneta
ID: 169058740
Email: gran8740@mylaurier.ca
__updated__ = "2024-03-15"
-------------------------------------------------------
"""
# Imports

# Constants


def hash_table(slots, values):
    """
    -------------------------------------------------------
    Print a hash table of a set of values. The format is:
Hash     Slot Key
-------- ---- --------------------
     695    2 Lasagna, 7
    1355    4 Butter Chicken, 2
    Do not create an actual Hash_Set.
    Use: hash_table(slots, values)
    -------------------------------------------------------
    Parameters:
       slots - the number of slots available (int > 0)
       values - the values to hash (list of ?)
    Returns:
       None
    -------------------------------------------------------
    """

    print("Hashes")
    print("Hash     Slot Key")
    print("======== ==== ====================")
    for value in values:
        x = hash(value)
        slot = x % slots
        f_str = value.key()
        print("{:8}{:5} {}".format(x, slot, f_str))
    return
