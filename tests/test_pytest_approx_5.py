# sample code for Pytest Approx vs. Numpy's `assert_allclose`


import pytest
import numpy as np


# A function that calculates the square root of a number
def calculate_square_root(x):
    return np.sqrt(x)


def test_pytest_approx():
    result = calculate_square_root(2)
    expected_result = 1.41421356

    assert result == pytest.approx(expected_result, rel=1e-5)


def test_numpy_assert_allclose():
    result = calculate_square_root(2)
    expected_result = 1.41421356

    np.testing.assert_allclose(result, expected_result, rtol=1e-5)
