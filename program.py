import pytest
#0 celsius is 32 F

def convert_c_to_f(t):
    answer = t * 9/5 + 32
    return answer

def test_answer():
    assert convert_c_to_f(0) == 32
    assert convert_c_to_f(5) != 32


#temp = int(input("Please introduce temperature:"))

test_answer()