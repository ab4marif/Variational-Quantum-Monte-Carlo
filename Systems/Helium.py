import numpy as np
""" This file contains the System information about the Helium atom.
"""

alpha = np.arange(0.05, 0.25, 0.025)
dimension = 6

def trialWaveFunction(alpha, r):
    """ Trail wave function of the Helium atom.

    Parameters
    ----------
    alpha:          int; parameter of the trail wave function to be varied
    r:              position of the electron orbiting the atom.
                    dim = (N_walkers, 6), where N_walkers are the number of walkers
                    6 is taken as the dimension of the system. Then the first 3 dimensions are the 1st electron
                    r[:,:3] = 1st electron
                    r[:,3:] = 2nd electron



    Returns:
    --------
    Trail wave function with 3 variables

    """
    r1 = np.linalg.norm(r[:,:3], axis = 1, keepdims = True)
    r2 = np.linalg.norm(r[:,3:], axis = 1, keepdims = True)
    r12 =  np.linalg.norm(r[:, :3]-r[:, 3:], axis = 1, keepdims = True)

    wf = np.exp(-2*r1)*np.exp(-2*r2)*np.exp(r12/(2*(1+alpha*r12)))
    return wf

def E_loc(alpha, r):
    """ Local Energy of the Helium atom.

    Parameters
    ----------
    alpha:          int; parameter of the trail wave function to be varied
    r:              position of the electron orbiting the atom.
                    dim = (N_tries, N_walkers, 6), where N_walkers are the number of walkers, N_tries are number of steps taken
                    6 is taken as the dimension of the system.
                    r[:,:3] = 1st electron
                    r[:,3:] = 2nd electron



    Returns:
    --------
    E_loc:          local energy for the positions of the electrons

    """
    r1_unit = r[:,:3] / np.linalg.norm(r[:, :3], axis = 1, keepdims = True)

    r2_unit = r[:,3:] / np.linalg.norm(r[:, 3:], axis = 1, keepdims = True)
    r12_unit = r1_unit - r2_unit
    r12 = np.linalg.norm(r[:, :3] - r[:, 3:], axis = 1, keepdims = True)

    E_loc = -4 + np.sum(r12_unit * (r[:, :3] - r[:, 3:]), axis = 1, keepdims = True) * 1/(r12*(1+alpha*r12)**2) - 1/(r12*(1+alpha*r12)**3) - 1/(4*(1+alpha*r12)**4) + 1/r12
    return E_loc


def dWaveFunction(alpha, r):
    """ he derivative of the natural logarithm of the trail wave function. Needed for the minimal alpha finder.

    Parameters
    ----------
    alpha:          int; parameter of the trail wave function to be varied
    r:              position of the electron orbiting the atom.
                    dim = (N_walkers, 6), where N_walkers are the number of walkers
                    6 is taken as the dimension of the system. Then the first 3 dimensions are the 1st electron
                    r[:,:3] = 1st electron
                    r[:,3:] = 2nd electron



    Returns:
    --------
    dwf:          r12**2/(-2*(1 + alpha*r12)**2)

    """
    r12 =  np.linalg.norm(r[:, :3]-r[:, 3:], axis = 1, keepdims = True)
    dwf = r12**2/(-2*(1 + alpha*r12)**2)
    return dwf
