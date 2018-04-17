from index import *
from inspect import isfunction

def test_one():
    #reverse_int function exists
    assert isfunction(reverse_int)

def test_two():
    #reverse_int handles 0 as input
    assert reverse_int(0) == 0

def test_three():
    #reverse_int flips a positive number
    assert reverse_int(5) == 5
    assert reverse_int(15) == 51
    assert reverse_int(90) == 9
    assert reverse_int(2359) == 9532

def test_four():
    #reverse_int flips a negative number
    assert reverse_int(-5) == -5
    assert reverse_int(-15) == -51
    assert reverse_int(-90) == -9
    assert reverse_int(-2359) == -9532
