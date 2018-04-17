from index import *
from inspect import isfunction

def test_one():
    assert isfunction(vowels)

def test_two():
    assert vowels('aeiou') == 5

def test_three():
    assert vowels('AEIOU') == 5

def test_four():
    assert vowels('abcdefghijklmnopqrstuvwxyz') == 5

def test_five():
    assert vowels('bcdfghjkl') == 0
