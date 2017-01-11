import numpy as np


a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
print a + b
print a * b
print a + 10
print a * 10
A = np.ones((2, 2))
B = np.ones((2, 2))
print A
print B
print A + B
print A + 10
print A * B

# Matrix
# print A @ B
print np.dot(A, B)

A = np.array((1, 2))
B = np.array((10, 20))
print np.dot(A, B)
