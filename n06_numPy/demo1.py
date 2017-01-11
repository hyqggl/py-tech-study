import numpy as np


# x = np.random.uniform(0, 1, size=1000000)
# print x.mean()

a = np.zeros(3)
print type(a)
print type(a[0])
b = np.zeros(3, dtype=int)
print type(b)
print type(b[0])

# Shape and Dimension
z = np.zeros(10)
print z.shape
z.shape = (10, 1)
print z
z.shape = (2, 2)
print z

