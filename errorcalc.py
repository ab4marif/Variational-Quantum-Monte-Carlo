import numpy as np

def bootstrapError(data, N_error):
    """ Calculates error of a data set with the bootstrap Method. It picks a
        random set from the data, with this subset the mean is calculated.
        This is done N_error times, then the standard deviation of this gives the error of the
        data.

    Parameters
    ----------
    data:           Data set of N points
    N_error         Number of times to calculate the mean data from the subset


    Returns:
    --------
    data_error:      error of the data

    """
    N_subset = 10000
    data_subset = np.random.choice(data, (N_subset, N_error))

    average_data_subsets = np.mean(data_subset, axis = 0)
    var_rdnset = np.var(data_subset, axis = 0)

    variance = np.mean(var_rdnset)
    error_var = np.std(var_rdnset)
    error_data = np.std(average_data_subsets)


    return (error_data, variance, error_var)
