#https://www.linkedin.com/learning/python-data-structures-linked-lists/creating-the-singlylinkedlist-class-and-its-methods

class DLLNode:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.previous = None

	def __repr__(self):
		return "DLLNode object: data={}".format(self.data)

	def get_data(self):
		"""return self.data attribute"""
		return self.data


	def set_data(self, new_data):
		"""Replaced the existing value of the self.data attribute with the new data parameter"""
		self.data = new_data

	def get_next(self):
		""" Return the self.next attribute"""
		return self.next

	def set_next(self, new_next):
		"""Replaced the existing value of the self.next attribute with the new_next parameter"""
		self.next = new_next

	def get_previous(self):
		""" Return the self.previous attribute"""
		return self.previous

	def set_previous(self, new_previous):
		"""Replaced the existing value of the self.previous attribute with the new_previous parameter"""
		self.previous = new_previous


class DLL: 

	def __init__(self):
		self.head = None

	def __repr__(self):
		return"<DLL object: head=>".format(self.head)

	def is_empty(self):
		return self.head is None

	def size(self):
		""" Traverses a Linked List and return an integer value representing the number of nodes in the Linked List"""
		# the time complexity is O(n) becuase every node on the list must be visited in order to calculate the size of the linked list
		size = 0
		if self.head is None: 
			return 0

		current = self.head
		while current is not None: # while there are still nodes left to count
			size += 1
			current = current.get_next()

		return size


	def search(self, data):
		"""  it traverse the linked list and returns true id the data searched for is present in one of the nodes. 
		Otherwise, it returns false."""
		if self.head is None:
			return "Linked List is empty. No nodes to search."

		current = self.head	
		while current is not None:
			
			if current.get_data() == data:
				return True
			else: 
				current = current.get_next()
		return False 

	def add_front(self, new_data):
		"""  Add a node whose data is the new_data arguement to the front of the linked list"""
		temp = DLLNode(new_data)
		temp.set_next(self.head)
		if self.head is not None:
			self.head.set_previous(temp)

		self.head = temp

	def remove(self, data):
		""" Removes the first occurence of a Node that contains the data arguement as its self.data attribute Returns nothing"""
		if self.head is None:
			return "Linked List is empty no nodes to remove"

		current = self.head
		found = False
		while not found:
			if current.get_data() == data: 
				found = True
			else:
				if current.get_next() is None:
					return"A node with that data value is not present"
				else: current = current.get_next()

		if current.previous is None:
			self.head = current.get_next()
		else:
			current.previous.set_next(current.get_next())
			current.next.previous(current.get_previous())



#node1 = DLLNode(1)
#node2 = DLLNode(2)
#print(node1.get_previous())
#node1.set_previous(node2)
#print(node1.get_previous())

dll = DLL()
print(dll.size())
print(dll.remove("bird"))
dll.add_front(5)
dll.add_front("apple")
print(dll.size())