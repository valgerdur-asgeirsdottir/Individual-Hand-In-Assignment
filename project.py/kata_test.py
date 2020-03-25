import pytest
from kata import Add
from kata import NegativeNumbersException

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

def test_negatives_are_not_allowed():
    with pytest.raises(NegativeNumbersException) as excinfo:
        Add("-1,2,-3,4")

    assert "Negatives not allowed: -1 -3 " == str(excinfo.value)

    with pytest.raises(NegativeNumbersException) as excinfo:
        Add("1\n2,-3,-4")

    assert "Negatives not allowed: -3 -4 " == str(excinfo.value)

    with pytest.raises(NegativeNumbersException) as excinfo:
        Add("-100\n-2,9999,-10")

    assert "Negatives not allowed: -100 -2 -10 " == str(excinfo.value)

def test_different_delimiter():
    assert Add("//X\n1X2") == 3
    assert Add("//%\n1%2%3") == 6
    assert Add("//[delimiter]\n") == 0