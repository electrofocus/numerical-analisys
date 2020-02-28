import math
import integral
import multiple_integral


def f(x):
    return x * math.exp(x ** 2)


# print(trapeze(0, 2, f, 10000))
# print(rectangle(0, 2, f, 10000))
# print(simpson(0, 2, f, 10000))
# print(gauss(0, 2, f, 100))

def c(x):
    return x ** 2


def d(x):
    return 1


def f_2(x, y):
    return x ** 2 + x * y + y ** 2


# print(simple(-1, 1, c, d, f_2, 0.001))
