import matplotlib.pyplot as plt
import numpy as np

alpha = 0.9
ts_length = 200
current_x = 0

x_values = []
for i in range(ts_length + 1):
    x_values.append(current_x)
    current_x = alpha * current_x + np.random.randn()
plt.plot(x_values, 'b-')
plt.show()