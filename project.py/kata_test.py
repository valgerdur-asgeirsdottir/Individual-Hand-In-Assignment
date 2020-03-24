import pytest
from kata import Add

def test_empty_string():
    assert Add("") == 0

def test_single_number():
    assert Add("3") == 3
    assert Add("4") == 4
    assert Add("25") == 25
    assert Add("60") == 60

def test_two_numbers():
    assert Add("3,4") == 7
    assert Add("4,5") == 9
    assert Add("2,5") == 7
    assert Add("6,0") == 6