import math
import numpy as np


def simple(a, b, c_func, d_func, func, delta):
    s = 0

    for x in np.arange(a, b, delta):
        for y in np.arange(c_func(x), d_func(x), delta):
            s += func(x, y) * delta ** 2
    
    return s
