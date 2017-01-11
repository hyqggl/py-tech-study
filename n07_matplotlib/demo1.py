# from pylab import *  # Deprecated
# x = linspace(0, 10, 200)
# y = sin(x)
# plot(x, y, 'b-', linewidth=2)
# show()

import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 200)
y = np.sin(x)
plt.plot(x, y, 'b-', linewidth=2)
plt.show()