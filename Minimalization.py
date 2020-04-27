import numpy as np
import matplotlib.pyplot as plt

from Metropolis import *
import Systems.HarmonicOscillator  as oscillator
import Systems.Hatom as Hydrogen
import Systems.Helium as Helium


def derivEnergy(alpha, N_tries, N_walkers, System):
    f = lambda R: System.trialWaveFunction(alpha, R)
    rn, accept_rate = metropolisAlgorithm(f, N_tries, N_walkers, System.dimension)
    deriv_wf = System.dWaveFunction(rn)

    E_loc = System.E_loc(alpha, rn)
    E_a = np.mean(E_loc)

    deriv_E = 2*(np.mean(E_loc*deriv_wf)- E_a*np.mean(deriv_wf))
    return deriv_E

def minimalAlphaFinder(alpha_guess, N_tries, N_walkers, System):
    alpha_current = alpha_guess

    toll = 1e-4
    learningrate = 0.5
    prev_step_size = 1
    count = 0
    max_count = 100
    alpha_values = [alpha_current]

    while prev_step_size > toll and count < max_count:
        alpha_old = alpha_current
        alpha_current = alpha_old - learningrate*derivEnergy(alpha_old, N_tries, N_walkers, System )

        prev_step_size = np.abs(alpha_current - alpha_old)
        count += 1
        alpha_values.append(alpha_current)
        print("alpha: {}, iteration: {}".format(alpha_current, count))
    return (alpha_values, count)


def plotMinumumAlpha(alpha_min, count):

    iterations = np.arange(count+1)

    plt.plot(iterations, alpha_min, linestyle = "--" , marker = "o")
    plt.xlabel("Iteration")
    plt.ylabel("\N{greek small letter alpha}")
    plt.title("Minimalization of \N{greek small letter alpha} ")
    plt.show()


# N_tries = 30000
# N_walkers = 50
# alpha_guess = 1.2
# System = oscillator
#
#
# alpha_min, count = minimalAlphaFinder(alpha_guess, N_tries, N_walkers, System)
# plotMinumumAlpha(alpha_min, count)
#
# print(f"this took {count}  iterations")
