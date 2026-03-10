import numpy as np


def logistic_map(r, x):
    """
    Compute one iteration of the logistic map.

    Parameters:
        r (float or np.ndarray): Growth/control parameter
        x (float or np.ndarray): Current state value

    Returns:
        float or np.ndarray: Next state value
    """
    return r * x * (1 - x)


def iterate_logistic_map(r, x0, n_iterations):
    """
    Compute multiple iterations of the logistic map.

    Parameters:
        r (float): Growth/control parameter
        x0 (float): Initial condition
        n_iterations (int): Number of iterations

    Returns:
        np.ndarray: Array of x values over time
    """
    x_values = np.zeros(n_iterations)
    x_values[0] = x0

    for i in range(1, n_iterations):
        x_values[i] = logistic_map(r, x_values[i - 1])

    return x_values
