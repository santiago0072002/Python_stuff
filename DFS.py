class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):# method to do a DFS passing an array
        array.append(self.name) # append to the array self.name
        for child in self.children: # for every child in array children
			child.depthFirstSearch(array)# call DFS() in every child passing the array
        return array # return the array
