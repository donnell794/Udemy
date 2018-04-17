from index import Queue
from inspect import isclass
import pytest

def test_one():
    assert isclass(Queue)

def test_two():
    q = Queue()
    try:
        q.add(1)
    except:
        pytest.fail('could not add to queue')

def test_three():
    q = Queue()
    try:
        q.add(1)
        q.remove()
    except:
        pytest.fail('could not remove element from queue')

def test_four():
    q = Queue()
    q.add(1)
    q.add(2)
    q.add(3)
    assert q.remove() == 1
    assert q.remove() == 2
    assert q.remove() == 3
    assert q.remove() == None

def test_five():
    q = Queue()
    q.add(1)
    q.add(2)
    assert(q.peek()) == 1
    assert(q.peek()) == 1
    assert(q.remove()) == 1
    assert(q.remove()) == 2
