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
Otherwise, the head attribute points to none.
 We'll need to keep this in mind as we code our link list Data Structure""" 
node = SLLNode("Apple")
print(node.get_data())
node.set_data(7)
print(node.get_data())
node2 = SLLNode("APPLE")
node.set_next(node2)
print(node.get_next())