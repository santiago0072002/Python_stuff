#https://www.linkedin.com/learning/python-data-structures-linked-lists/creating-the-singlylinkedlist-class-and-its-methods

class DLLNode:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.previous = None

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

	def get_previous(self):
		""" Return the self.previous attribute"""
		return self.previous

	def set_previous(self, new_previous):
		"""Replaced the existing value of the self.previous attribute with the new_previous parameter"""
		self.previous = new_previous

node1 = DLLNode(1)
node2 = DLLNode(2)
print(node1.get_previous())
node1.set_previous(node2)
print(node1.get_previous())