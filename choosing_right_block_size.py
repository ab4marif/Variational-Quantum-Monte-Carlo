import numpy as np
import

from Functions.metropolis import *
from Functions.errorcalc import *
from Functions.plot_figures import *
import Systems.HarmonicOscillator  as Oscillator
import Systems.Hatom as Hydrogen
import Systems.Helium as Helium


""" This file is to help choose the right block size to calculate the error of a correlated time series.
    It will plot the error as function of the block size, and if the error is rougly constant the data series
    becomes uncorrelated.
"""
def block_size_error_plot(System, N_tries, N_walkers, alpha, D, plots):

    f = lambda R: System.trial_wave_function(alpha,  R)
    rn, accept_rate = metropolis_algorithm(f, N_tries, N_walkers, D)
    E = System.E_loc(alpha, rn)
    E_a = np.mean(E)

    block_size = np.arange(200, 2000)

    E_error = np.zeros(len(block_size))
    var = np.zeros(len(block_size))

    for i in range(len(block_size)):
        E_error[i], var[i]  = data_blocking_error(E[:,0], block_size[i])

    if plots == True:
        plt.plot(block_size, E_error)
        plt.savefig("Plots/Error_blocksize.png")
        plt.show()

# Simulation parameters
System = Helium
N_tries = 30000
N_walkers = 400
plots = True
alpha = 0.14
D = System.dimension

block_size_error_plot(System, N_tries, N_walkers, alpha, D, plots)
