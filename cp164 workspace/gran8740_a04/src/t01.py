"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Jayden Graneta
ID: 169058740
Email: gran8740@mylaurier.ca
__updated__ = "2024-02-04"
-------------------------------------------------------
"""
# Imports
from Queue_circular import Queue

q = Queue()

q.insert(123)
q.insert(1)
q.insert(2)
q.insert(3)
print(q._values, q._front, q._rear)

if q.is_empty():
    print("empty")
else:
    print("not empty")

if q.is_full():
    print("The queue is full.")
else:
    print("The queue is not full.")

q.remove()
q.remove()

print(q._values, q._front, q._rear)
