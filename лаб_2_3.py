def secant_method(a, b, tol=0.0001):
    if f(a) * f(b) >= 0:
        return None
    
    while abs(b - a) > tol:
        a, b = b, b - f(b) * (b - a) / (f(b) - f(a))
    return b

for a, b in intervals:
    root = secant_method(a, b)
    print(f"Корінь на інтервалі [{a}, {b}] методом хорд: {root}")
