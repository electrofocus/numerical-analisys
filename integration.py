import math
import numpy as np


def trapeze(a, b, func, n=100):
    def coeff(n):
        yield 0.5
        for i in range(n - 1):
            yield 1
        yield 0.5

    x = a
    h = abs(b - a) / n
    s = 0

    for c in coeff(n):
        s += c * func(x)
        x += h

    return s * h


def rectangle(a, b, func, n = 100):
    # c === 1
    h = abs(b - a) / n
    s = 0

    for x in np.linspace(a, b, n + 1):
        s += func(x)

    return s * h


def simpson(a, b, func, n = 100):

    # gives 1, 4, 2, 4, ..., 2, 4, 1

    def coeff(n):
        yield 1
        for i in range(n - 1):
            yield (4, 2)[i % 2]
        yield 1
    

    x = a
    h = abs(b - a) / n
    s = 0

    for c in coeff(n):
        s += c * func(x)
        x += h
    
    return s * (h / 6) * 2


def gauss(a, b, func, n = 100):
    h = abs(b - a) / n
    h_2 = h / 2
    h_3 = h / (2 * math.sqrt(3))
    vals = list()

    for x in np.linspace(a, b, n + 1):
        vals.append(func(x + h_2 - h_3) + func(x + h_2 + h_3))

    return sum(vals[1:-1]) * h_2
