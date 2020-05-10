import numpy as np

# Basic utilities package for matrix operations

def get_numpy_version():
    """
    Gets the NumPy version in the current Python environment
    """
    return np.__version__
    

def add_matrices(a,b):
    """
    Adds two 2-D matrices a and b that must be of the same shape
    """

    # First, do some basic checks on shapes
    a_dim = len(a.shape)
    if a_dim != 2:
        raise SizeError("Matrix a must be of dimension 2, got dimension {}".format(a_dim))
    b_dim = len(b.shape)
    if b_dim != 2:
        raise SizeError("Matrix b must be of dimension 2, got dimension {}".format(b_dim))
    if not (a.shape == b.shape):
        raise SizeError("Matrices a {} and b {} must be of same size.".format(a.shape,b.shape))

    # If you made it past all the errors, add the matrices
    return a + b
    

class SizeError(Exception):
    """
    Custom exception type raised due to a shape mismatch in addition.
    We want to check that this specific type of exception is thrown 
    when testing on invalid input.
    """
    pass