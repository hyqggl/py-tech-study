#coding=utf-8
"""
The binomial random variable Y∼Bin(n,p)Y∼Bin(n,p) represents the number of successes in nn binary trials, where each trial succeeds with probability pp

Without any import besides from numpy.random import uniform, write a function binomial_rv such that binomial_rv(n, p) generates one draw of YY

Hint: If UU is uniform on (0,1)(0,1) and p∈(0,1)p∈(0,1), then the expression U < p evaluates to True with probability p
"""

from numpy.random import uniform


def binomial_rv(n, p):
    count = 0
    for i in range(n):
        U = uniform()
        if U < p:
            count += 1
    return count

binomial_rv(10, 0.5)