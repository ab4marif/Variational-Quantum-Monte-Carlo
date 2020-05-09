import numpy as np

from Functions.metropolis import *
import Systems.HarmonicOscillator  as oscillator
import Systems.Hatom as Hydrogen
import Systems.Helium as Helium
    
""" This file has the functions to find the optimal parameters by using the steepest descent method,
    for 1 and 2 parameters
"""

def deriv_energy_alpha(alpha, N_tries, N_walkers, System):
    """ This function calculates the derivative of the energy with respect to alpha.

            dE/dα = 2 (<E_loc dlnψT/dα > − E< dlnψT/dα> ).

        dlnψT/dα is the natural logarithm derivative with respect to alpha.


    Parameters
    ----------
    alpha:                  int; value of current alpha
    N_walkers:              Number of random walkers placed
    N_tries:                Number of steps for the walkers to try
    System:                 current system. Can choose between: Oscillator, Hydrogen or Helium


    Returns:
    --------
    deriv_E:                int; dE/dα the derivative of the enrgy with respect to current alpha
    E_loc:                  numpy array of the local energy for each position
    E_a:                    The ground state energy for the alpha

    """

    f = lambda R: System.trial_wave_function(alpha, R)
    rn, accept_rate = metropolis_algorithm(f, N_tries, N_walkers, System.dimension)

    # If system is helium the derivative of the trail wave function also depends on alpha
    if System == Helium:
        deriv_wf = System.deriv_wave_function(alpha, rn)
    else:
        deriv_wf = System.deriv_wave_function(rn)


    E_loc = System.E_loc(alpha, rn)
    E_a = np.mean(E_loc)

    deriv_E = 2*(np.mean(E_loc*deriv_wf)- E_a*np.mean(deriv_wf))
    return (deriv_E, E_loc, E_a)


def deriv_energy_alpha_beta(alpha, beta, N_tries, N_walkers, System):
    """ This function calculates the derivative of the energy with respect to alpha and beta.

            dE/dα = 2 (<E_loc dlnψT/dα > − E< dlnψT/dα> ).
            dE/dβ = 2 (<E_loc dlnψT/dβ > − E< dlnψT/dβ> ).

        dlnψT/dα is the natural logarithm derivative with respect to alpha and likewise dlnψT/dβ is the natural
        logarithm derivative with respect to beta.

        # NOTE: this function only works for System Helium2


    Parameters
    ----------
    alpha:                  int; value of current alpha
    beta:                   int; value of current beta
    N_walkers:              Number of random walkers placed
    N_tries:                Number of steps for the walkers to try
    System:                 Current system. This function only works for Helium2


    Returns:
    --------
    deriv_E_alpha:          int; dE/dα the derivative of the energy with respect to current alpha
    deriv_E_beta:           int; dE/dβ the derivative of the energy with respect to current beta
    E_loc:                  numpy array of the local energy for each position
    E_a:                    The ground state energy for the alpha and beta

    """

    f = lambda R: System.trial_wave_function(alpha, beta, R)

    rn, accept_rate = metropolis_algorithm(f, N_tries, N_walkers, System.dimension)


    deriv_alpha = System.d_alpha_wave_function(alpha, rn)
    deriv_beta = System.d_beta_wave_function(rn)


    E_loc = System.E_loc(alpha,beta, rn)
    E_a = np.mean(E_loc)

    deriv_E_alpha = 2*(np.mean(E_loc*deriv_alpha)- E_a*np.mean(deriv_alpha))
    deriv_E_beta = 2*(np.mean(E_loc*deriv_beta)- E_a*np.mean(deriv_beta))

    return (deriv_E_alpha, deriv_E_beta, E_loc, E_a)


def optimal_alpha_beta_finder(alpha_guess, beta_guess, N_tries, N_walkers, System):
    """ Uses steepest descent method to gain the optimal value for alpha and beta and thus also the optimal value for the Energy.
        First a guess has to be made for the parameters. Then it calculates the derivative of the energy with respect to the parameters and uses
        that value to obtain a new value for the parameters:

            α_new = α_old − γ*(dE/dα)_old
            β_new = β_old − γ*(dE/dβ)_old

        where gamma is the learningrate. The search stops when α_new - α_old and β_new - β_old is smaller than some tollerance.

        # NOTE: This function only works for System Helium2

    Parameters
    ----------
    alpha_guess:            int; first value of alpha
    beta_guess:             int; first value of beta
    N_walkers:              Number of random walkers placed
    N_tries:                Number of steps for the walkers to try
    System:                 current system. Only Helium2


    Returns:
    --------
    alpha_values            numpy array of all the values of alpha calculated in the process
    beta_values:            numpy array of all the values of beta calculated in the process
    count:                  int; number of iteration neccasary
    Eloc_values:            numpy array of the local energies for each alpha and beta
    Ea_values:              numpy array of the ground state energy found with the alphas and betas

    """


    # initializing values with the guess alpha
    alpha = alpha_guess
    beta = beta_guess
    deriv_E_alpha, deriv_E_beta, E_loc, E_a = deriv_energy_alpha_beta(alpha, beta, N_tries, N_walkers, System )

    # store the values in python lists
    alpha_values = [alpha]
    beta_values = [beta]
    Eloc_values = [E_loc]
    Ea_values = [E_a]

    # settings for the minimalization algorithm
    toll = 1e-3
    learningrate = 0.4
    count = 0
    max_count = 100


    while True:
        deriv_E_alpha, deriv_E_beta, E_loc, E_a = deriv_energy_alpha_beta(alpha, beta, N_tries, N_walkers, System )
        alpha_temp = alpha - learningrate*deriv_E_alpha
        beta_temp = beta - learningrate*deriv_E_beta

        count += 1
        if count > max_count:
            print("Too many iteration. Adjust learning rate")
            break

        if (np.abs(alpha_temp - alpha) < toll) and (np.abs(beta_temp - beta) < toll):
            break

        # Simultaneuos update
        alpha = alpha_temp
        beta = beta_temp


        # Keep track of every value found
        Eloc_values.append(E_loc)
        Ea_values.append(E_a)
        alpha_values.append(alpha)
        beta_values.append(beta)
        print("Iteration: {}, alpha: {}, beta: {}".format(count, alpha, beta))

    # convert python list into numpy array for better handeling
    Eloc_values = np.array(Eloc_values)
    alpha_values = np.array(alpha_values)
    Ea_values = np.array(Ea_values)
    beta_values = np.array(beta_values)

    return (alpha_values, beta_values, count, Eloc_values, Ea_values)


def optimal_alpha_finder(alpha_guess, N_tries, N_walkers, System):
    """ Uses steepest descent method to gain the optimal value for alpha and thus also the optimal value for the Energy.
        First a guess has to be made for the alpha. Then it calculates the derivative of the energy with that alpha and uses
        that value to obtain a new value for alpha:

                α_new = α_old − γ*(dE/dα)_old

        where gamma is the learningrate. The search stops when α_new - α_old is smaller than some tollerance.


    Parameters
    ----------
    alpha_guess:            int; first value of alpha
    N_walkers:              Number of random walkers placed
    N_tries:                Number of steps for the walkers to try
    System:                 current system. Can choose between: oscillator, Hydrogen or Helium


    Returns:
    --------
    alpha_values            numpy array of all the values of alpha calculated in the process
    count:                  int; number of iteration neccasary
    Eloc_values:            numpy array of the local energies for each alpha
    Ea_values:              numpy array of the ground state energy found with the alphas

    """
    # initializing values with the guess alpha
    alpha = alpha_guess
    deriv_E, E_loc, E_a = deriv_energy_alpha(alpha_guess, N_tries, N_walkers, System )

    # store the values in python lists
    alpha_values = [alpha_guess]
    Eloc_values = [E_loc]
    Ea_values = [E_a]

    # settings for the minimalization algorithm
    toll = 1e-3
    learningrate = 0.5
    prev_step_size = 1
    count = 0
    max_count = 100


    while True:
        deriv_E, E_loc, E_a = deriv_energy_alpha(alpha, N_tries, N_walkers, System )
        alpha_new = alpha - learningrate*deriv_E

        count += 1
        if count > max_count:
            print("Too many iterations. Try to adjust learning rate")
            break

        if np.abs(alpha_new - alpha) < toll:
            break

        alpha = alpha_new

        # Keep track of every value found
        Eloc_values.append(E_loc)
        Ea_values.append(E_a)
        alpha_values.append(alpha)
        print("Iteration: {}, alpha: {}".format(count, alpha))

    # convert python list into numpy array for better handeling
    Eloc_values = np.array(Eloc_values)
    alpha_values = np.array(alpha_values)
    Ea_values = np.array(Ea_values)

    return (alpha_values, count, Eloc_values, Ea_values)
