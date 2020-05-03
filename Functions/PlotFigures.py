import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


def plotEnergy(alpha, E_a, E_error):

    plt.figure()
    plt.errorbar(alpha, E_a, yerr = E_error, linestyle = "--",  marker = 'o')
    plt.xlabel("\N{greek small letter alpha}")
    plt.ylabel("E(\N{greek small letter alpha})")
    plt.title(f"  Ground state Energy")
    plt.show()

def plotVariance(alpha, E_var, var_error):

    plt.figure()
    plt.errorbar(alpha, E_var, yerr = var_error, linestyle = "--",  marker = 'o')
    plt.xlabel("\N{greek small letter alpha}")
    plt.ylabel("E(\N{greek small letter alpha})")
    plt.title(f"  Variance of Ground state Energy")
    plt.show()

def plotMinumumAlpha(alpha_min, count):

    iterations = np.arange(count+1)

    plt.plot(iterations, alpha_min, linestyle = "--" , marker = "o")
    plt.xlabel("Iteration")
    plt.ylabel("\N{greek small letter alpha}")
    plt.title("Minimalization of \N{greek small letter alpha} ")
    plt.show()

def subplotEnergyVariance(alpha, E_a, E_error, E_var, var_error):

    plt.subplots_adjust(hspace=0.5 )

    # energy plot
    plt.subplot(211)
    plt.errorbar(alpha, E_a, yerr = E_error, linestyle = "--",  marker = 'o')
    plt.xlabel("\N{greek small letter alpha}")
    plt.ylabel("E(\N{greek small letter alpha})")
    plt.title(f"  Ground State Energy")

    # variance plot
    plt.subplot(212)
    plt.errorbar(alpha, E_var, yerr = var_error, linestyle = "--",  marker = 'o')
    plt.xlabel("\N{greek small letter alpha}")
    plt.ylabel("\N{greek small letter sigma}(\N{greek small letter alpha})")
    plt.title(f"  Variance")

    plt.show()

def subplotEnergyVarianceAlpha(alpha, E_a, E_error, E_var, var_error, count):

    gs = gridspec.GridSpec(2, 2)

    iterations = np.arange(count+1)

    # alpha plot
    plt.subplots_adjust(hspace=0.5, wspace = 0.5 )
    plt.subplot(gs[1, 0])
    plt.plot(iterations, alpha, linestyle = "--" , marker = "o")
    plt.xlabel("Iteration")
    plt.ylabel("\N{greek small letter alpha}")
    plt.title("Minimalization of \N{greek small letter alpha} ")

    # energy plot
    plt.subplot(gs[0, :])
    plt.errorbar(alpha, E_a, yerr = E_error, linestyle = "--",  marker = 'o')
    plt.xlabel("\N{greek small letter alpha}")
    plt.ylabel("E(\N{greek small letter alpha})")
    plt.title(f"  Ground State Energy")

    # variance plot
    plt.subplot(gs[1, 1])
    plt.errorbar(alpha, E_var, yerr = var_error, linestyle = "--",  marker = 'o')
    plt.xlabel("\N{greek small letter alpha}")
    plt.ylabel("\N{greek small letter sigma}(\N{greek small letter alpha})")
    plt.title(f"  Variance")

    plt.show()
