## sample code for `approx` and `assert_approx_equal`

import pytest
import numpy as np


def divide(a, b):
    return a / b


def test_pytest_approx():
    result = divide(1, 3)
    assert result == pytest.approx(0.3333333333333333)


def test_assert_approx_equal():
    result = divide(1, 3)
    np.testing.assert_approx_equal(result, 0.3333333333333333, significant=6)


# if __name__ == "__main__":
#     pytest.main()
