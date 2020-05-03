import numpy as np
""" This file contains the System information about the Hydrogen atom.
"""

alpha = np.array([0.8, 0.9, 1, 1.1, 1.2])
dimension = 3

def trialWaveFunction(alpha, r):
    """ Trail wave function of the Hydrogen atom.

    Parameters
    ----------
    alpha:          int; parameter of the trail wave function to be varied
    r:              numpy array of the position of the electron orbiting the atom


    Returns:
    --------
    np.exp(-alpha*r)
    """
    r = np.linalg.norm(r, axis = 1, keepdims = True)
    return np.exp(-alpha*r)

def E_loc(alpha, r):
    """ Local Energy of the Hydrogen atom.

    Parameters
    ----------
    alpha:          int; parameter of the trail wave function to be varied
    r:              numpy array of the position of the electron orbiting the atom


    Returns:
    --------
    -1/r - 0.5*alpha*(alpha -2/r)
    """
    r = np.linalg.norm(r, axis = 1, keepdims = True)
    return (-1/r - 0.5*alpha*(alpha -2/r))

def dWaveFunction(r):
    """ The derivative of the natural logarithm of the trail wave function. Needed for the minimal alpha finder.

    Parameters
    ----------
    r:              numpy array of the position of the electron orbiting the atom

    Returns:
    --------
    -r

    """
    r = np.linalg.norm(r, axis = 1, keepdims = True)
    return -r

