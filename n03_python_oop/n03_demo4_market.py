# coding=utf-8
"""
The market consists of the following objects:

A linear demand curve Q=ad−bdpQ=ad−bdp
A linear supply curve Q=az+bz(p−t)Q=az+bz(p−t)
Here

pp is price paid by the consumer, QQ is quantity, and tt is a per unit tax
Other symbols are demand and supply parameters
The class provides methods to compute various values of interest, including competitive equlibrium price and quantity, tax revenue raised, consumer surplus and producer surplus
"""

from __future__ import division
from scipy.integrate import quad

"""
Filename: market.py
Reference: http://quant-econ.net/py/python_oop.html
"""


class Market:
    def __init__(self, ad, bd, az, bz, tax):
        """
        Set up market parameters.  All parameters are scalars.  See
        http://quant-econ.net/py/python_oop.html for interpretation.

        """
        self.ad, self.bd, self.az, self.bz, self.tax = ad, bd, az, bz, tax
        if ad < az:
            raise ValueError('Insufficient demand.')

    def price(self):
        "Return equilibrium price"
        return (self.ad - self.az + self.bz * self.tax) / (self.bd + self.bz)

    def quantity(self):
        "Compute equilibrium quantity"
        return self.ad - self.bd * self.price()

    def consumer_surp(self):
        "Compute consumer surplus"
        # == Compute area under inverse demand function == #
        integrand = lambda x: (self.ad / self.bd) - (1 / self.bd) * x
        area, error = quad(integrand, 0, self.quantity())
        return area - self.price() * self.quantity()

    def producer_surp(self):
        "Compute producer surplus"
        #  == Compute area above inverse supply curve, excluding tax == #
        integrand = lambda x: -(self.az / self.bz) + (1 / self.bz) * x
        area, error = quad(integrand, 0, self.quantity())
        return (self.price() - self.tax) * self.quantity() - area

    def taxrev(self):
        "Compute tax revenue"
        return self.tax * self.quantity()

    def inverse_demand(self, x):
        "Compute inverse demand"
        return self.ad / self.bd - (1 / self.bd) * x

    def inverse_supply(self, x):
        "Compute inverse supply curve"
        return -(self.az / self.bz) + (1 / self.bz) * x + self.tax

    def inverse_supply_no_tax(self, x):
        "Compute inverse supply curve without tax"
        return -(self.az / self.bz) + (1 / self.bz) * x


baseline_params = 15, .5, -2, .5, 3
m = Market(*baseline_params)
print "equilibrium price = ", m.price()
print "consumer surplus = ", m.consumer_surp()
