from index import *
from linkedlist import *
from inspect import isfunction

def test_one():
    assert isfunction(circular)

def test_two():
    l = LinkedList()
    a = Node('a')
    b = Node('b')
    c = Node('c')

    l.head = a
    a.next = b
    b.next = c
    c.next = b

    assert circular(l) == True

def test_three():
    l = LinkedList()
    a = Node('a')
    b = Node('b')
    c = Node('c')

    l.head = a
    a.next = b
    b.next = c
    c.next = a

    assert circular(l) == True

def test_four():
    l = LinkedList()
    a = Node('a')
    b = Node('b')
    c = Node('c')

    l.head = a
    a.next = b
    b.next = c
    c.next = None

    assert circular(l) == False
