"""
Code for the section handling Complex Data Structures with Pytest Approx

Approximating Lists and Arrays
"""
import pytest
import numpy as np


# Function to calculate the element-wise square of a list or array
def calculate_square_elements(data):
    return [x**2 for x in data]


def test_list_comparison():
    expected_result = [1, 4, 9, 16]
    input_data = [1, 2, 3, 4]
    calculated_result = calculate_square_elements(input_data)

    assert calculated_result == pytest.approx(expected_result)


def test_numpy_array_comparison():
    expected_result = np.array([0.1, 0.2, 0.3])
    input_data = np.array([0.31622776601683794, 0.4472135954999579, 0.5477225575051661])
    calculated_result = calculate_square_elements(input_data)

    assert calculated_result == pytest.approx(expected_result, abs=1e-6)
