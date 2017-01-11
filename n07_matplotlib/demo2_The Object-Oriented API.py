import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()
x = np.linspace(0, 10, 200)
y = np.sin(x)
ax.plot(x, y, 'b-', linewidth=2)
plt.show()

# Here the call fig, ax = plt.subplots() returns a pair, where
#
# fig is a Figure instance—like a blank canvas
# ax is an AxesSubplot instance—think of a frame for plotting in
# The plot() function is actually a method of ax

