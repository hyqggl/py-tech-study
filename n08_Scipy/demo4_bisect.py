import numpy as np
from scipy.optimize import bisect


# f = lambda x: np.sin(4 * (x - 0.25)) + x + x**20 - 1
#bisect(f, 0, 1)


def bisect(f, a, b, tol=10e-5):
    """
    Implements the bisection root finding algorithm, assuming that f is a
    real-valued function on [a, b] satisfying f(a) < 0 < f(b).
    """
    lower, upper = a, b

    while upper - lower > tol:
        middle = 0.5 * (upper + lower)
        # === if root is between lower and middle === #
        if f(middle) > 0:
            lower, upper = lower, middle
        # === if root is between middle and upper  === #
        else:
            lower, upper = middle, upper

    return 0.5 * (upper + lower)