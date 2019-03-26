
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
                assert not self._first_Element.content == None or not self._last_Element.content == None
            else:
                assert not self._first_Element.content == None 			# empty first, last for empty list
                assert not self._last_Element.content == None
                assert not self._first_Element.next == None
                assert self._last_Element.next == None 	#fungerar ej				# always points to null
            sizecount = 0
            init = self._first_Element
            #while init.next:               #Behandlar som int, ej som nod. Varför? Får automatiska error!
                #sizecount += 1
                #init = init.next
            #print(sizecount)
            #assert self._length == sizecount
##New behövs inte, ska vara __init__

        def new(self):  #OK. Onödig?
            """Construct empty linked list"""
            self._first_Element = ListElement(None,None)
            self._last_Element = self._first_Element
            self._length = 0

        def addFirst(self, elem):           #OK
            """Insert the given element at the beginning of this list."""
            _first_Old = self._first_Element
            self._first_Element = ListElement(elem,_first_Old)
            self._first_Element.content = elem
            self._first_Element.next = _first_Old
            self._length += 1
            if self._length == 1:
                self._last_Element = self._first_Element
            self.healthy()

        def addLast(self, elem):         	  # Ikoppling pekare fungerar nu!
            """Insert the given element at the end of this list."""
            old_last = self._last_Element
            helper = ListElement(elem,None)
            helper.content = elem
            helper.next = None
            old_last.next = helper
            self._last_Element = helper
            self._length += 1
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


        def get(self,index):    #OK
            """Return the element at the specified position in this list.
            Return null if index is out of bounds. 1-indexed."""
            if index > self._length or index<1:
                raise ValueError("outside of list!")
            else:
                iter = self._first_Element
                for k in range (1,index):
                    iter = iter.next
                return iter.content

        def removeFirst(self):      #OK
            """Remove and returns the first element from this list.
            Return null if the list is empty."""
            if True:
                new_first = self._first_Element.next
                print (self._first_Element.content, "will be deleted")
                self._first_Element = new_first
                self._length = self._length - 1
            else:
                raise ValueError("List is empty")

        def clear(self):        #OK
            """Remove all elements from the list."""
            self._first_Element = None
            self._last_Element = None
            self._length = 0


        def length(self):  #OK
            """Return the number of elements in the list."""
            return (self._length)

        def string(self):       #OK
            """Return a string representation of this list.
            The elements are enclosed in square brackets ("[]").
            Adjacent elements are separated by ", "."""
            iter = self._first_Element
            print("[", end = '')
            for k in range(0,self._length):
                print(iter.content,",",end = '')
                iter = iter.next
            print("]")

###Har rättat allt utom healthy

# Unit test
#testing code here

z = LinkedList()
z.new()
assert z.length() == 0
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
assert z.length() == 3
z.clear()
assert z.length() == 0
assert z.string() == None
# assert z.string() == "dfgfd"
