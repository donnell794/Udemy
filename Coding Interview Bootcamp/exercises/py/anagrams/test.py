from index import *
from inspect import isfunction

def test_one():
    assert isfunction(anagrams)

def test_two():
    assert anagrams('hello', 'llohe') == True

def test_three():
    assert anagrams('Whoa! Hi!', 'Hi! Whoa!') == True

def test_four():
    assert anagrams('One One', 'Two two two') == False

def test_five():
    assert anagrams('One one', 'One one c') == False

def test_six():
    assert anagrams('A tree, a life, a bench', 'A tree, a fence, a yard') == False
