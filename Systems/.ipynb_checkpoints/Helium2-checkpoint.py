import numpy as np

""" This file contains the System information about the Helium atom with 2 variational parameters alpha and beta.
    This file can only be used with optimal_energy_helium_2_parameters.py file
"""

dimension = 6

def trial_wave_function(alpha, beta, r):
    """ Trail wave function of the Helium atom.

    Parameters
    ----------
    alpha:          int; parameter of the trail wave function to be varied
    beta:           int; parameter of the trail wave function to be varied
    r:              matrix of shape (N_tries*N_walkers-N_walkers*4000) x 6
                     N_tries , number of steps
                     N_walkers , number of walkers
                     :3 x (N*n_walkers-n_walkers*4000) , distance between proton and electron 1
                     3: x (N*n_walkers-n_walkers*4000) , distance between proton and electron 2



    Returns:
    --------
    Trail wave function with 4 variables

    """
    r1 = np.linalg.norm(r[:,:3], axis = 1, keepdims = True)
    r2 = np.linalg.norm(r[:,3:], axis = 1, keepdims = True)
    r12 =  np.linalg.norm(r[:, :3]-r[:, 3:], axis = 1, keepdims = True)

    wf = np.exp(-beta*(r1 + r2))*np.exp(r12/(2*(1+alpha*r12)))
    return wf

def E_loc(alpha, beta, r):
    """ Local Energy of the Helium atom.

    Parameters
    ----------
    alpha:          int; parameter of the trail wave function to be varied
    beta:           int; parameter of the trail wave function to be varied
    r:              matrix of shape (N_tries*N_walkers-N_walkers*4000) x 6
                     N_tries , number of steps
                     N_walkers , number of walkers
                     :3 x (N*n_walkers-n_walkers*4000) , distance between proton and electron 1
                     3: x (N*n_walkers-n_walkers*4000) , distance between proton and electron 2



    Returns:
    --------
    E_loc:          local energy for the positions of the electrons

    """

    # for helium Z = 2
    Z = 2

    r1 = np.linalg.norm(r[:,:3], axis = 1, keepdims = True)
    r2 = np.linalg.norm(r[:,3:], axis = 1, keepdims = True)
    r12 =  np.linalg.norm(r[:, :3]-r[:, 3:], axis = 1, keepdims = True)
    rdot12 = np.sum(r[:, :3]*r[:, 3:], axis = 1, keepdims = True)

    El1 = (beta - Z)*(1/r1 + 1/r2) + 1/r12 - beta**2
    El2 = 1/(2*(1+ alpha*r12)**2)

    El3 = (beta*(r1 + r2)/r12)*(1- rdot12/(r1*r2)) - 1/(2*(1+ alpha*r12)**2) -2/r12 + 2*alpha/(1+ alpha*r12)

    E_loc = El1 + El2*El3

    return E_loc

def d_alpha_wave_function(alpha, r):
    """ The derivative of the natural logarithm of the trail wave function with respect to alpha.
        Needed for the optimal alpha beta finder.

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

def d_beta_wave_function( r):
    """ The derivative of the natural logarithm of the trail wave function with respect to beta.
        Needed for the optimal alpha beta finder.

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
    dwf:          -(r1 + r2)

    """
    r1 = np.linalg.norm(r[:,:3], axis = 1, keepdims = True)
    r2 = np.linalg.norm(r[:,3:], axis = 1, keepdims = True)
    dwf = -(r1 + r2)
    return dwf
