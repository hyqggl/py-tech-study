import numpy as np


a = np.random.randn(3)
print a
b = a
b[0] = 0.0
print a


a = np.random.randn(3)
b = np.empty_like(a)
np.copyto(b, a)