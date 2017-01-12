import numpy as np
from scipy.stats import beta
import matplotlib.pyplot as plt

q = beta(5, 5)      # Beta(a, b), with a = b = 5
obs = q.rvs(2000)   # 2000 observations
grid = np.linspace(0.01, 0.99, 100)

fig, ax = plt.subplots()
ax.hist(obs, bins=40, normed=True)
ax.plot(grid, q.pdf(grid), 'k-', linewidth=2)
# fig.show()
plt.show()

print q.cdf(0.4)      # Cumulative distribution function
print q.pdf(0.4)      # Density function
print q.ppf(0.8)      # Quantile (inverse cdf) function
print q.mean()
