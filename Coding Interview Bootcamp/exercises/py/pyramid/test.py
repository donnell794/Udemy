from index import *
from inspect import isfunction
import sys

def test_one():
    assert isfunction(pyramid)

def test_two(capsys):
    pyramid(2)
    out, err = capsys.readouterr()
    #sys.stdout.write(out)
    output = [x for x in out.split('\n')]
    output.pop()
    assert output[0] == ' # '
    assert output[1] == '###'
    assert len(output) == 2


def test_three(capsys):
    pyramid(3)
    out, err = capsys.readouterr()
    #sys.stdout.write(out)
    output = [x for x in out.split('\n')]
    output.pop()
    assert output[0] == '  #  '
    assert output[1] == ' ### '
    assert output[2] == '#####'
    assert len(output) == 3

def test_four(capsys):
    pyramid(4)
    out, err = capsys.readouterr()
    sys.stdout.write(out)
    output = [x for x in out.split('\n')]
    output.pop()
    print(output)
    assert output[0] == '   #   '
    assert output[1] == '  ###  '
    assert output[2] == ' ##### '
    assert output[3] == '#######'
    assert len(output) == 4
