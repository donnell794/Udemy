from index import *
from linkedlist import *
from inspect import isfunction

def test_one():
    assert isfunction(from_last)

def test_two():
    l = LinkedList()
    l.insertLast('a')
    l.insertLast('b')
    l.insertLast('c')
    l.insertLast('d')
    l.insertLast('e')

    assert from_last(l, 3).data == 'b'
