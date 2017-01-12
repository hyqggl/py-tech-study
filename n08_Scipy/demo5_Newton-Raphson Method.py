from scipy.optimize import newton
import numpy as np

f = lambda x: np.sin(4 * (x - 0.25)) + x + x**20 - 1
print newton(f, 0.2)
print newton(f, 0.7)


# timeit newton(f, 0.2)      #IPYTHON
