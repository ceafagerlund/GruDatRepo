
class ListElement:
    """Implements a node for linked list use."""
    def __init__(self,content,next):
        """Make default node"""
        self.content = ""
        self.next = ""

class LinkedList:
        """This class implements a linked list."""

        def __init__(self):
            self._first_Element = None                   #first element
            self._last_Element =  None                   #last element
            self._length = 0                             #list length

        def healthy(self): 		#first, last nollpekare? Vad menas? https://stackoverflow.com/questions/25825693/calling-one-method-from-another-within-same-class-in-python
            """Testing function. Checks list."""
            if self._length == 0:
                assert self._first_Element.content == None 			# empty first, last for empty list
                assert self._last_Element.content == None
                assert self._first_Element.next == None
            #elif self._length == 1: #assertion error här...
                #assert not self._first_Element.content == None and self._last_Element.content == None or self._first_Element.content == None and not self._last_Element.content == None
            else:
                assert not self._first_Element.content == None 			# empty first, last for empty list
                assert not self._last_Element.content == None
                assert not self._first_Element.next == None
            assert self._last_Element.next == None 					# always points to null
            sizecount = 0
            init = self._first_Element
            while not init == None:
                sizecount += 1
                init = init.next
            assert self._length == sizecount

        def new(self):  #call: LL.new()
            """Construct empty linked list"""
            self._first_Element = ListElement(None,None)
            self._last_Element = self._first_Element
            self._length = 0

        def addFirst(self, elem):           #klar
            """Insert the given element at the beginning of this list."""
            _first_Old = self._first_Element
            self._first_Element = ListElement(elem,self._first_Element)
            self._first_Element.content = elem
            self._first_Element.next = _first_Old
            self._length += 1
            #self.healthy()

        def addLast(self, elem):         	  #klar
            """Insert the given element at the end of this list."""
            _last_Old = self._last_Element
            self._last_Element = ListElement(elem,self._last_Element)
            self._last_Element.content = elem
            self._last_Element.next = None
            self._length += 1
            _last_Old.next = self._last_Element
            #self.healthy()

###Har rättat hit ned.

        def getFirst(self, _first_Element,_last_Element,_length):
            """Return the first element of this list.
            Return null if the list is empty."""
            if self._length == 0:
                raise ValueError("List is empty")
            else:
                return self._first_Element

        def getLast():
            """Return the last element of this list.
            Return null if the list is empty."""
            if self._length == 0:
                raise ValueError("List is empty")
            else:
                return self._last_Element

        def get(index):
            """Return the element at the specified position in this list.
            Return null if index is out of bounds."""
            if index > self._length:
                raise ValueError("list is not that long")
            else:
                iter = self._first_Element
                for k in range (1,index):
                    iter = iter.next
                return iter

        def removeFirst(specific_list):
            """Remove and returns the first element from this list.
            Return null if the list is empty."""
            if self._length != 0:
			    #remove?
                return _first.Element
            else:
                raise ValueError("List is empty")

        def clear():
            """Remove all elements from the list."""
            self._length = 0
		    #remove?

        def length():
            """Return the number of elements in the list."""
            return (_self.length)

        def string():
            """Return a string representation of this list.
            The elements are enclosed in square brackets ("[]").
            Adjacent elements are separated by ", "."""
            iter = _self.first_Element
            print("[")
            for k in range(1,self._length):
                print(iter,",")
                iter = iter.next
return ("]")



# Unit test
#testing code here

z = LinkedList()
z.new()
z.addFirst(3)
z.addLast(56)
