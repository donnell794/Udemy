class Stack:
    def __init__(self):
        self.data = list()

    def push(self, n):
        self.data.append(n)

    def pop(self):
        return self.data.pop() if self.data else None

    def peek(self):
        return self.data[-1] if self.data else None
