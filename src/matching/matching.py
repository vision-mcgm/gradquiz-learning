class Node(object):
	#Constructor
    def __init__(self, data):
        self.data = data
        self.children = []

        #Children
    def add_child(self, obj):
        self.children.append(obj)