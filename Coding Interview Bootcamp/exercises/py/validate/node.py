class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.left and data < self.data:
            self.left.insert(data)
        elif data < self.data:
            self.left = Node(data)
        if self.right and data > self.data:
            self.right.insert(data)
        elif data > self.data:
            self.right = Node(data)

    def contains(self, data):
        if self.data == data:
            return self
        if self.left and data < self.data:
            return self.left.contains(data)
        if self.right and data > self.data:
            return self.right.contains(data)
        return None
