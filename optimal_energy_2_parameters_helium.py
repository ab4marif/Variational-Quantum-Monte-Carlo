import numpy as np

from Functions.errorcalc import *
from Functions.steepest_descent import *
from Functions.plot_figures import *
import Systems.Helium2 as Helium2


def optimal_energy_finder(alpha_guess, beta_guess, N_walkers, N_tries, System, plot_setting):
    """For a System with 2 parameters alpha and beta: Helium2. Finds the optimal ground state energy.

    Parameters
    ----------
    alpha_guess:            int; first value of alpha
    beta_guess:             int; first value of beta
    N_walkers:              Number of random walkers placed
    N_tries:                Number of steps for the walkers to try
    System:                 Current system. Only Helium2
    plots:                  True or False to plot the results

    """

    alpha, beta, iteration, E_loc , E_a = optimal_alpha_beta_finder(alpha_guess, beta_guess, N_tries, N_walkers, System)

    E_var = np.zeros(len(alpha))
    E_error = np.zeros(len(alpha))
    var_error = np.zeros(len(alpha))

    # calculate the errors
    for i in range(len(alpha)):
       E_error[i], E_var[i] = data_blocking_error(E_loc[i,:,0], block_size = 6000)


    alpha_min = alpha[-1]
    E_min = E_a[-1]
    E_exp = - 2.9037            # experimental value of ground state Helium
    percentage = np.abs(100*(E_min  + E_error[-1]  - E_exp)/E_exp)

    print("The energy was found to be optimal with \N{greek small letter alpha} = {} and \N{greek small letter beta} = {} ".format(alpha_min, beta[-1]))
    print("The corresponding Energy is E = {} +/- {}".format(E_min, E_error[-1]))
    print("With variance var = {} ".format(E_var[-1]))
    print()
    print("Deviation from experimental value: {}%".format(round(percentage, 2)))

    if plots == True:
        subplot_energy_variance_alpha_beta(alpha, beta, E_a, E_var, E_error, iteration, plotsave)



# System parameters
System = Helium2        # only Helium2 for this file
N_tries = 10000
N_walkers = 50

# Guess the initial values of the parameters
alpha_guess = 0.4
beta_guess = 2

# plot settings
plots = True
plotsave = False
plot_setting = [plots, plotsave]

optimal_energy_finder(alpha_guess, beta_guess, N_walkers, N_tries, System, plot_setting)
