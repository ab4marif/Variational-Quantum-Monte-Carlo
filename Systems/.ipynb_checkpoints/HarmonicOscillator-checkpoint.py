import numpy as np

alpha = np.array([0.4, 0.45, 0.5, 0.55, 0.6])
dimension = 1

def trialWaveFunction(alpha, r):
    return np.exp(-alpha*r**2 )


def E_loc(alpha, r):
    return alpha + (0.5-2*alpha**2)*r**(2)

def dWaveFunction(r):
    return -r**2