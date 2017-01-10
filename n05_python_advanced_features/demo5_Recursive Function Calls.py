def x_loop(t):
    x = 1
    for i in range(t):
        x = 2 * x
    return x

#OR


def x(t):
    if t == 0:
        return 1
    else:
        return 2 * x(t-1)

