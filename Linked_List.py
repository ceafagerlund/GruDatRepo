class LinkedList:
        """This class implements a linked list."""
        self._first_Element = None                   #first element
        self._last_Element =  None                   #last element
        self._length = 0                             #list length

        def _init_(self):
            """Construct empty linked list"""
            self._first_Element = ListElement(None,None)
            healthy()

        def addFirst(elem):           #klar
            """Insert the given element at the beginning of this list."""
            self._first_Element = ListElement(elem,_self.first_Element)
            self._length += 1
            healthy()

        def addLast(elem):         	  #klar
            """Insert the given element at the end of this list."""
            self._last_Element.next = elem
            self._last_Element = ListElement(elem,None)
            self._length += 1
            healthy()

        def getFirst():
            """Return the first element of this list.
            Return null if the list is empty."""
            if self._length == 0:
                raise valueError("List is empty")
            else:
                return self._first_Element

        def getLast():
            """Return the last element of this list.
            Return null if the list is empty."""
            if self._length == 0:
                raise valueError("List is empty")
            else:
                return self._last_Element

        def get(index):
            """Return the element at the specified position in this list.
            Return null if index is out of bounds."""
            if index > self._length:
                raise valueError("list is not that long")
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
                raise valueError("List is empty")

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
			    for k = 1:1:_self.length:
				    print(iter,",")
				    iter = iter.next
			    return ("]")

class ListElement:
    """Implements a node for linked list use."""
    def _init_(self,content,next):
        """Make default node"""
        self.content = None
        self.next = None

def healthy(): 		#first, last nollpekare? Vad menas?
    """Testing function. Checks list."""
    if _self.length = 0:
		assert _self.first_Element.content == None 			# empty first, last for empty list
		assert _self.last_Element.content == None
		assert _self.first_Element.next == None
	else if _self.length = 1: 								# either only first or only last
		assert _self.first_Element.content != None and _self.last_Element.content = None or _self.first_Element.content = None and _self.last_Element.content != None
	else:
		assert _self.first_Element.content != None 			# empty first, last for empty list
		assert _self.last_Element.content != None
		assert _self.first_Element.next != None
	assert _self.last_Element.next == None 					# always points to null

	sizecount = 0
	init = _self.first_Element
	while init != None 										#assume no None elements in middle of code
		sizecount += 1
		init = init.next
	assert _self.length == sizecount



# Unit test
#testing code here
