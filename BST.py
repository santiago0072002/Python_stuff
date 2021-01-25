
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value): # BST Class define, every node has a value and left and a right node. 
        self.value = value
        self.left = None # both of this are defaulted to NONE or default value. 
        self.right = None 
		# in Average this is going to run in O (log(n)time) and | o(1) space, worst would be O(n) time and O(1) space. 
    def insert(self, value):
        currentNode = self # iniitizalize a variable to allow us to keep track of what the current node is, 
                                #because at the beggining the current node is the is the node we are calling on the insertion method and that's self
                                # then we can say while true 
	    while True:# forever or until we use a break statement or return statement. 
		    if value < currentNode.value: # is the value that we are traying to insert is less than the current node's value
				if currentNode.left is None: # this means we are at the very end of a branch
					currentNode.left = BST(value) # then currentNode.left is equal to the value that we are trying to add. 
					break
				else: # this means if current Node.left is not None. that means we have a current subtree to explore.
					currentNode = currentNode.left # current Node = currentNode.left
			else: 
				if currentNode.right is None:
					currentNode.right = BST(value)
					break
				else:
					currentNode = currentNode.right
        return self
		#TestBst.insert(1).insert(5)
		
		# in Average this is going to run in O (log(n)time) and | o(1) space, worst would be O(n) time and O(1) space. 
    def contains(self, value):
        # this contains is pretty similar to the insert method. we start by initializing the currentNode to be self. 
		currentNode = self
		while currentNode is not None: # we check, we compare the values. 
			if value < currentNode.value:
				currentNode = currentNode.left
			elif value > currentNode.value:
				currentNode = currentNode.right
			else: 
				return True
		return False
# in Average this is going to run in O (log(n)time) and | o(1) space, worst would be O(n) time and O(1) space. 
    def remove(self, value, parentNode = None): # this is the most difficult method becuase it got quite a few edge cases.
		currentNode = self
		while currentNode is not None:
			if value < currentNode.value: # if the value that we are passing is less than the currentNode.value 
				parentNode = currentNode
				currentNode = currentNode.left # set the currentNode to be equal to the currentNode.left
			elif value > currentNode.value:
				parentNode = currentNode
				currentNode = currentNode.right
        	else:
				# first case if the case that we are trying to remove a node that has two children nodes. in this case we want to find the smallest node of the right sub tree
				# and replace it with the value that we are trying to remove
				if currentNode.left is not None and currentNode.right is not None:
					currentNode.value = currentNode.right.getMinValue() # create a new method to get the smallest element on the right BST we are calling it on the right BST
					currentNode.right.remove(currentNode.value, currentNode)# remove currentNode.value passing in the currentNode as a parent. 
				# this is the rootNode case
				elif parentNode is None: 
					if currentNode.left is not None:
						currentNode.value = currentNode.left.value
						currentNode.right = currentNode.left.right
						currentNode.left = currentNode.left.left 
					elif currentNode.right is not None:
						currentNode.value = currentNode.right.value
						currentNode.left = currentNode.right.left
						currentNode.right = currentNode.right.right
					else: 
						# if it doesn't have any children nodes
						#currentNode.value = None
						pass
				# the other case is when we don't have two child nodes present
				elif parentNode.left == currentNode:
					parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
				elif parentNode.right == currentNode:
					parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
				break
		return self
	
	def getMinValue(self):
		currentNode = self
		while currentNode.left is not None:
			currentNode = currentNode.left
		return currentNode.value 
	
B = BST
B.insert(1)
