import pytest


@pytest.mark.set1
def test_file1_method1():
    """set 1 test."""
    x = 5
    y = 6
    assert x+1 == y, "test failed"
    assert x == y, "test failed"


@pytest.mark.set2
def test_file1_method2():
    """set 2 test."""
    x = 5
    y = 6
    assert x+1 == y, "test failed"