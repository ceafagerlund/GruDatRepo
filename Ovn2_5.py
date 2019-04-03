#Alexander Fagerlund, GruDat, uppg 2.5


import random

class treap:
    """Randomized binary search tree for strings."""

    def __init__(self):
        """Creates empty tree"""
        self.data = ""
        self.right = ""
        self.left = ""
        self.parent = ""
        self.prio = random.randint(1,1000)
        self.length = 0

    def add(self,node):
        """Given string node, adds str to tree."""
        if type(node) == str:
            new_node = treap()
            new_node.data = node
            if self.length == 0:
                self.length += 1
                self.parent = None
                return new_node.data
            elif new_node.data < self.data:
                self.left = self.left.add(new_node.data)
                if self.prio > self.left.prio:
                    rotate_right()
            else:
                self.right = self.right.add(new_node.data) #nonfunctional due to wrong object type. Node help class? Treap help?
                if self.prio > self.right.prio:
                    rotate_left()
            return self.string()
        else:
            raise ValueError("Input must be string!")

    def size(self):
        """Returns number of elements in tree."""
        return self.length

    def string(self):
        """Returns all elements in alphabetical order as string representation."""
        pass

    def rotate_right():
        self.left.right = self
        self.left.parent = self.parent
        self.left = None
        self.parent = None

    def rotate_left():
        self.right.left = self
        self.right.parent = self.parent
        self.right = None
        self.parent = None


#Unit test
a = treap()
a.add("D")
a.add("EF")
    
