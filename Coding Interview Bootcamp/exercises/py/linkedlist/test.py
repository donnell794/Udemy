from index import *
from inspect import isclass
import pytest

def test_one():
    assert isclass(LinkedList)

def test_two():
    assert isclass(Node)

def test_three():
    node = Node('a', 'b')
    assert node.data == 'a'
    assert node.next == 'b'

def test_four():
    l = LinkedList()
    l.insertFirst(1)
    assert l.head.data == 1
    l.insertFirst(2)
    assert l.head.data == 2

def test_five():
    l = LinkedList()
    assert l.size() == 0
    l.insertFirst(1)
    l.insertFirst(1)
    l.insertFirst(1)
    l.insertFirst(1)
    assert l.size() == 4

def test_six():
    l = LinkedList()
    l.insertFirst(1)
    assert l.getFirst().data == 1
    l.insertFirst(2)
    assert l.getFirst().data == 2

def test_seven():
    l = LinkedList()
    l.insertFirst(2)
    assert l.getLast().data == 2 and  l.getLast().next is None
    l.insertFirst(1)
    assert l.getLast().data == 2 and  l.getLast().next is None

def test_eight():
    l = LinkedList()
    assert l.size() == 0
    l.insertFirst(1)
    l.insertFirst(1)
    l.insertFirst(1)
    l.insertFirst(1)
    assert l.size() == 4
    l.clear()
    assert l.size() == 0

def test_nine():
    l = LinkedList()
    l.insertFirst('a')
    l.removeFirst()
    assert l.size() == 0
    assert l.getFirst() == None

def test_ten():
    l = LinkedList()
    l.insertFirst('c')
    l.insertFirst('b')
    l.insertFirst('a')
    l.removeFirst()
    assert l.size() == 2
    l.getFirst().data == 'b'
    l.removeFirst()
    assert l.size() == 1
    l.getFirst().data == 'c'

def test_eleven():
    l = LinkedList()
    try:
        l.removeLast()
    except:
        pytest.fail('cannot remove last node when list is empty')

def test_twelve():
    l = LinkedList()
    l.insertFirst('a')
    l.removeLast()
    assert l.head is None

def test_thirteen():
    l = LinkedList()
    l.insertFirst('b')
    l.insertFirst('a')
    l.removeLast()
    assert l.size() == 1
    assert l.head.data == 'a'

def test_fourteen():
    l = LinkedList()
    l.insertFirst('c')
    l.insertFirst('b')
    l.insertFirst('a')
    l.removeLast()
    assert l.size() == 2
    assert l.getLast().data == 'b'

def test_fifteen():
    l = LinkedList()
    l.insertFirst('a')
    l.insertLast('b')
    assert l.size() == 2
    assert l.getLast().data == 'b'

def test_sixteen():
    l = LinkedList()
    assert l.getAt(10) == None
    l.insertLast(1)
    l.insertLast(2)
    l.insertLast(3)
    l.insertLast(4)

    assert l.getAt(0).data == 1
    assert l.getAt(1).data == 2
    assert l.getAt(2).data == 3
    assert l.getAt(3).data == 4

def test_seventeen():
    l = LinkedList()
    try:
        l.removeAt(0)
        l.removeAt(1)
        l.removeAt(2)
    except:
        pytest.fail("removeAt crash empty list")

def test_eighteen():
    l = LinkedList()
    try:
        l.insertFirst('a')
        l.removeAt(1)
    except:
        pytest.fail('removeAt is out of bounds')

def test_nineteen():
    l = LinkedList()
    l.insertLast(1)
    l.insertLast(2)
    l.insertLast(3)
    l.insertLast(4)
    assert l.getAt(0).data == 1
    l.removeAt(0)
    assert l.getAt(0).data == 2

def test_twenty():
    l = LinkedList()
    l.insertLast(1)
    l.insertLast(2)
    l.insertLast(3)
    l.insertLast(4)
    assert l.getAt(1).data == 2
    l.removeAt(1)
    assert l.getAt(1).data == 3

def test_twentyone():
    l = LinkedList()
    l.insertLast(1)
    l.insertLast(2)
    l.insertLast(3)
    l.insertLast(4)
    assert l.getAt(3).data == 4
    l.removeAt(3)
    assert l.getAt(3) == None

def test_twentytwo():
    l = LinkedList()
    l.insertAt('hi', 0)
    assert l.getFirst().data == 'hi'

def test_twentythree():
    l = LinkedList()
    l.insertLast('a')
    l.insertLast('b')
    l.insertLast('c')
    l.insertAt('hi', 0)
    assert l.getAt(0).data == 'hi'
    assert l.getAt(1).data == 'a'
    assert l.getAt(2).data == 'b'
    assert l.getAt(3).data == 'c'

def test_twentyfour():
    l = LinkedList()
    l.insertLast('a')
    l.insertLast('b')
    l.insertAt('hi', 2)
    assert l.getAt(0).data == 'a'
    assert l.getAt(1).data == 'b'
    assert l.getAt(2).data == 'hi'

def test_twentyfive():
    l = LinkedList()
    l.insertLast('a')
    l.insertLast('b')
    l.insertAt('hi', 30)
    assert l.getAt(0).data == 'a'
    assert l.getAt(1).data == 'b'
    assert l.getAt(2).data == 'hi'

def test_twentysix():
    l = LinkedList()
    l.insertLast(1)
    l.insertLast(2)
    l.insertLast(3)
    l.insertLast(4)

    for node in iter(l):
        node.data += 10

    assert l.getAt(0).data == 11
    assert l.getAt(1).data == 12
    assert l.getAt(2).data == 13
    assert l.getAt(3).data == 14

def test_twentyseven():
    l = LinkedList()
    try:
        for node in iter(l):
            pass
    except:
        pytest.fail('cant iter over empty list')
