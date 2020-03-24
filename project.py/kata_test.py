import pytest
from kata import Add

def test_empty_string():
    assert Add("") == 0