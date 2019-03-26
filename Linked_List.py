
class ListElement:  #OK
    """Implements a node for linked list use."""
    def __init__(self,content,next):
        """Make default node"""
        self.content = None
        self.next = None

class LinkedList:
        """This class implements a linked list."""

        def __init__(self):     #OK
            self._first_Element = None                   #first element
            self._last_Element =  None                   #last element
            self._length = 0                             #list length

        def healthy(self): 		#first, last nollpekare? Vad menas? https://stackoverflow.com/questions/25825693/calling-one-method-from-another-within-same-class-in-python
            """Testing function. Checks list."""
            if self._length == 0:
                assert self._first_Element.content == None 			# empty first, last for empty list
                assert self._last_Element.content == None
                assert self._first_Element.next == None
            elif self._length == 1: #assertion error här...
                assert not self._first_Element.content == None and self._last_Element.content == None or self._first_Element.content == None and not self._last_Element.content == None
            else:
                assert not self._first_Element.content == None 			# empty first, last for empty list
                assert not self._last_Element.content == None
                assert not self._first_Element.next == None
                assert self._last_Element.next == None 					# always points to null
            sizecount = 0
            init = self._first_Element
            while not init.next == None:
                sizecount += 1
                init = init.next
            assert self._length == sizecount
##New behövs inte, ska vara __init__

        def new(self):  #OK. Onödig?
            """Construct empty linked list"""
            self._first_Element = ListElement(None,None)
            self._last_Element = self._first_Element
            self._length = 0

        def addFirst(self, elem):           #OK
            """Insert the given element at the beginning of this list."""
            _first_Old = self._first_Element
            self._first_Element = ListElement(elem,self._first_Element)
            self._first_Element.content = elem
            self._first_Element.next = _first_Old
            self._length += 1
            self.healthy()

        def addLast(self, elem):         	  #OK
            """Insert the given element at the end of this list."""
            _last_Old = self._last_Element
            self._last_Element = ListElement(elem,self._last_Element)
            self._last_Element.content = elem
            self._last_Element.next = None
            self._length += 1
            _last_Old.next = self._last_Element
            self.healthy()



        def getFirst(self):         #OK
            """Return the first element of this list.
            Return null if the list is empty."""
            if self._length == 0:
                raise ValueError("List is empty")
            else:
                return self._first_Element.content

        def getLast(self):          #OK
            """Return the last element of this list.
            Return null if the list is empty."""
            if self._length == 0:
                raise ValueError("List is empty")
            else:
                return self._last_Element.content

###Har rättat hit ned.

        def get(self,index):    #OK?
            """Return the element at the specified position in this list.
            Return null if index is out of bounds."""
            if index > self._length:
                raise ValueError("list is not that long")
            else:
                iter = self._first_Element
                for k in range (1,index):
                    iter = iter.next
                return iter.content

        def removeFirst(self):      #
            """Remove and returns the first element from this list.
            Return null if the list is empty."""
            if not self._length == 0:
                new_first = self._first_Element.next
                return (self._first_Element.content,"has been deleted")
                self._first_Element = new_first
                self._length = self._length - 1
            else:
                raise ValueError("List is empty")

        def clear(self):
            """Remove all elements from the list."""
            for i in range(1,self.length):
                self._first_Element

            self._length = 0



        def length(self):  #OK
            """Return the number of elements in the list."""
            return (self._length)

        def string(self):
            """Return a string representation of this list.
            The elements are enclosed in square brackets ("[]").
            Adjacent elements are separated by ", "."""
            iter = self._first_Element
            print("[", end = '')
            for k in range(0,self._length):
                print(iter.content,",", end = "")
                iter = iter.next
            print("]")



# Unit test
#testing code here

z = LinkedList()
z.new()
z.addFirst(3)
z.addLast(56)
z.getFirst()
z.getLast()
assert z.getFirst() == 3
assert z.getLast() == 56
z.get(1)
