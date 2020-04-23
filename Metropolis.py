import numpy as np


def metropolis_algorithm(function, N_tries, N_walkers, D):

    r_initial = np.random.randn(N_walkers, D)
    r_final = np.zeros((N_tries, N_walkers, D))
    displacement = 1.2*np.random.randn(N_tries, N_walkers, D)
    coin_flip = np.random.uniform(0, 1, (N_tries, N_walkers, D))

    # these will help to obtain the acceptance rate
    A = np.ones((N_walkers, D))
    B = np.zeros((N_walkers, D))
    accept = 0

    for i in range(N_tries):
        r_trial = r_initial + displacement[i,:,:]       # trial move
        ratio = (function(r_trial) / function(r_initial))**2

        r_final[i, :, :] = np.where(ratio >= 1, r_trial, (np.where(coin_flip[i,:,:] < ratio, r_trial, r_initial)))
        r_initial = np.where(ratio >= 1, r_trial, (np.where(coin_flip[i,:,:] < ratio, r_trial, r_initial)))

        accept += np.sum( np.where(ratio >= 1, A, (np.where(coin_flip[i,:,:] < ratio, A, B))) )

    rate = accept/(N_tries*N_walkers)

    r_shape = np.reshape(r_final[4000:,:], (N_tries*N_walkers -N_walkers*4000, D))     # trow out first 4000 ensuiring equiliburm
    return (r_shape, rate)
