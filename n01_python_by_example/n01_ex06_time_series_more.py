#coding=utf-8
"""
Now, starting with your solution to exercise 5, plot three simulated time series, one for each of the cases α=0α=0, α=0.8α=0.8 and α=0.98
"""
import matplotlib.pyplot as plt
import numpy as np


alphas = [0.0, 0.8, 0.98]
ts_length = 200

for alpha in alphas:
    x_values = []
    current_x = 0
    for i in range(ts_length):
        x_values.append(current_x)
        current_x = alpha * current_x + np.random.randn()
    plt.plot(x_values, label='alpha = ' + str(alpha))
plt.legend()
plt.show()