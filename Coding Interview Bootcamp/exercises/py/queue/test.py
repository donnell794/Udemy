from index import *
from inspect import isclass
import pytest

def test_one():
    assert isclass(Queue)

def test_two():
    q = Queue()
    try:
        q.add(1)
    except:
        pytetst.fail("Could not add to Queue")

def test_three():
    q = Queue()
    try:
        q.add(1)
        q.remove()
    except:
        pytest.fail("Could not remove elements from queue")

def test_four():
    q = Queue()
    q.add(1)
    q.add(2)
    q.add(3)
    assert q.remove() == 1
    assert q.remove() == 2
    assert q.remove() == 3
    assert q.remove() == None
