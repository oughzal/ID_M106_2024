from math import sqrt,sin
def f(x):
    return sqrt(x**2 - 2*sin(x+4))/x**3
print(f(1))