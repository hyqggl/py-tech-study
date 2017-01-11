import numpy as np


z = np.array([1, 2, 3])
print np.sin(z)

y = np.empty_like(z)
n = z.size

for i in range(n):
    y[i] = np.sin(z[i])
print y


def f(x):
    return 1 if x > 0 else 0

x1 = np.random.randn(4)
print x1
# np.where(x1 > 0, 1, 0)  # Insert 1 if x > 0 true, otherwise 0
print x1

f = np.vectorize(f)
f(x1)

# Comparisons
z = np.array([2, 3])
y = np.array([2, 3])
print z == y

#Subpackages
z = np.random.randn(10000)  # Generate standard normals
y = np.random.binomial(10, 0.5, size=1000)    # 1,000 draws from Bin(10, 0.5)
print y.mean()
print z.mean()
