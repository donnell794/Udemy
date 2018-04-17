from index import *

arr = [100, -40, 500, -124, 0, 21, 7]

sorted_arr = [-124, -40, 0, 7, 21, 100, 500]

def test_one():
    assert bubble_sort(arr) == sorted_arr

def test_two():
    assert selection_sort(arr) == sorted_arr

def test_three():
    left = [1, 10]
    right = [2, 8, 12]

    assert merge(left, right) == [1, 2, 8, 10, 12]

def test_four():
    assert merge_sort(arr) == sorted_arr
