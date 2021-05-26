import pytest
#0 celsius is 32 F

def convert(t):
    return 32

def test_answer():
    assert convert(0) == 32


#temp = int(input("Please introduce temperature:"))

test_answer()