from index import *
from inspect import isfunction

def test_one():
    assert isfunction(capitalize)

def test_two():
    assert capitalize('hi there, how is it going?') == 'Hi There, How Is It Going?'

def test_three():
    assert capitalize('i love breakfast at bill miller bbq') == 'I Love Breakfast At Bill Miller Bbq'
