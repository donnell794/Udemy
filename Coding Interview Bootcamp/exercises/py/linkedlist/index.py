# --- Directions
# Implement classes Node and Linked Lists
# See 'directions' document

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insertFirst(self, data):
        self.head = Node(data, self.head)

    def size(self):
        count = 0
        temp = self.head
        while(temp):
            count += 1
            temp = temp.next
        return count

    def getFirst(self):
        return self.head

    def getLast(self):
        if self.head is None:
            return None
        return self.getAt(self.size() - 1)

    def clear(self):
        self.head = None

    def removeFirst(self):
        if self.head:
            self.head = self.head.next
        else: return None

    def removeLast(self):
        if not self.head:
            return
        if self.head.next is None:
            self.clear()
        self.removeAt(self.size() - 1)

    def insertLast(self, data):
        temp = self.getLast()
        if temp:
            temp.next = Node(data)
        else: self.insertFirst(data)

    def getAt(self, n):
        count = 0
        temp = self.head
        while temp:
            if count == n:
                return temp
            count += 1
            temp = temp.next
        return None

    def removeAt(self, n):
        if not self.head:
            return
        if n == 0:
            self.head = self.head.next
        prev = self.getAt(n - 1)
        if not prev or not prev.next:
            return
        prev.next = prev.next.next

    def insertAt(self, data, n):
        if not self.head or n == 0:
            self.insertFirst(data)
            return
        prev = self.getAt(n - 1)
        prev = prev if prev else self.getLast()
        node = Node(data, prev.next)
        prev.next = node

    def __iter__(self):
        node = self.head
        while(node):
            yield node
            node = node.next

    def __next__(self):
        if self.next is None:
            raise StopIteration
        else: return self.next
