import pytest
import numpy as np

# Define inputs and expected outputs
# Test Case 0: Will pass with exact comparison
a0 = np.array([[0, 1, 2],
               [3, 4, 5],
               [6, 7, 8]])
b0 = np.array([[8, 7, 6],
               [5, 4, 3],
               [2, 1, 0]])
expected0 = np.array([[8, 8, 8],
                      [8, 8, 8],
                      [8, 8, 8]])

# Test Case 1: Will fail with exact comparison due to numerical error
a1 = np.array([[0, 1, 2],
               [3, 4, 5],
               [6, 7, 8]])
b1 = np.array([[3*0.1, 2,  3],
               [0,     0,  0],
               [-1,   -2, -3]])
expected1 = np.array([[0.3, 3, 5],
                      [3,   4, 5],
                      [5,   5, 5]])

# Define test functions
def test_numpy_version():
    """
    Checks for the correct NumPy version as per specification
    """
    np_ver = np.__version__
    assert(np_ver == "1.22.4")
    print("Correct NumPy version found: " + np_ver)


@pytest.mark.skip(reason="Not using exact matrix comparison")
@pytest.mark.parametrize("a,b,expected",[(a0,b0,expected0),(a1,b1,expected1)])
def test_addition_exact(a,b,expected):
    """
    Tests the addition of 2 matrices by exact comparison
    """
    actual = a + b
    assert((expected == actual).all())
    print("Matrices are exactly equal")


@pytest.mark.parametrize("a,b,expected",[(a0,b0,expected0),(a1,b1,expected1)])
def test_addition_close(a,b,expected):
    """
    Tests the addition of 2 matrices by checking if they are close within some tolerance
    """
    actual = a + b
    assert(np.allclose(actual,expected,rtol=1e-05,atol=1e-08))
    print("Matrices are equal within specified tolerance")