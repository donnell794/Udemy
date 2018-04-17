from index import *
from inspect import isfunction

def test_one():
    assert isfunction(chunk)

def test_two():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    chunked = chunk(arr, 2)
    assert chunked == [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]

def test_three():
    arr = [1, 2, 3]
    chunked = chunk(arr, 1)
    assert chunked == [[1], [2], [3]]

def test_four():
    arr = [1, 2, 3, 4, 5]
    chunked = chunk(arr, 3)
    assert chunked == [[1, 2, 3], [4, 5]]

def test_five():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    chunked = chunk(arr, 5)
    assert chunked == [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13]]
