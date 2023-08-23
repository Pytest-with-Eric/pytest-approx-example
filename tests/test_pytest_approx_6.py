import pytest

def test_measurements():
    expected = {
        'length': 10.0,
        'temperature': 25.5,
        'pressure': 1013.25,
    }
    
    calculated = {
        'length': 10.0001,        # Slightly different due to calculations
        'temperature': 25.4999,   # Slightly different due to calculations
        'pressure': 1013.24,      # Slightly different due to calculations
    }
    
    tolerance = {
        'length': 0.01,           # Tolerance for length values
        'temperature': 0.05,      # Tolerance for temperature values
        'pressure': 0.1,          # Tolerance for pressure values
    }
    
    for key in expected:
        assert calculated[key] == pytest.approx(expected[key], abs=tolerance[key])
