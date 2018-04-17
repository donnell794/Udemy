from index import *
from inspect import isfunction
import sys

def test_one():
    assert isfunction(fizzbuzz)

def test_two(capsys):
    fizzbuzz(5)
    out,err = capsys.readouterr()
    #sys.stdout.write(out)
    #words = out.split()
    output = [x.strip('\n') for x in out.split()]
    #words = lambda x: x.strip('\n'), words
    assert len(output) == 5

def test_three(capsys):
    fizzbuzz(15)
    out,err = capsys.readouterr()
    #sys.stdout.write(out)
    output = [x.strip('\n') for x in out.split()]
    output = [int(x) if x.isdigit() else x for x in output]
    print(output)
    assert output[0] == 1
    assert output[1] == 2
    assert output[2] == 'fizz'
    assert output[3] == 4
    assert output[4] == 'buzz'
    assert output[5] == 'fizz'
    assert output[6] == 7
    assert output[7] == 8
    assert output[8] == 'fizz'
    assert output[9] == 'buzz'
    assert output[10] == 11
    assert output[11] == 'fizz'
    assert output[12] == 13
    assert output[13] == 14
    assert output[14] == 'fizzbuzz'
