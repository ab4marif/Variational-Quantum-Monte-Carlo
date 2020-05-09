import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


def plot_energy(alpha, E_a, E_error, plotsave):
    
    plt.figure()
    plt.errorbar(alpha, E_a, yerr = E_error, linestyle = "--",  marker = 'o')
    plt.xlabel("\N{greek small letter alpha}")
    plt.ylabel("E(\N{greek small letter alpha})")
    plt.title(f"Ground state Energy")

    if plotsave == True:
        plot_name = input("Save your plot as: ")
        plt.savefig(f"Plots/{plot_name}.png")

    plt.show()

def plot_variance(alpha, E_var, plotsave):

    plt.figure()
    plt.plot(alpha, E_var, linestyle = "--",  marker = 'o')
    plt.xlabel("\N{greek small letter alpha}")
    plt.ylabel("E(\N{greek small letter alpha})")
    plt.title(f"  Variance of Ground state Energy")

    if plotsave == True:
        plot_name = input("Save your plot as: ")
        plt.savefig(f"Plots/{plot_name}.png")

    plt.show()

def plot_alpha(alpha_min, count, plotsave):

    iterations = np.arange(count)
    plt.plot(iterations, alpha_min, linestyle = "--" , marker = "o")
    plt.xlabel("Iteration")
    plt.ylabel("\N{greek small letter alpha}")
    plt.title("Minimalization of \N{greek small letter alpha} ")

    if plotsave == True:
        plot_name = input("Save your plot as: ")
        plt.savefig(f"Plots/{plot_name}.png")

    plt.show()

def subplot_energy_variance(alpha, E_a, E_error, E_var, plotsave):

    gs = gridspec.GridSpec(1, 2)
    plt.subplots_adjust(hspace=0.5 )

    # energy plot
    a1 = plt.subplot(gs[0,0])
    a1.errorbar(alpha, E_a, yerr = E_error, linestyle = "--",  marker = 'o')
    plt.xlabel("\N{greek small letter alpha}")
    plt.ylabel("E(\N{greek small letter alpha})")
    plt.title(f"Ground State Energy")


    # variance plot
    a2 = plt.subplot(gs[0,1])
    a2.plot(alpha, E_var, linestyle = "--",  marker = 'o')
    plt.xlabel("\N{greek small letter alpha}")
    plt.ylabel("var(E)")
    plt.title(f"Variance of Energy")

    if plotsave == True:
        plot_name = input("Save your plot as: ")
        plt.savefig(f"Plots/{plot_name}.png")

    plt.show()



def subplot_energy_variance_alpha(alpha, E_a, E_error, E_var, count, plotsave):

    gs = gridspec.GridSpec(2, 2)
    iterations = np.arange(count)

    # energy plot
    plt.subplot(gs[0, :])
    plt.errorbar(alpha, E_a, yerr = E_error, linestyle = "--",  marker = 'o')
    plt.xlabel("\N{greek small letter alpha}")
    plt.ylabel("E(\N{greek small letter alpha})")
    plt.title(f"Ground State Energy")
    plt.gca().invert_xaxis()

    # alpha plot
    plt.subplots_adjust(hspace=0.5, wspace = 0.5 )
    plt.subplot(gs[1, 0])
    plt.plot(iterations, alpha, linestyle = "--" , marker = "o")
    plt.xlabel("Iteration")
    plt.ylabel("\N{greek small letter alpha}")
    plt.title("Minimalization of \N{greek small letter alpha} ")

    # variance plot
    plt.subplot(gs[1, 1])
    plt.plot(alpha, E_var, linestyle = "--",  marker = 'o')
    plt.xlabel("\N{greek small letter alpha}")
    plt.ylabel("var(E)")
    plt.title(f"Variance of Energy")
    plt.gca().invert_xaxis()

    if plotsave == True:
        plot_name = input("Save your plot as: ")
        plt.savefig(f"Plots/{plot_name}.png")

    plt.show()

def subplot_energy_variance_alpha_beta(alpha,beta, E_a, E_var, E_error, count, plotsave):

    gs = gridspec.GridSpec(2, 2)
    iterations = np.arange(count)

    # energy plot
    plt.subplot(gs[0, 0])
    plt.errorbar(alpha, E_a, yerr = E_error, linestyle = "--",  marker = 'o')
    plt.xlabel("\N{greek small letter alpha}")
    plt.ylabel("E(\N{greek small letter alpha})")
    plt.title(f"  Ground State Energy")
    plt.gca().invert_xaxis()

    # variance plot
    plt.subplot(gs[0, 1])
    plt.plot(alpha, E_var, linestyle = "--",  marker = 'o')
    plt.xlabel("\N{greek small letter alpha}")
    plt.ylabel("var(E)")
    plt.title(f"  Variance")
    plt.gca().invert_xaxis()

    # alpha plot
    plt.subplots_adjust(hspace=0.5, wspace = 0.5 )
    plt.subplot(gs[1, 0])
    plt.plot(iterations, alpha, linestyle = "--" , marker = "o")
    plt.xlabel("Iteration")
    plt.ylabel("\N{greek small letter alpha}")
    plt.title("Minimalization of \N{greek small letter alpha} ")

    # beta plot
    plt.subplot(gs[1, 1])
    plt.plot(iterations, beta, linestyle = "--",  marker = 'o')
    plt.xlabel("Iteration")
    plt.ylabel("\N{greek small letter beta}")
    plt.title("Minimalization of \N{greek small letter beta} ")

    if plotsave == True:
        plot_name = input("Save your plot as: ")
        plt.savefig(f"Plots/{plot_name}.png")

    plt.show()
