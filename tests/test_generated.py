import pytest
from sample_app.sample_app import divide

def test_divide_positive_numbers():
    assert divide(10, 2) == 5
    assert divide(6, 3) == 2

def test_divide_negative_numbers():
    assert divide(-10, -2) == 5
    assert divide(-6, 3) == -2

def test_divide_mixed_sign_numbers():
    assert divide(10, -2) == -5
    assert divide(-10, 2) == -5

def test_divide_zero_numerator():
    assert divide(0, 5) == 0
    assert divide(0, -5) == 0

def test_divide_by_one():
    assert divide(5, 1) == 5
    assert divide(-5, 1) == -5
    assert divide(5, -1) == -5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
    with pytest.raises(ZeroDivisionError):
        divide(-5, 0)
    with pytest.raises(ZeroDivisionError):
        divide(0, 0)

def test_divide_large_numbers():
    assert divide(1_000_000, 2) == 500_000
    assert divide(-1_000_000, -2) == 500_000

def test_divide_edge_case_large_divisor():
    assert divide(5, 1_000_000) == 5e-06
    assert divide(-5, 1_000_000) == -5e-06

def test_divide_float_numbers():
    assert divide(5.0, 2.5) == 2.0
    assert divide(-10.0, 2.0) == -5.0