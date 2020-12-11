#https://www.linkedin.com/learning/python-data-structures-linked-lists/coding-the-singly-linked-list-node-class
class SLLNode:
	def __init__(self, data):
		self.data = data
		self.next = None

	def __repr__(self):
		return "SLLNode object: data={}".format(self.data)

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


""" I want to highlight the fact that linked lists don't contain nodes. 
Instead, they have a head attribute that points to the first node of the linked list if one exists. 
Otherwise, the head attribute points to none."""
class SLL:
	def __init__(self):
		self.head = None


	def __repr__(self):
		return "SLL object: head={}".format(self.head)



	def is_empty(self):
		""" Returns True if the linked list is empty otherwise it returns false """
		return self.head is None # self.head == None if we call this method it would return true if the head is empty or false if there is a node there.
		#below is another way to check if the node is empty longer than the one above
		"""if self.head == None:
			return True
		else: 
			return False """ 



	def add_front(self, new_data):
		"""  Add a node whose data is the new_data arguement to the front of the linked list"""
		temp = SLLNode(new_data)
		temp.set_next(self.head)
		self.head = temp


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

	def remove(self, data):
		""" Removes the first occurence of the neod that contains the data argument as in self.data variable, returns nothing"""
		if self.head is None:
			return "the Linked List is empty no nodes to remove"
		current = self.head
		previous = None
		found = False
		while not found:
			if current.get_data() == data:
				found = True
			else:
				if current.get_next() == None:
					return" A node with that data value is not present"
				else:
					previous = current
					current = current.get_next()

		if previous is None:
			self.head = current.get_next()
		else:
			previous.set_next(current.get_next())



sll = SLL()
sll.add_front(27)
print(sll.remove(15))
sll.remove(27)
print(sll.head)
sll.add_front("apple")
sll.add_front("berry")
sll.add_front("cherry")
sll.remove("berry")
print(sll.head)
print(sll.head.next)

