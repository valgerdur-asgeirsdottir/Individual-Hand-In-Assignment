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

def test_unknown_number_of_numbers():
    assert Add("3,4,5,6") == 18
    assert Add("4,5,10") == 19
    assert Add("20,51") == 71
    assert Add("9,10,13") == 32

def test_new_line_between_numbers():
    assert Add("3\n4,5,6") == 18
    assert Add("4\n5,10\n") == 19
    assert Add("20\n") == 20
    assert Add("9\n10\n13") == 32

def test_numbers_bigger_than_1000():
    assert Add("3,4002,999,6") == 1008
    assert Add("4,1001,1000") == 1004
    assert Add("20\n9000") == 20
    assert Add("9000,2000,1300") == 0