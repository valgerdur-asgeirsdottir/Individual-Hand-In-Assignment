import pytest
from kata import Add

def test_empty_string():
    assert Add("") == 0
    assert Add("3") == 3
    assert Add("4") == 4
    assert Add("25") == 25
    assert Add("60") == 60
