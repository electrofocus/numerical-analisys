import math
import numpy as np
import matplotlib.pyplot as plt


def euler(a, b, func, n, y_init):
    args = np.linspace(a, b, n)
    vals = [0] * n
    vals[0] = y_init
    h = abs(b - a) / n
    for i in range(n - 1):
        vals[i + 1] = vals[i] + func(args[i], vals[i]) * h
    
    return args, vals


def runge(a, b, func, n, y_init):
    args = np.linspace(a, b, n)
    vals = [0] * n
    vals[0] = y_init
    h = abs(b - a) / n
    for i in range(n - 1):
        k = func(args[i], vals[i]) * h
        vals[i + 1] = vals[i] + func(args[i] + h / 2, vals[i] + k / 2) * h
    
    return args, vals
