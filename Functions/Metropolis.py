import numpy as np


def metropolisAlgorithm(function, N_tries, N_walkers, D):
    """ This function performs the metroplolis algorithm for important sampling. it sets N number of walkers in a random position
        It makes a random trail move. The trail function is evauluted at the new configuration and its ratio sqaured with the old
        configuration is calculated. p = [ψT(R)/ψT(R)]2. If p < 1: the new position is accepted with probability p;
        If p ≥ 1 the new position is accepted;

    Parameters
    ----------
    function:               The trail wave function of the system with R as its input
    N_walkers:              Number of random walkers placed
    N_tries:                Number of steps for the walkers to try
    D:                      Dimension of the system


    Returns:
    --------
    data_error:             All of the walkers and its accepted moves in a single numpy array of
                            (N_walkers x N_tries -N_walkers*4000, D) which takes away the first 4000 for equiliburm
    rate:                   int the number of overall accepted moves by the walkers

    """

    r_initial = np.random.randn(N_walkers, D)
    r_final = np.zeros((N_tries, N_walkers, D))
    displacement = 0.3*np.random.randn(N_tries, N_walkers, D)       # set outside of for loop
    coin_flip = np.random.uniform(0, 1, (N_tries, N_walkers, D))    # to compare with if ratio < 1

    # these will help to obtain the acceptance rate
    A = np.ones((N_walkers, D))
    B = np.zeros((N_walkers, D))
    accept = 0

    for i in range(N_tries):
        r_trial = r_initial + displacement[i,:,:]       # trial move
        ratio = (function(r_trial) / function(r_initial))**2

        r_final[i, :, :] = np.where(ratio >= 1, r_trial, (np.where(coin_flip[i,:,:] < ratio, r_trial, r_initial)))
        r_initial = np.where(ratio >= 1, r_trial, (np.where(coin_flip[i,:,:] < ratio, r_trial, r_initial)))

        # keep track of accepted moves
        accept += np.sum( np.where(ratio >= 1, A, (np.where(coin_flip[i,:,:] < ratio, A, B))) )

    rate = accept/(N_tries*N_walkers*D)

    r_shape = np.reshape(r_final[4000:,:], (N_tries*N_walkers -N_walkers*4000, D))     # trow out first 4000 ensuiring equiliburm
    return (r_shape, rate)
