# --- Directions
# Implement a 'peek' method in this Queue class.
# Peek should return the last element (the next
# one to be returned) from the queue *without*
# removing it.

class Queue:
    def __init__(self):
        self.data = list()

    def add(self, n):
        self.data.append(n)

    def remove(self):
        return self.data.pop(0) if self.data else None

    def peek(self):
        return self.data[0] if self.data else None
