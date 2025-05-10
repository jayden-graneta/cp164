"""
-------------------------------------------------------
Linked version of the BST ADT.
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2024-08-14"
-------------------------------------------------------
"""
# Imports
from copy import deepcopy


class _BST_Node:

    def __init__(self, value):
        """
        -------------------------------------------------------
        Initializes a BST node containing value. Child pointers 
        are None, height is 1.
        Use: node = _BST_Node(value)
        -------------------------------------------------------
        Parameters:
            value - value for the node (?)
        Returns:
            A _BST_Node object (_BST_Node)            
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._left = None
        self._right = None
        self._height = 1
        self._count = 0

    def _update_height(self):
        """
        -------------------------------------------------------
        Updates the height of the current node.
        Use: node._update_height()
        -------------------------------------------------------
        Returns:
            _height is 1 plus the maximum of the node's two children.
        -------------------------------------------------------
        """
        # your code here
        if self._left is None:
            left_height = 0
        else:
            left_height = self._left._height
        if self._right is None:
            right_height = 0
        else:
            right_height = self._right._height

        self._height = max(right_height, left_height) + 1

        return

    def __str__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Returns node height and value as a string - for debugging.
        -------------------------------------------------------
        """
        return "h: {}, v: {}".format(self._height, self._value)


class BST:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty BST.
        Use: bst = BST()
        -------------------------------------------------------
        Returns:
            A BST object (BST)
        -------------------------------------------------------
        """
        self._root = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if bst is empty.
        Use: b = bst.is_empty()
        -------------------------------------------------------
        Returns:
            True if bst is empty, False otherwise.
        -------------------------------------------------------
        """
        # your code here
        return self._root is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of nodes in the BST.
        Use: n = len(bst)
        -------------------------------------------------------
        Returns:
            the number of nodes in the BST.
        -------------------------------------------------------
        """
        # your code here
        return self.count

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the bst. Values may appear 
        only once in a tree.
        Use: b = bst.insert(value)
        -------------------------------------------------------
        Parameters:
            value - data to be inserted into the bst (?)
        Returns:
            inserted - True if value is inserted into the BST,
                False otherwise. (boolean)
        -------------------------------------------------------
        """
        # your code here
        self._root, inserted = self._aux_insert(self._root, value)

        return inserted

    def _aux_insert(self, node, value):
        if node is None:
            node = _BST_Node(value)
            self._count += 1
            inserted = True
        elif node._value < value:
            self._aux_insert(node._right, value)
        elif node._value > value:
            self._aux_insert(node._left, value)
        else:
            inserted = False

        if inserted:
            node._update_height()

        return node, inserted

    def retrieve(self, key):
        """
        -------------------------------------------------------
        Retrieves a copy of a value matching key in a BST. (Iterative)
        Use: v = bst.retrieve(key)
        -------------------------------------------------------
        Parameters:
            key - data to search for (?)
        Returns:
            value - value in the node containing key, otherwise None (?)
        -------------------------------------------------------
        """
        # your code here
        node = self._root
        value = None

        while value is None and node is not None:
            if node._value > key:
                node._left
            elif node._value < key:
                node._right
            elif node._value == key:
                value = deepcopy(node._value)

        return value

    def remove(self, key):
        """
        -------------------------------------------------------
        Removes a node with a value matching key from the bst.
        Returns the value matched. Updates structure of bst as 
        required.
        Use: value = bst.remove(key)
        -------------------------------------------------------
        Parameters:
            key - data to search for (?)
        Returns:
            value - value matching key if found, otherwise None.
        -------------------------------------------------------
        """
        # your code here
        self._root, value = self._aux_remove(self._root, key)

        return value

    def _aux_remove(self, node, key):

        if node is None:
            value = None
        elif key > node._value:
            node._right, value = self._remove_aux(node._right, key)
        elif key < node._vallue:
            node._left, value = self._remove_aux(node._left, key)
        else:
            # Value has been found.
            value = node._value
            self._count -= 1
            # Replace this node with another node.
            if node._left is None and node._right is None:
                # node has no children.
                node = None

            elif node._left is None:
                # node has no left child.
                node = node._right

            elif node._right is None:
                # node has no right child.
                node = node._left

            else:
                # Node has two children
                if node._left._right is None:
                    repl_node = node._left
                else:

                    repl_node = self._delete_node_left(node._left)
                    repl_node._left = node._left
                    repl_node._right = node._right
                    node = repl_node

# your code here (calls _delete_node somewhere)

        if node is not None and value is not None:
            # If the value was found, update the ancestor heights.
            node._update_height()
        return node, value

    def _delete_node_left(self, parent):
        """
        -------------------------------------------------------
        Finds a replacement node for a node to be removed from the tree.
        Private operation called only by _remove_aux.
        Use: repl_node = self._delete_node_left(node, node._right)
        -------------------------------------------------------
        Parameters:
            parent - node to search for largest value (_BST_Node)
        Returns:
            repl_node - the node that replaces the deleted node. This node 
                is the node with the maximum value in the deleted node's left
                subtree (_BST_Node)
        -------------------------------------------------------
        """
        # your code here
        child = parent._right

        if child._right is None:
            repl_node = child
            parent._right = child._left
        else:
            repl_node = self._delete_node_left(child)

        parent._height_update()
        return repl_node

    def remove_root(self):
        """
        -------------------------------------------------------
        Removes the root node and returns its value.
        Use: value = bst._remove_root()
        -------------------------------------------------------
        Returns:
            value - value in root.
        -------------------------------------------------------
        """
        assert self._root is not None, "Cannot remove the room of an empty BST"

        # your code here
        return

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the bst contains key.
        Use: b = key in bst
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            True if the bst contains key, False otherwise.
        -------------------------------------------------------
        """
        # your code here
        return

    def height(self):
        """
        -------------------------------------------------------
        Returns the maximum height of a BST, i.e. the length of the
        largest path from root to a leaf node in the tree.
        Use: h = bst.height()
        -------------------------------------------------------
        Returns:
            maximum height of bst (int)
        -------------------------------------------------------
        """
        # your code here
        node = self._root

        return

    def __eq__(self, target):
        """
        ---------------------------------------------------------
        Determines whether two BSTs are equal.
        Values in self and target are compared and if all values are equal
        and in the same location, returns True, otherwise returns False.
        Use: equals = source == target
        ---------------
        Parameters:
            target - a bst (BST)
        Returns:
            equals - True if source contains the same values
                as target in the same location, otherwise False. (boolean)
        -------------------------------------------------------
        """
        # your code here
        return

    def parent_i(self, key):
        """
        ---------------------------------------------------------
        Returns the value of the parent node of a key node in a bst.
        ---------------------------------------------------------
        Parameters:
            key - a key value (?)
        Returns:
            value - a copy of the value in a node that is the parent of the
            key node, None if the key is not found. (?)
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot locate a parent in an empty BST"

        # your code here
        return

    def parent_r(self, key):
        """
        ---------------------------------------------------------
        Returns the value of the parent node in a bst given a key.
        ---------------------------------------------------------
        Parameters:
            key - a key value (?)
        Returns:
            value - a copy of the value in a node that is the parent of the
            key node, None if the key is not found.
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot locate a parent in an empty BST"

        # your code here
        return

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in BST. (Iterative algorithm)
        Use: value = bst.max()
        -------------------------------------------------------
        Returns:
            value - a copy of the maximum value in the BST (?)
        -------------------------------------------------------
        """
        assert self._root is not None, "Cannot find maximum of an empty BST"

        # your code here
        node = self._root
        value = None

        while node is not None:
            node = node._right
        value = deepcopy(node._value)

        return value

    def max_r(self):
        """
        ---------------------------------------------------------
        Returns the largest value in a bst. (Recursive algorithm)
        Use: value = bst.max_r()
        ---------------------------------------------------------
        Returns:
            value - a copy of the maximum value in the BST (?)
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot find maximum of an empty BST"

        # your code here
        node = self._root

        node, value = self._aux_max(node)
        return value

    def min(self):
        """
        -------------------------------------------------------
            Finds the minimum value in BST. (Iterative algorithm)
            Use: value = bst.min()
            -------------------------------------------------------
        Returns:
                value - a copy of the minimum value in the BST (?)
        -------------------------------------------------------
        """
        assert self._root is not None, "Cannot find minimum of an empty BST"

        # your code here
        node = self._root
        while node is not None:
            node = node._left
        value = deepcopy(node._value)

        return value

    def min_r(self):
        """
        ---------------------------------------------------------
        Returns the minimum value in a bst. (Recursive algorithm)
        Use: value = bst.min_r()
        ---------------------------------------------------------
        Returns:
            value - a copy of the minimum value in the BST (?)
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot find minimum of an empty BST"

        # your code here
        return

    def leaf_count(self):
        """
        ---------------------------------------------------------
        Returns the number of leaves (nodes with no children) in bst.
        Use: n = bst.leaf_count()
        (Recursive algorithm)
        ---------------------------------------------------------
        Returns:
            count - number of nodes with no children in bst (int)
        ---------------------------------------------------------
        """
        # your code here
        node = self._root
        count = node._aux_leaf_count(node)

        return count

    def _aux_leaf_count(self, node):
        if node is None:
            count = 0

        elif node._left is None and node._right is None:
            count = 1

        else:
            count = self._leaf_count_aux(
                node._left) + self._leaf_count_aux(node._right)

        return count

    def two_child_count(self):
        """
        ---------------------------------------------------------
        Returns the number of the three types of nodes in a BST.
        Use: count = bst.two_child_count()
        -------------------------------------------------------
        Returns:
            count - number of nodes with two children in bst (int)
        ----------------------------------------------------------
        """
        # your code here
        node = self._root
        count = self._aux_two_child_count(node)
        return count

    def _aux_two_child_count(self, node):
        if node is None:
            count = 0
        elif node._left is not None and node._right is not None:
            count = 1 + \
                self._two_child_count_aux(
                    node._left) + self._two_child_count_aux(node._right)
        else:
            count = self._two_child_count_aux(
                node._left) + self._two_child_count_aux(node._right)

        return count

    def one_child_count(self):
        """
        ---------------------------------------------------------
        Returns the number of the three types of nodes in a BST.
        Use: count = bst.one_child_count()
        -------------------------------------------------------
        Returns:
            count - number of nodes with one child in bst (int)
        ----------------------------------------------------------
        """
        # your code here
        node = self._root
        count = self._aux_one_child_count(node)

        return count

    def _aux_one_child_count(self, node):
        if node is None:
            count = 0
        elif node._left is not None and node._right is None:
            count = 1 + self._aux_one_child_count(node._left)
        elif node._right is not None and node._left is None:
            count = 1 + self._aux_one_child_count(node._right)
        else:
            count = 1 + \
                self._aux_one_child_count(
                    node._right) + self._aux_one_child_count(node._left)

        return count

    def node_counts(self):
        """
        ---------------------------------------------------------
        Returns the number of the three types of nodes in a BST.
        Use: zero, one, two = bst.node_counts()
        -------------------------------------------------------
        Returns:
            zero - number of nodes with zero children (int)
            one - number of nodes with one child (int)
            two - number of nodes with two children (int)
        ----------------------------------------------------------
        """
        # your code here
        zero = 0
        one = 0
        two = 0

        node = self._root

        zero, one, two = self._aux_node_counts(node)

        return zero, one, two

    def _aux_node_counts(self, node):

        if node is None:
            pass
        elif node._left is None and node._right is None:
            zero += 1
        elif node._left is None:
            one += 1
            zero, one, two = self._aux_node_counts(node._left)
        elif node._right is None:
            one += 1
            zero, one, two = self._aux_node_counts(node._left)
        else:
            two += 1
            zero, one, two = self._aux_node_counts(node._left)
            zero, one, two = self._aux_node_counts(node._right)
        return zero, one, two

    def is_balanced(self):
        """
        ---------------------------------------------------------
        Returns whether a bst is balanced, i.e. the difference in
        height between all the bst's node's left and right subtrees is <= 1.
        Use: b = bst.is_balanced()
        ---------------------------------------------------------
        Returns:
            balanced - True if the bst is balanced, False otherwise (boolean)
        ---------------------------------------------------------
        """
        # your code here
        node = self._root
        balanced = self._aux_is_balanced(node)
        return balanced

    def _aux_is_balanced(self, node):

        if node is None or node._height == 1:
            balanced = True
        return balanced

    def _node_height(self, node):
        """
        ---------------------------------------------------------
        Helper function to determine the height of node - handles empty node.
        Private operation called only by _is_valid_aux.
        Use: h = self._node_height(node)
        ---------------------------------------------------------
        Parameters:
            node - the node to get the height of (_BST_Node)
        Returns:
            height - 0 if node is None, node._height otherwise (int)
        ---------------------------------------------------------
        """
        # your code here
        return

    def retrieve_r(self, key):
        """
        -------------------------------------------------------
        Retrieves a _value in a BST. (Recursive)
        Use: v = bst.retrieve(key)
        -------------------------------------------------------
        Parameters:
            key - data to search for (?)
        Returns:
            value - If bst contains key, returns value, else returns None.
        -------------------------------------------------------
        """
        # your code here
        return

    def is_valid(self):
        """
        ---------------------------------------------------------
        Determines if a tree is a is_valid BST, i.e. the values in all left nodes
        are smaller than their parent, and the values in all right nodes are
        larger than their parent, and height of any node is 1 + max height of
        its children.
        Use: b = bst.is_valid()
        ---------------------------------------------------------
        Returns:
            valid - True if tree is a BST, False otherwise (boolean)
        ---------------------------------------------------------
        """
        # your code hereif
        return

    def inorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in inorder order.
        Use: a = bst.inorder()
        -------------------------------------------------------
        Returns:
            a - copy of the contents of the tree in inorder (list of ?)
        -------------------------------------------------------
        """
        # your code here
        a = []
        self._inorder_aux(self._root, a)
        return a

    def _inorder_aux(self, node, a):

        if node is not None:
            self._inorder_aux(node._left, a)
            a.append(deepcopy(node._value))
            self._inorder_aux(node._right, a)

    def preorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in preorder order.
        Use: a = bst.preorder()
        -------------------------------------------------------
        Returns:
            a - copy of the contents of the tree in preorder (list of ?)
        -------------------------------------------------------
        """
        # your code here
        return

    def postorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in postorder order.
        Use: a = bst.postorder()
        -------------------------------------------------------
        Returns:
            a - copy of the contents of the tree in postorder (list of ?)
        -------------------------------------------------------
        """
        # your code here
        return

    def levelorder(self):
        """
        -------------------------------------------------------
        Copies the contents of the tree in levelorder order to a list.
        Use: values = bst.levelorder()
        -------------------------------------------------------
        Returns:
            values - a list containing the values of bst in levelorder.
            (list of ?)
        -------------------------------------------------------
        """
        # your code here
        return

    def count(self):
        """
        ---------------------------------------------------------
        Returns the number of nodes in a BST.
        Use: number = bst.count()
        -------------------------------------------------------
        Returns:
            number - count of nodes in tree (int)
        ----------------------------------------------------------
        """
        # your code here
        return

    def __iter__(self):
        """
        -------------------------------------------------------
        Generates a Python iterator. Iterates through a BST node
        in level order.
        Use: for v in bst:
        -------------------------------------------------------
        Returns:
            yields
            value - the values in the BST node and its children (?)
        -------------------------------------------------------
        """
        if self._root is not None:
            # Put the nodes for one level into a queue.
            queue = []
            queue.append(self._root)

            while len(queue) > 0:
                # Add a copy of the data to the sublist
                node = queue.pop(0)
                yield node._value

                if node._left is not None:
                    queue.append(node._left)
                if node._right is not None:
                    queue.append(node._right)
