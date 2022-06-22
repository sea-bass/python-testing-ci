import pytest
import numpy as np

# Test Case: Will fail with exact comparison due to numerical error
a = np.array([[0, 1, 2],
              [3, 4, 5],
              [6, 7, 8]])
b = np.array([[8, 7, 6],
              [5, 4, 3],
              [2, 1, 0]])
expected = np.array([[8, 8, 8],
                     [8, 8, 8],
                     [8, 8, 8]])

# Define test functions
def test_numpy_version():
    """
    Checks for the correct NumPy version as per specification
    """
    np_ver = np.__version__
    assert(np_ver == "1.22.4")
    print("Correct NumPy version found: " + np_ver)


def test_addition():
    """
    Tests the addition of 2 matrices by exact comparison
    """
    actual = a + b
    assert((expected == actual).all())
    print("Matrices are exactly equal")