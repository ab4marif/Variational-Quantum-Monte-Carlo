import numpy as np

from Functions.errorcalc import *
from Functions.steepest_descent import *
from Functions.plot_figures import *
import Systems.HarmonicOscillator  as Oscillator
import Systems.Hatom as Hydrogen
import Systems.Helium as Helium


def optimal_energy_finder(alpha_guess, N_walkers, N_tries, System, plot_setting):
    """ For a given system finds the optimal ground state energy.

    Parameters
    ----------
    alpha_guess:            int; first value of alpha
    N_walkers:              Number of random walkers placed
    N_tries:                Number of steps for the walkers to try
    System:                 Current system. Can choose between: Oscillator, Hydrogen or Helium
    plot_setting:           list;   [plots subplot plotsave]

                                    plots:      set to True if want to show the plot
                                    plotsave:   set to True if want to save the plot

    """

    alpha, iteration, E_loc , E_a = optimal_alpha_finder(alpha_guess, N_tries, N_walkers, System)

    E_var = np.zeros(len(alpha))
    E_error = np.zeros(len(alpha))

    for i in range(len(alpha)):
       E_error[i], E_var[i] = data_blocking_error(E_loc[i,:,0], block_size = 6000)


    alpha_min = alpha[-1]
    E_min = E_a[-1]

    if System == Helium:
        E_exp = - 2.9037        # experimental value of ground state Helium
        percentage = np.abs(100*(E_min + E_error[-1]  - E_exp)/E_exp)

    print()
    print("The energy was found to be optimal with \N{greek small letter alpha} = {}".format(alpha_min))
    print("The corresponding Energy is E = {} +/- {}".format(E_min, E_error[-1]))
    print("With variance var = {} ".format(E_var[-1]))

    if System == Helium:
        print()
        print("Deviation from experimental value: {} %".format(round(percentage, 2)))

    # plots
    plots = plot_setting[0]
    plotsave = plot_setting[1]

    if plots == True:
        subplot_energy_variance_alpha(alpha, E_a, E_error, E_var, iteration, plotsave)


# System parameters
System = Oscillator             # please choose: Oscillator, Hydrogen or Helium.
N_tries = 30000
N_walkers = 400
alpha_guess = 1.2

# plot settings
plots = True
plotsave = False
plot_setting = [plots, plotsave]

optimal_energy_finder(alpha_guess, N_walkers, N_tries, System, plot_setting)
