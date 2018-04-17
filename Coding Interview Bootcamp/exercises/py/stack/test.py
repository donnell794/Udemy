from index import *
from inspect import isclass

def test_one():
    assert isclass(Stack)

def test_two():
    s = Stack()
    s.push(1)
    assert(s.pop()) == 1
    s.push(2)
    assert(s.pop()) == 2

def test_three():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    assert(s.pop()) == 3
    assert(s.pop()) == 2
    assert(s.pop()) == 1

def test_four():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    assert(s.peek()) == 3
    assert(s.pop()) == 3
    assert(s.peek()) == 2
    assert(s.pop()) == 2
    assert(s.peek()) == 1
    assert(s.pop()) == 1
