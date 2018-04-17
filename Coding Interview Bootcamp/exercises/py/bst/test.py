from index import *
from inspect import isclass

def test_one():
    assert isclass(Node)

def test_two():
    node = Node(10)
    node.insert(5)
    node.insert(15)
    node.insert(17)

    assert node.left.data == 5
    assert node.right.data == 15
    assert node.right.right.data == 17

def test_three():
    node = Node(10)
    node.insert(5)
    node.insert(15)
    node.insert(20)
    node.insert(0)
    node.insert(-5)
    node.insert(3)

    three = node.left.left.right

    assert node.contains(3) == three

def test_four():
    node = Node(10)
    node.insert(5)
    node.insert(15)
    node.insert(20)
    node.insert(0)
    node.insert(-5)
    node.insert(3)
    assert node.contains(9999) == None
