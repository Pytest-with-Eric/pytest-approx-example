## Different Approaches to Approximation 
import pytest
@pytest.mark.xfail(reason="This test is currently expected to fail")
def test_approx_syntax():
    # Test case 1: Using default tolerance
    actual_value_1 = 10.5
    expected_value_1 = 10.0
    assert actual_value_1 == pytest.approx(expected_value_1)

## These test cases will pass

def test_rel_tol():
    # Test case 2: Using relative tolerance
    actual_value_2 = 200.0
    expected_value_2 = 205.0
    assert actual_value_2 == pytest.approx(expected_value_2, rel=0.2)

def test_abs_tol():
    # Test case 3: Using absolute tolerance
    actual_value_3 = 15.0
    expected_value_3 = 15.5
    assert actual_value_3 == pytest.approx(expected_value_3, abs=0.6)

def test_NaN_val():
    # Test case 4: Handling NaN values
    nan_value = float("nan")
    assert nan_value == pytest.approx(nan_value, nan_ok=True)

def test_custom_error():
    # Test case 5: Using custom error message
    actual_value_5 = 3.14159
    expected_value_5 = 3.14
    assert actual_value_5 == pytest.approx(expected_value_5, abs=0.01), "Values not approximately equal"

# Define a custom function that performs a scaling operation
def scale_value(value, factor):
    return value * factor

def test_scaling_factors():
    # Test case 6: Using a scaling factor
    original_value = 5.0
    scaling_factor = 2.0
    scaled_value = scale_value(original_value, scaling_factor)

    assert scaled_value == pytest.approx(original_value, rel=scaling_factor - 1)
