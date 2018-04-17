from index import *
from node import *

def test_one():
    n = Node(10)
    n.insert(5)
    n.insert(15)
    n.insert(0)
    n.insert(20)

    assert validate(n) == True

def test_two():
    n = Node(10)
    n.insert(5)
    n.insert(15)
    n.insert(0)
    n.insert(20)
    n.left.left.right = Node(999)

    assert validate(n) == False
