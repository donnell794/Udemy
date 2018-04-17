from index import *
from inspect import isfunction

def test_one():
    assert isfunction(palindrome)

def test_two():
    assert palindrome('aba') == True

def test_three():
    assert palindrome(' aba') == False

def test_four():
    assert palindrome('aba ') == False

def test_five():
    assert palindrome('greetings') == False

def test_six():
    assert palindrome('1000000001') == True

def test_seven():
    assert palindrome('Fish hsif') == False

def test_eight():
    assert palindrome('pennep') == True
