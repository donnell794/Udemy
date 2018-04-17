from index import *
from inspect import isfunction

def test_one():
    assert isfunction(max_char)

def test_two():
    assert max_char('a') == 'a'
    assert max_char('abcdefghijklmnaaaaa') == 'a'

def test_three():
    assert max_char('ab1c1d1e1f1g1') == '1'
