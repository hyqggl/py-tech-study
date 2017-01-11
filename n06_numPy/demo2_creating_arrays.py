import numpy as np


z = np.empty(3)
print z

z = np.linspace(2, 4, 5)
print z

z = np.identity(2)
print z

z = np.array([10, 20])
print z
print type(z)

z = np.array((10, 20), dtype=float)
print z

z = np.array([[1, 2], [3, 4]])
print z

na = np.linspace(10, 20, 2)
print na is np.asarray(na)
print na is np.array(na)
