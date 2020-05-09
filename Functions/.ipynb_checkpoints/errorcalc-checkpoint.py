import numpy as np


def data_blocking_error(data, block_size):
    """ Uses data blocking to compute the error in a given data set. The time series data set is replaced with a block averaged
        version. It first splits the time series into blocks with a certain blocksize. Then it computes the averages of each
        of these blocks. If the blocksize is chosen correctly the data will be statistically uncorrelated so the error can be
        computed in the usual fashion.


    Parameters
    ----------
    data:           Data set of N points
    block_size:     Size of the blocks from the data set


    Returns:
    --------
    error_data:         error of the data
    variance:           Variance of data
    """

    N_blocks = int(len(data)/block_size)
    blocks = np.array( np.array_split(data, N_blocks))
    block_av = np.zeros(N_blocks)

    for i in range(N_blocks):
        block_av[i] = np.mean( blocks[i])

    error_data = np.sqrt(1/(N_blocks - 1)*(np.mean(block_av**2)- np.mean(block_av)**2 ) )
    variance = np.var(data)

    return (error_data, variance)


def bootstrapError(data, N_error):
    """ Calculates error of a data set with the bootstrap Method. It picks a
        random set from the data, with this subset the mean is calculated.
        This is done N_error times, then the standard deviation of this gives the error of the
        data.

        # NOTE: This can only be used for non correlated data

    Parameters
    ----------
    data:           Data set of N points
    N_error         Number of times to calculate the mean data from the subset


    Returns:
    --------
    error_data:         error of the data
    variance:           Variance of data
    """

    N_subset = 10000
    data_subset = np.random.choice(data, (N_subset, N_error))

    average_data_subsets = np.mean(data_subset, axis = 0)
    var_rdnset = np.var(data_subset, axis = 0)

    variance = np.mean(var_rdnset)
    error_var = np.std(var_rdnset)
    error_data = np.std(average_data_subsets)


    return (error_data, variance)
