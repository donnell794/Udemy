from index import *
from inspect import isfunction
import sys

def test_one():
    assert isfunction(steps)

def test_two(capsys):
    steps(1)
    out, err = capsys.readouterr()
    #sys.stdout.write(out)
    output = [x for x in out.split('\n')]
    assert output[0] == '#'
    assert len(output) == 1

def test_three(capsys):
    steps(2)
    out, err = capsys.readouterr()
    #sys.stdout.write(out)
    output = [x for x in out.split('\n')]
    output.pop()
    assert output[0] == '# '
    assert output[1] == '##'
    assert len(output) == 2

def test_four(capsys):
    steps(3)
    out, err = capsys.readouterr()
    #print(out.split('\n'))
    sys.stdout.write(out)
    output = [x for x in out.split('\n')]
    output.pop()
    print(output)
    assert output[0] == '#  '
    assert output[1] == '## '
    assert output[2] == '###'
    assert len(output) == 3
