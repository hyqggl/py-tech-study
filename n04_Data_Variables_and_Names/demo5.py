def f(x):
    x += 1
    return x

x = 1
print(f(x), x)


def f2(x):
    x[0] += 1
    return x

x = [1]
print(f2(x), x)