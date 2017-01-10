singular = ('dog', 'cat', 'bird')
print type(singular)
plural = [string + 's' for string in singular]
print plural
print type(plural)

# Generator Functions
def f():
    yield 'start'
    yield 'middle'
    yield 'end'

gen = f()
print next(gen)
print next(gen)
print next(gen)
print next(gen) #STOP


def g(x):
    while x < 100:
        yield x
        x = x * x

gen = g(2)
next(gen)
next(gen)
next(gen)
next(gen)

