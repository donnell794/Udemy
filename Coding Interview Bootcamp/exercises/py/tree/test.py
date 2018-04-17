from index import *
from inspect import isclass

def test_one():
    assert isclass(Node)

def test_two():
    n = Node('a')
    assert n.data == 'a'
    assert len(n.children) == 0

def test_three():
    n = Node('a')
    n.add('b')
    assert len(n.children) == 1
    n.remove('b')
    assert len(n.children) == 0

def test_four():
    t = Tree()
    assert t.root is None

def test_five():
    letters = list()
    t = Tree()
    t.root = Node('a')
    t.root.add('b')
    t.root.add('c')
    t.root.children[0].add('d')

    t.traverseBF(lambda node: letters.append(node.data))

    assert letters == ['a', 'b', 'c', 'd']

def test_six():
    letters = list()
    t = Tree()
    t.root = Node('a')
    t.root.add('b')
    t.root.add('d')
    t.root.children[0].add('c')
    print(t)
    t.traverseDF(lambda node: letters.append(node.data))

    assert letters == ['a', 'b', 'c', 'd']
