
class LinkedList:
	"""This class implements a linked list."""
    def _init_(self):
        """Construct empty linked list"""
        _self.first_Element = 1                   #first element
        _self.last_Element =  2                   #last element
        _self.length = 3                         #list length

	def newList(self, firstElement):
		"""Create a new list."""                  #hur göra godtyckligt lång?
		node0 = ListElement()
        node1 = ListElement()
        node2 = ListElement()

        node0.content = _self.first_Element
        node2.content = _self.last_Element

        node0.nextNode = node1
        node1.nextNode = node2
        node2.Nextnode = None


	def addFirst(Elem0):           #klar
		"""Insert the given element at the beginning of this list."""
        node1.content = Elem1

    def addLast(Elem2):         #klar
        """Insert the given element at the end of this list."""
        node2.content = Elem2

    def getFirst():
        """Return the first element of this list.
        Return null if the list is empty."""
        if not _self:
            return None
        else:
            return _self.first_Element

    def getLast():
        """Return the last element of this list.
        Return null if the list is empty."""
        if not _self:
            return None
        else:
            return _self.last_Element

    def get(index):
        """Return the element at the specified position in this list.
        Return null if index is out of bounds."""
        if 0 < index < _self.length
            #return element
        else:
            return None


    def removeFirst(specific_list):
        """Remove and returns the first element from this list.
        Return null if the list is empty."""
        if not specific_list:   #cred stackexchange, see https://stackoverflow.com/questions/53513/how-do-i-check-if-a-list-is-empty
            return _first.Element
        else:
            return None

    def clear(specific_list):
        """Remove all elements from this list."""
        specific_list = []

	def length(specific_list):
		"""Return the number of elements in the list."""
		return (specific_list.length)

    def string(specific_list):
        """Return a string representation of this list.
        The elements are enclosed in square brackets ("[]").
        Adjacent elements are separated by ", "."""
        return "["node0.content","node1.content","node2.content"]"

class ListElement:
    """Implements a node for linked list use."""
    def _init_(self):
        """Make default node"""
        self.content = 3
        self.nextNode = 4


# Unit test
#testing code here
