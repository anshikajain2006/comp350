import pytest
from math import isclose, sqrt
from approximate_sqrt import approximate_sqrt  

def test_perfect_square():
    assert isclose(approximate_sqrt(4), 2.0, rel_tol=1e-5)
    assert isclose(approximate_sqrt(9), 3.0, rel_tol=1e-5)
    assert isclose(approximate_sqrt(1), 1.0, rel_tol=1e-5)

def test_non_perfect_square():
    assert isclose(approximate_sqrt(2), sqrt(2), rel_tol=1e-5)
    assert isclose(approximate_sqrt(10), sqrt(10), rel_tol=1e-5)
    assert isclose(approximate_sqrt(0.25), 0.5, rel_tol=1e-5)

def test_zero_input():
    assert isclose(approximate_sqrt(0), 0.0, rel_tol=1e-5)

def test_negative_input():
    with pytest.raises(ValueError, match="Cannot compute square root of a negative number."):
        approximate_sqrt(-1)
