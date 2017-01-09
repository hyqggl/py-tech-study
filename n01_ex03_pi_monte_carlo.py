#coding=utf-8
"""
Compute an approximation to ππ using Monte Carlo. Use no imports besides

import numpy as np
Your hints are as follows:

If UU is a bivariate uniform random variable on the unit square (0,1)2(0,1)2, then the probability that UU lies in a subset BB of (0,1)2(0,1)2 is equal to the area of BB
If U1,…,UnU1,…,Un are iid copies of UU, then, as nn gets large, the fraction that fall in BB converges to the probability of landing in BB
For a circle, area = pi * radius^2

"""
from __future__ import division
import numpy as np

n = 100000

count = 0
for i in range(n):
    u, v = np.random.uniform(), np.random.uniform()
    d = np.sqrt((u - 0.5)**2 + (v - 0.5)**2)
    if d < 0.5:
        count += 1

area_estimate = count / n

print(area_estimate * 4)

