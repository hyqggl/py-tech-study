import numpy as np


A = np.array((4, 3, 2, 1))

# array([4, 3, 2, 1])

A.sort()              # Sorts A in place

# array([1, 2, 3, 4])

A.sum()               # Sum

#10

A.mean()              # Mean
# 2.5

A.max()               # Max
# 4

A.argmax()            # Returns the index of the maximal element
# 3

A.cumsum()            # Cumulative sum of the elements of A
# array([ 1,  3,  6, 10])

A.cumprod()           # Cumulative product of the elements of A
# array([ 1,  2,  6, 24])

A.var()               # Variance
# 1.25

A.std()               # Standard deviation
# 1.1180339887498949

A.shape = (2, 2)

print A.T                   # Equivalent to A.transpose()

# array([[1, 3],
#        [2, 4]])

z = np.linspace(2, 4, 5)
# If z is a nondecreasing array, then z.searchsorted(a) returns the index of the first element of z that is >= a
print z.searchsorted(2.2)
print z.searchsorted(2.5)
print z.searchsorted(2.6)


