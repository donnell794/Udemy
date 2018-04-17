from index import *
from queue import *
from inspect import ismethod, isfunction
import pytest

def test_one():
    q = Queue()
    assert ismethod(q.peek)

def test_two():
    q = Queue()
    q.add(1)
    q.add(2)
    assert q.peek() == 1
    assert q.peek() == 1
    assert q.remove() == 1
    assert q.remove() == 2

def test_three():
    assert isfunction(weave)

def test_four():
    one = Queue()
    one.add(1)
    one.add(2)
    one.add(3)
    one.add(4)

    two = Queue()
    two.add('one')
    two.add('two')
    two.add('three')
    two.add('four')

    result = weave(one, two)
    assert result.remove() == 1
    assert result.remove() == 'one'
    assert result.remove() == 2
    assert result.remove() ==  'two'
    assert result.remove() == 3
    assert result.remove() == 'three'
    assert result.remove() == 4
    assert result.remove() == 'four'
    assert result.remove() == None
