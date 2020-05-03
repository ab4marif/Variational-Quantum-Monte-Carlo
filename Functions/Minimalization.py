import numpy as np

from Functions.Metropolis import *
import Systems.HarmonicOscillator  as oscillator
import Systems.Hatom as Hydrogen
import Systems.Helium as Helium



def derivEnergy(alpha, N_tries, N_walkers, System):
    """ This function calculates the derivative of the energy with respect to alpha.
        dE/dα = 2 (<E_loc dlnψT/dα > − E< dlnψT/dα> ). dlnψT/dα is the natural logarithm derivative with respect to alpha.


    Parameters
    ----------
    alpha:                  int; value of current alpha
    N_walkers:              Number of random walkers placed
    N_tries:                Number of steps for the walkers to try
    System:                 current system. Can choose between: oscillator, Hydrogen or Helium


    Returns:
    --------
    deriv_E:                int; dE/dα the derivative of the enrgy with respect to current alpha
    E_loc:                  numpy array of the local energy for each position
    E_a:                    The ground state energy for the alpha

    """

    f = lambda R: System.trialWaveFunction(alpha, R)
    rn, accept_rate = metropolisAlgorithm(f, N_tries, N_walkers, System.dimension)

    # If system is helium the derivative of the trail wave function also depends on alpha
    if System == Helium:
        deriv_wf = System.dWaveFunction(alpha, rn)
    else:
        deriv_wf = System.dWaveFunction(rn)


    E_loc = System.E_loc(alpha, rn)
    E_a = np.mean(E_loc)

    deriv_E = 2*(np.mean(E_loc*deriv_wf)- E_a*np.mean(deriv_wf))
    return (deriv_E, E_loc, E_a)


def minimalAlphaFinder(alpha_guess, N_tries, N_walkers, System):
    """ Uses steepest descent method to gain the optimal value for alpha and thus also the optimal value for the Energy.
        First a guess has to be made for the alpha. Then it calculates the derivative of the energy with that alpha and uses
        that value to obtain a new value for alpha: α_new = α_old − γ*(dE/dα)_old where gamma is the learningrate. The
        search stops when α_new - α_old is smaller than some tollerance.


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
    alpha_current = alpha_guess
    deriv_E, E_loc, E_a = derivEnergy(alpha_guess, N_tries, N_walkers, System )

    # store the values in python lists
    alpha_values = [alpha_current]
    Eloc_values = [E_loc]
    Ea_values = [E_a]

    # settings for the minimalization algorithm
    toll = 1e-3
    learningrate = 0.5
    prev_step_size = 1
    count = 0
    max_count = 100


    while prev_step_size > toll and count < max_count:
        alpha_old = alpha_current
        deriv_E, E_loc, E_a = derivEnergy(alpha_old, N_tries, N_walkers, System )

        alpha_current = alpha_old - learningrate*deriv_E
        prev_step_size = np.abs(alpha_current - alpha_old)
        count += 1

        # Keep track of every value found
        Eloc_values.append(E_loc)
        Ea_values.append(E_a)
        alpha_values.append(alpha_current)
        print("alpha: {}, iteration: {}".format(alpha_current, count))

    # convert python list into numpy array for better calculation
    Eloc_values = np.array(Eloc_values)
    alpha_values = np.array(alpha_values)
    Ea_values = np.array(Ea_values)
    return (alpha_values, count, Eloc_values, Ea_values)
