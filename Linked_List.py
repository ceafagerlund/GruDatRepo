
class ListElement:
    """Implements a node for linked list use."""
    def _init_(self,content,next):
        """Make default node"""
        self.content = None
        self.next = None

class LinkedList:
        """This class implements a linked list."""

        def _init_(self,_first_Element,_last_Element,_length):
            _first_Element = None                   #first element
            _last_Element =  None                   #last element
            _length = 0                             #list length

        def healthy(): 		#first, last nollpekare? Vad menas?
            """Testing function. Checks list."""
            if _length == 0:
                assert _first_Element.content == None 			# empty first, last for empty list
                assert _last_Element.content == None
                assert _first_Element.next == None
            elif _length == 1:
                assert not _first_Element.content == None and _last_Element.content == None or _first_Element.content == None and not _last_Element.content == None
            else:
                assert not _first_Element.content == None 			# empty first, last for empty list
                assert not _last_Element.content == None
                assert not _first_Element.next == None
            assert _last_Element.next == None 					# always points to null
            sizecount = 0
            init = _first_Element
            while not init == None:
                sizecount += 1
                init = init.next
            assert _length == sizecount

        def new():  #call: LL.new()
            """Construct empty linked list"""
            _first_Element = ListElement()
            _self.healthy()

        def addFirst(elem):           #klar
            """Insert the given element at the beginning of this list."""
            _first_Element = ListElement(elem,_first_Element)
            _length += 1
            self.healthy()

        def addLast(elem):         	  #klar
            """Insert the given element at the end of this list."""
            _last_Element.next = elem
            _last_Element = ListElement(elem,None)
            _length += 1
            healthy()

        def getFirst():
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

v = ListElement()
v.content = 3
w = ListElement()
w.content = 9
v.next = w
z = LinkedList
z.new()
