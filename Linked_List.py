#Alexander Fagerlund, GruDat, uppg 1.2, 1.3.

class _ListElement:         # Help class for nodes
    """Implements a node for linked list use."""

    def __init__(self,content,next):
        """Make default node"""
        self.content = None
        self.next = None


class LinkedList:
        """A singly linked list of elements of type int."""

        def __init__(self):  #Time complexity O(1)
            """Create an empty list"""
            self._first_Element = None                         #first element
            self._last_Element =  None                         #last element
            self._length = 0                                   #list length

        def healthy(self):
            """Testing function. Given list, it verifies that content and pointers are correct."""
            if self._length == 0:
                assert self._first_Element.content == None
                assert self._last_Element.content == None			# empty first, last for empty list
                assert self._first_Element.next == None
            elif self._length == 1:
                assert not self._first_Element.content == None or not self._last_Element.content == None    # content in one node if one node long
            else:
                assert not self._first_Element.content == None 			# empty first, last for empty list
                assert not self._last_Element.content == None
                assert not self._first_Element.next == None
            assert self._last_Element.next == None                      # always true. controls self._last_Element.next for all cases.
            sizecount = 0
            init = self._first_Element
            if self._first_Element.content == None:
                pass
            else:
                sizecount = 1
                while init.next:               # while not pointing to None
                    sizecount += 1
                    init = init.next
            assert self._length == sizecount

        def new(self):  # Time complexity O(1)
            """Construct empty linked list"""
            self._first_Element = _ListElement(None,None)
            self._last_Element = _ListElement(None,None)
            self._first_Element.content = None
            self._last_Element.content = None
            self._first_Element.next = None
            self._last_Element.next = None
            self._length = 0

        def addFirst(self, elem):           # Time complexity O(1)
            """Insert the given element at the beginning of this list."""
            _first_Old = self._first_Element
            self._first_Element = _ListElement(elem,_first_Old)
            self._first_Element.content = elem
            self._first_Element.next = _first_Old
            self._length += 1
            if self._length == 1:
                self._last_Element = self._first_Element
                self._first_Element.next = None
                self._last_Element.next = None

        def addLast(self, elem):         	  # Time Complexity O(1)
            """Insert the given element at the end of this list."""
            old_last = self._last_Element
            helper = _ListElement(elem,None)
            helper.content = elem
            helper.next = None
            if old_last:
                old_last.next = helper
            else:
                self._first_Element = helper
            self._last_Element = helper
            self._length += 1

        def getFirst(self):         # Time complexity O(1)
            """Return the first element of this list.
            Return null if the list is empty."""
            if self._length == 0:
                raise ValueError("List is empty")
            else:
                return self._first_Element.content

        def getLast(self):          # Time complexity O(1)
            """Return the last element of this list.
            Return null if the list is empty."""
            if self._length == 0:
                raise ValueError("List is empty")
            else:
                return self._last_Element.content

        def get(self,index):    # uses 1-indexation. Time complexity: O(n) (worst case).
            """Return the element at the specified position in this list.
            Return null if index is out of bounds."""
            if index > self._length or index<1:         # 1-indexation
                raise ValueError("outside of list!")
            else:
                iter = self._first_Element
                for k in range (1,index):
                    iter = iter.next
                return iter.content

        def removeFirst(self):      # Time complexity O(1)
            """Remove and returns the first element from this list.
            Return null if the list is empty."""
            if not self._length == 0:
                new_first = self._first_Element.next
                print (self._first_Element.content, "will be deleted")
                old_first = self._first_Element
                self._first_Element = new_first
                self._length = self._length - 1
                return old_first.content
            else:
                raise ValueError("List is empty")

        def clear(self):        # Time complexity O(1)
            """Remove all elements from this list."""
            self._first_Element.content = None
            self._first_Element.next = None
            self._last_Element.content = None
            self._last_Element.next = None
            self._length = 0

        def size(self):  # Time complexity O(1)
            """Return the number of elements in this list."""
            return (self._length)

        def string(self):       # Time complexity O(n) (worst case)
            """Return a string representation of this list.
            The elements are enclosed in square brackets ("[]").
            Adjacent elements are separated by ", "."""
            if self._first_Element:
                iter = self._first_Element
                pre_list = ""
                pre_list += "["
                for k in range(0,self._length):
                    pre_list += str(iter.content)
                    pre_list += ", "
                    iter = iter.next
                pre_list = pre_list.rstrip(',')  #Help from: https://stackoverflow.com/questions/12625636/python-string-function-to-strip-the-last-comma
                pre_list += "]"
            else:
                pre_list = "[]"
            return pre_list

# Unit test

# Testing code below

z = LinkedList()
z.new()
assert z.string() == "[]"
assert z.size() == 0
z.healthy()
z.addFirst(3)
z.healthy()
z.addFirst(8)
z.healthy()
z.addLast(56)
z.healthy()
z.addLast(0)
z.healthy()
z.getFirst()
z.healthy()
z.getLast()
z.healthy()
assert z.getFirst() == 8
assert z.getLast() == 0
assert z.get(2) == 3
z.removeFirst()
assert z.getFirst() == 3
assert z.size() == 3
z.clear()
assert z.size() == 0
assert z.string() == "[]"
z.healthy()
