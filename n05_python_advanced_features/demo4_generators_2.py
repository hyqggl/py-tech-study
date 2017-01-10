import random


def f(n):
    i = 1
    while i <= n:
        yield random.uniform(0, 1) < 0.5
        i += 1

n = 10000000
draws = f(n)
sum(draws)
