from index import *
from inspect import isfunction

def test_one():
    assert isfunction(matrix)

def test_two():
    m = matrix(2)
    assert len(m) == 2
    assert m[0] == [1, 2]
    assert m[1] == [4, 3]

def test_three():
    m = matrix(3)
    assert len(m) == 3
    assert m[0] == [1, 2, 3]
    assert m[1] == [8, 9, 4]
    assert m[2] == [7, 6, 5]

def test_four():
    m = matrix(4)
    assert len(m) == 4
    assert m[0] == [1, 2, 3, 4]
    assert m[1] == [12, 13, 14, 5]
    assert m[2] == [11, 16, 15, 6]
    assert m[3] == [10, 9, 8, 7]
