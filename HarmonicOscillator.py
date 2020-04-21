import numpy as np

def trialWaveFunction(alpha, r):
    return np.exp(-alpha*r**2)


def E_loc(alpha, r):
    return alpha + (0.5-2*alpha**2)*r**(2)
