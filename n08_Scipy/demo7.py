from scipy.optimize import fminbound
from scipy.integrate import quad


print fminbound(lambda x: x**2, -1, 2)
integral, error = quad(lambda x: x**2, 0, 1)
print integral