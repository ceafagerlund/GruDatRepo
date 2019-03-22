# A singly linked list of elements of type T.
public LinkedList:
    #private first ListElement # first element in list
    #private last ListElement  # last element in list
    #private size int          # number of elements in list

    # Create an empty list.
    public new() LinkedList

    # Insert the given element at the beginning of this list.
    public void addFirst(element T)

    # Insert the given element at the end of this list.
    public void addLast(element T)

    # Return the first element of this list.
    # Return null if the list is empty.
    public getFirst() T

    # Return the last element of this list.
    # Return null if the list is empty.
    public getLast() T

    # Return the element at the specified position in this list.
    # Return null if index is out of bounds.
    public get(index int) T

    # Remove and returns the first element from this list.
    # Return null if the list is empty.
    public removeFirst() T

    # Remove all elements from this list.
    public clear()

    # Return the number of elements in this list.
    public size() int

    # Return a string representation of this list.
    # The elements are enclosed in square brackets ("[]").
    # Adjacent elements are separated by ", ".
    public string() string



class LinkedList:
	"""This class implements a stack of objects."""
    def _init_(self):
        """Construct empty linked list"""
        _self.firstElement = 1                   #first element
        _self.lastElement =  2                   #last element
        _self.length = 4                         #list length

	def NewList(self, firstElement):
		"""Add x to the top of the stack."""
		self._data += [item]

	def pop(self):
		"""Remove and return the top element of the stack.
		It is a run-time error to call pop on an empty stack.
		"""
		return self._data.pop()

	def length(self):
		"""Return the number of elements in the list."""
		return (self.length)

# Unit test
def main():
	s = Stack() # stack of strings
	s.push("world!")
	s.push("Hello, ")
	assert len(s) == 2

	res = ""
	exp = "Hello, world!"
	while len(s) > 0:
		res += s.pop()
	assert res == exp

	# TODO Add more test cases.

if __name__ == '__main__': main()
