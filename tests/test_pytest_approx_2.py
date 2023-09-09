## Different Approaches to Approximation 
import pytest
@pytest.mark.xfail(reason="This test is currently expected to fail")
def test_approx_syntax():
    # Test case 1: Using default tolerance
    actual_value_1 = 10.5
    expected_value_1 = 10.0
    assert actual_value_1 == pytest.approx(expected_value_1)

## These test cases will pass

def test_approximate():
    # Test case 2: Using relative tolerance
    actual_value_2 = 200.0
    expected_value_2 = 205.0
    assert actual_value_2 == pytest.approx(expected_value_2, rel=0.2)

    # Test case 3: Using absolute tolerance
    actual_value_3 = 15.0
    expected_value_3 = 15.5
    assert actual_value_3 == pytest.approx(expected_value_3, abs=0.6)

    # Test case 4: Handling NaN values
    nan_value = float("nan")
    assert nan_value == pytest.approx(nan_value, nan_ok=True)

    # Test case 5: Using custom error message
    actual_value_5 = 3.14159
    expected_value_5 = 3.14
    assert actual_value_5 == pytest.approx(expected_value_5, abs=0.01, msg="Values not approximately equal")
