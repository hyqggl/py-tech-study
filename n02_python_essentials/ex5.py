# coding=utf-8
"""
When we cover the numerical libraries, we will see they include many alternatives for interpolation and function approximation

Nevertheless, let’s write our own function approximation routine as an exercise

In particular, without using any imports, write a function linapprox that takes as arguments

A function f mapping some interval [a,b][a,b] into ℝR
two scalars a and b providing the limits of this interval
An integer n determining the number of grid points
A number x satisfying a <= x <= b
and returns the piecewise linear interpolation of f at x, based on n evenly spaced grid points a = point[0] < point[1] < ... < point[n-1] = b

Aim for clarity, not efficiency
"""

def linapprox(f, a, b, n, x):
    """
    Evaluates the piecewise linear interpolant of f at x on the interval
    [a, b], with n evenly spaced grid points.

    Parameters
    ===========
        f : function
            The function to approximate

        x, a, b : scalars (floats or integers)
            Evaluation point and endpoints, with a <= x <= b

        n : integer
            Number of grid points

    Returns
    =========
        A float. The interpolant evaluated at x

    """
    length_of_interval = b - a
    num_subintervals = n - 1
    step = length_of_interval / num_subintervals

    # === find first grid point larger than x === #
    point = a
    while point <= x:
        point += step

    # === x must lie between the gridpoints (point - step) and point === #
    u, v = point - step, point

    return f(u) + (x - u) * (f(v) - f(u)) / (v - u)