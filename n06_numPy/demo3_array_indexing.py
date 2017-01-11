import numpy as np


z = np.array([[1, 2], [3, 4]])
print z[0, 0]
print z[0, 1]

print z[0, :]
print z[:, 1]


z = np.linspace(2, 4, 5)
print z
indices = np.array((0, 2, 3))
print z[indices]

d = np.array([0, 1, 1, 0, 0], dtype=bool)
print z[d]

z = np.empty(3)
z[:] = 42
print z

