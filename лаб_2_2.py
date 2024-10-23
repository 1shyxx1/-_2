import numpy as np

# Функція f(x)
def f(x):
    return 0.0932*x**4 - 4*x**3 + 4*x**2 - x - 4

# Метод половинного ділення
def bisection_method(a, b, tol=0.0001):
    if f(a) * f(b) >= 0:
        return None
    
    while (b - a) / 2.0 > tol:
        midpoint = (a + b) / 2.0
        if f(midpoint) == 0:
            return midpoint
        elif f(a) * f(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
    return (a + b) / 2.0

# Знаходимо інтервали та застосовуємо метод
def find_intervals():
    intervals = []
    for x in np.arange(-10, 10, 0.5):
        if f(x) * f(x + 0.5) < 0:
            intervals.append((x, x + 0.5))
    return intervals

intervals = find_intervals()
for a, b in intervals:
    root = bisection_method(a, b)
    print(f"Корінь на інтервалі [{a}, {b}] методом половинного ділення: {root}")
