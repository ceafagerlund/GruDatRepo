#Alexander Fagerlund, GruDat, uppg 2.5

import random

class treap:
    """Randomized binary search tree for strings."""

    def __init__(self): # time complexity O(1)
        """Creates empty tree"""
        self.data = None
        self.right = None
        self.left = None
        self.parent = None
        self.prio = random.randint(1,10000)


    def add(self,node):     # worst case time complexity: O(n) (going through singly linked list)
        """Given string node, adds string to tree."""
        if type(node) is str:
            text = node
            node = treap()
            node.data = text
            if self.data is None:
                self.data = node.data
                return self
            elif node.data == self.data:
                pass
            elif node.data < self.data:
                if self.left is None:
                    self.left = treap()
                self.left = self.left.add(node.data)
                if self.prio > self.left.prio:
                    print("rotate right", text)
                    self.rotate_right()
            else:
                if self.right is None:
                    self.right = treap()
                self.right = self.right.add(node.data)
                if self.prio > self.right.prio:
                    print("rotate left", text)
                    self.rotate_left()
            return self

        else:
            raise ValueError("Input must be string!")

    def _inorder(self,rep):     # visits all elements --> time complexity O(n)
        """Visit all nodes of a binary search tree in sorted order."""
        if self.data is None:
            pass
        else:
            rep.append(self.data)
            if self.left:
                self.left._inorder(rep)
            if self.right:
                self.right._inorder(rep)
        rep.sort()
        return rep
        
    def size(self): #inherits complexity from inorder--> O(n). See inorder.
        """Returns number of elements in tree."""
        rep = []
        self._parentcheck(rep)
        rep = self._inorder(rep)
        length = len(rep)
        return length

    def string(self):   #inherits complexity from inorder--> O(n). See inorder.
        """Returns all elements in alphabetical order as string representation."""
        text = []
        self._parentcheck(text)
        text = self._inorder(text)
        return(text)
    
    def _parentcheck(self,text):
        if self.parent:
            text.append(self.parent.data)
            if self.parent.left == self and self.parent.right is not None and self.parent.right != self:
                text.append(self.parent.right.string())
            elif self.parent.left is not None and self.parent.right == self and self.parent.left != self:
                text.append(self.parent.left.string())
            self.parent._parentcheck(text)
            

    def rotate_right(self):         #time complexity O(1)
        if self.left is not None:
            old_left = self.left
            self.left = old_left.right
            self.parent = old_left
            old_left.right = self
            
            if self.parent:
                if self.parent.right == self:
                    self.parent.right = old_left
                else:
                    self.parent.left = old_left


    def rotate_left(self):          #time complexity O(1)
        if self.right is not None:
            old_right = self.right
            self.right = old_right.left
            self.parent = old_right
            old_right.left = self
            
            if self.parent:
                if self.parent.right == self:
                    self.parent.right = old_right
                else:
                    self.parent.left = old_right

            
#Unit test
a = treap()
assert a.size() == 0
assert a.string() == []
a.add("D")
assert a.data == "D"
#assert a.size() == 1
a.add("B")
#assert a.right.data == "EF"
#assert a.left == None
#assert a.size() == 2
a.add("E")
#print(a.string())
#a.add("F")
#assert a.size() == 3
#assert a.left.data == "B"
#assert a.right.data == "EF"
#a.add("R") 
#assert a.right.data == "EF"
#a.add("P")
#assert a.right.right.left.data == "P"
#assert a.string() == ['B', 'D', 'EF', 'P', 'R']
#assert a.size() == 5


            
