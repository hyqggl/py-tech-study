def var(y):
    n = len(y)
    assert n > 1, 'Sample size must be greater than one.'
    return np.sum((y - y.mean()) ** 2) / float(n - 1)

# print var([1])


def f(x):
    try:
        return 1.0 / x
    except ZeroDivisionError:
        print('Error: Division by zero.  Returned None')
    except TypeError:
        print('Error: Unsupported operation.  Returned None')
    return None

print f(0)


def f2(x):
    try:
        return 1.0 / x
    except (TypeError, ZeroDivisionError):
        print('Error: Unsupported operation.  Returned None')
    return None


def f3(x):
    try:
        return 1.0 / x
    except:
        print('Error.  Returned None')
    return None
