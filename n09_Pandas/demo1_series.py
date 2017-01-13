import pandas as pd
import numpy as np


s = pd.Series(np.random.randn(4), name='daily returns')
print(s)
print(np.abs(s))
print(s.describe())

s.index = ['A', 'b', 'c', 'd']
print(s)

print(s['A'])
s['A'] = 0
print(s)
print('A' in s)
