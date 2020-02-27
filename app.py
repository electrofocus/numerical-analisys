import math
from integration import trapeze, rectangle, simpson, gauss


def f(x):
    return x * math.exp(x ** 2)


# print(trapeze(0, 2, f, 10000))
# print(rectangle(0, 2, f, 10000))
# print(simpson(0, 2, f, 10000))
# print(gauss(0, 2, f, 100))
