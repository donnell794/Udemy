from index import *
from node import *
from inspect import isfunction

def test_one():
    assert isfunction(level_width)

def test_two():
    root = Node(0)
    root.add(1)
    root.add(2)
    root.add(3)
    root.children[0].add(4)
    root.children[2].add(5)

    assert level_width(root) == [1,3,2]

def test_three():
    root = Node(0)
    root.add(1)
    root.children[0].add(2)
    root.children[0].add(3)
    root.children[0].children[0].add(4)

    assert level_width(root) == [1,1,2,1]
