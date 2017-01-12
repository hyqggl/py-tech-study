"""
So far we have seen that the Newton-Raphson method is fast but not robust

This bisection algorithm is robust but relatively slow

This illustrates a general principle

If you have specific knowledge about your function, you might be able to exploit it to generate efficiency
If not, then algorithm choice involves a trade-off between speed of convergence and robustness
In practice, most default algorithms for root finding, optimization and fixed points use hybrid methods

These methods typically combine a fast method with a robust method in the following manner:

Attempt to use a fast method
Check diagnostics
If diagnostics are bad, then switch to a more robust algorithm
In scipy.optimize, the function brentq is such a hybrid method, and a good default
"""

from scipy.optimize import brentq
import numpy as np

f = lambda x: np.sin(4 * (x - 0.25)) + x + x**20 - 1
print brentq(f, 0, 1)

# scipy.optimize.fsolve
# fixed_point
