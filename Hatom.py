import numpy as np

alpha = np.array([0.8, 0.9, 1, 1.1, 1.2])
dimension = 3

def trialWaveFunction(alpha, r):
    r = np.linalg.norm(r, axis = 1, keepdims = True)
    return np.exp(-alpha*r)

def E_loc(alpha, r):

    r = np.linalg.norm(r, axis = 1, keepdims = True)
    return (-1/r - 0.5*alpha*(alpha -2/r))
