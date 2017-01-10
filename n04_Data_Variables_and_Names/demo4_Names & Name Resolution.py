import math


def f(string):
    print(string)

g = f
print id(g) == id(f)
g('test')

# Viewing Namespaces
print vars(math)
print dir(math)
print math.__doc__
print math.__name__

print dir(__builtins__)
print __builtins__.max
