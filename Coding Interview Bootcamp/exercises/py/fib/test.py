from index import *
from inspect import isfunction

def test_one():
    assert isfunction(fib)

def test_two():
    assert fib(1) == 1

def test_three():
    assert fib(2) == 1

def test_four():
    assert fib(3) == 2

def test_five():
    assert fib(4) == 3

def test_six():
    assert fib(39) == 63245986
