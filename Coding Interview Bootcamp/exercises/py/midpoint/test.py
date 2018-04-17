from index import *
from linkedlist import *
from inspect import isfunction

def test_one():
    assert isfunction(midpoint)

def test_two():
    l = LinkedList()
    l.insertLast('a')
    l.insertLast('b')
    l.insertLast('c')

    assert midpoint(l).data == 'b'

def test_three():
    l = LinkedList()
    l.insertLast('a')
    l.insertLast('b')
    l.insertLast('c')
    l.insertLast('d')
    l.insertLast('e')

    assert midpoint(l).data == 'c'

def test_four():
    l = LinkedList()
    l.insertLast('a')
    l.insertLast('b')

    assert midpoint(l).data == 'a'

def test_five():
    l = LinkedList()
    l.insertLast('a')
    l.insertLast('b')
    l.insertLast('c')
    l.insertLast('d')

    assert midpoint(l).data == 'b'
