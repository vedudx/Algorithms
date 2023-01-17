class graphNode:

    def __init__(self, value):
        self.val = value
        self.neighbor = dict()

    def insert(self, node):
        if node not in self.neighbor:
            self.neighbor[node.val] = node
    