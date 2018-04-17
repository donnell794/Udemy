# --- Directions
# Create a stack data structure.  The stack
# should be a class with methods 'push', 'pop', and
# 'peek'.  Adding an element to the stack should
# store it until it is removed.
# --- Examples
#   const s = new Stack();
#   s.push(1);
#   s.push(2);
#   s.pop(); # returns 2
#   s.pop(); # returns 1

class Stack:
    def __init__(self):
        self.data = list()

    def push(self, n):
        self.data.append(n)

    def pop(self):
        return self.data.pop() if self.data else None

    def peek(self):
        return self.data[-1] if self.data else None
