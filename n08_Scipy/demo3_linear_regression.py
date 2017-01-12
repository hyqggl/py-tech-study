import numpy as np
from scipy.stats import linregress

x = np.random.randn(200)

y = 2 * x + 0.1 * np.random.randn(200)

gradient, intercept, r_value, p_value, std_err = linregress(x, y)

print gradient, intercept
