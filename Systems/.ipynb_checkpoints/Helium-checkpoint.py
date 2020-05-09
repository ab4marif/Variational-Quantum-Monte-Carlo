import numpy as np
""" This file contains the System information about the Helium atom.
"""

# alpha values to compare with Jos Thijsen
alpha_jos = np.arange(0.05, 0.25, 0.025)

# broader range of alphas to plot
alpha_broad = np.arange(0.05, 0.25, 0.015)

dimension = 6

def trial_wave_function(alpha, r):
    """ Trail wave function of the Helium atom.

    Parameters
    ----------
    alpha:          int; parameter of the trail wave function to be varied
    r:              matrix of shape (N_tries*N_walkers-N_walkers*4000) x 6
                     N_tries , number of steps
                     N_walkers , number of walkers
                     :3 x (N*n_walkers-n_walkers*4000) , distance between proton and electron 1
                     3: x (N*n_walkers-n_walkers*4000) , distance between proton and electron 2



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
    r:              matrix of shape (N_tries*N_walkers-N_walkers*4000) x 6
                     N_tries , number of steps
                     N_walkers , number of walkers
                     :3 x (N*n_walkers-n_walkers*4000) , distance between proton and electron 1
                     3: x (N*n_walkers-n_walkers*4000) , distance between proton and electron 2



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


def deriv_wave_function(alpha, r):
    """ The derivative of the natural logarithm of the trail wave function with respec to alpha.
        Needed for the optimal alpha finder.

    Parameters
    ----------
    alpha:          int; parameter of the trail wave function to be varied
    r:              matrix of shape (N_tries*N_walkers-N_walkers*4000) x 6
                     N_tries , number of steps
                     N_walkers , number of walkers
                     :3 x (N*n_walkers-n_walkers*4000) , distance between proton and electron 1
                     3: x (N*n_walkers-n_walkers*4000) , distance between proton and electron 2



    Returns:
    --------
    dwf:          r12**2/(-2*(1 + alpha*r12)**2)

    """
    r12 =  np.linalg.norm(r[:, :3]-r[:, 3:], axis = 1, keepdims = True)
    dwf = r12**2/(-2*(1 + alpha*r12)**2)
    return dwf
