#Alexander Fagerlund, GruDat, uppg 2.3

import random

class treap:
    """Randomized binary search tree for strings."""

    def __init__(self):             #time complexity O(1)
        """Creates empty tree"""
        self.data = None
        self.right = None
        self.left = None
        self.parent = None
        self.prio = random.randint(1,10000)



    def add(self,node):
        """Given string node, adds string to tree."""
        if type(node) is str:
            text = node
            node = treap()
            node.data = text
            if self.data is None:
                self.data = node.data
            elif node.data == self.data:
                pass
            elif node.data < self.data:
                if self.left is None:
                    self.left = treap()
                self.left = self.left.add(node.data)
                #if self.prio > self.left.prio:
                    #self.rotate_right()
            else:
                if self.right is None:
                    self.right = treap()
                self.right = self.right.add(node.data)
                #if self.prio > self.right.prio:
                    #self.rotate_left()
            return self

        else:
            raise ValueError("Input must be string!")

    def _inorder(self,rep):
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
        
    def size(self):
        """Returns number of elements in tree."""
        rep = []
        rep = self._inorder(rep)
        length = len(rep)
        return length

    def string(self):
        """Returns all elements in alphabetical order as string representation."""
        text = []
        text = self._inorder(text)
        #print (text)
        return(text)
    

    def rotate_right(self):         #time complexity O(1)
        if self.left is not None:
            helper = self.left
            helper.right = self
            self.left = None
            if self.parent:
                if self.parent.right == self:
                    self.parent.right = helper
                else:
                    self.parent.left = helper

    def rotate_left(self):          #time complexity O(1)
        if self.right is not None:
            helper = self.right
            helper.left = self
            self.right = None
            if self.parent:
                if self.parent.right == self:
                    self.parent.right = helper
                else:
                    self.parent.left = helper

#Unit test
a = treap()
assert a.size() == 0
a.add("D")
assert a.data == "D"
assert a.size() == 1
a.add("EF")
assert a.right.data == "EF"
assert a.left == None
assert a.size() == 2
a.add("B")
assert a.size() == 3
assert a.left.data == "B"
assert a.right.data == "EF"
a.add("R") 
assert a.right.data == "EF"
a.add("P")
assert a.right.right.left.data == "P"
assert a.string() == ['B', 'D', 'EF', 'P', 'R']
assert a.size() == 5
                #wanderer = self.finder()
                #if wanderer.right is None:
                    #if new_node.data >= wanderer.data:
                        #new_node.parent = wanderer
                        #wanderer.right = new_node
                    #else:
                        #wanderer = finder(wanderer.left)
                #elif wanderer.left is None:
                    #if new_node.data < wanderer.data:
                        #new_node.parent = wanderer
                        #wanderer.left = new_node
                    #else:
                        #wanderer = finder(wanderer.right)      
            


    #def finder(self):
        #wanderer = self
        #while wanderer.left != None and wanderer.right != None:
            #if new_node.data < wanderer.data:
                #wanderer = wanderer.left
            #else:
                #wanderer = wanderer.right
        #return wanderer

            #elif self.left is None or self.right is None:
                #if self.left is None:
                    #if new_node.data < self.data:
                        #self.left = new_node
                        #new_node.parent = self.left
                    #else:
                        #self.right
                #else:
                    #self.right = new_node
                    #new_node.parent = self.right
                #self.length += 1
                
            #else:
                
                #if new_node.data < self.data:
                    #if self.left is None:
                        #self.left = treap(new_node.data,None,None,self)
                    #self.left = self.left.add(new_node.data)
                    #if self.prio > self.left.prio:
                        #pass#self.rotate_right()
                #else: 
                    #if self.right is None:
                        #self.right = treap(new_node.data,None,None,self)
                    #self.right = self.right.add(new_node.data) #nonfunctional due to wrong object type. 
                    #if self.prio > self.right.prio:
                        #pass#self.rotate_left()
                #self.length += 1

    #def add(self,node):
        #"""Given string node, adds str to tree."""
        #if type(node) == str:
            #new_node = treap(node,None,None,None)
            #new_node.data = node

            #if self.data is None:
                #self.parent = None
                #self.data = new_node.data
                #return self
