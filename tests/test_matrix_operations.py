import numpy as np

# Test Case: Will fail with exact comparison due to numerical error
a = np.array([[0, 1, 2],
              [3, 4, 5],
              [6, 7, 8]])
b = np.array([[3*0.1, 2,  3],
              [0,     0,  0],
              [-1,   -2, -3]])
expected = np.array([[0.3, 3, 5],
                     [3,   4, 5],
                     [5,   5, 5]])

# Define test functions
def test_numpy_version():
    """
    Checks for the correct NumPy version as per specification
    """
    np_ver = np.__version__
    assert(np_ver == "1.17.0")
    print("Correct NumPy version found: " + np_ver)

# def test_addition_exact():
#     """
#     Tests the addition of 2 matrices by exact comparison
#     """
#     actual = a + b
#     assert((expected == actual).all())
#     print("Matrices are exactly equal")

def test_addition_close():
    """
    Tests the addition of 2 matrices by checking if they are close within some tolerance
    """
    actual = a + b
    assert(np.allclose(actual,expected,rtol=1e-05,atol=1e-08))
    print("Matrices are equal within specified tolerance")