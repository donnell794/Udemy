from index import *
from inspect import isfunction

def test_one():
    #reverse function exists
    assert isfunction(reverse)

def test_two():
    #Reverse reverses a string
    assert reverse('abcd') == 'dcba'

def test_three():
    #Reverse reverses a string
    assert reverse('  abcd') == 'dcba  '
