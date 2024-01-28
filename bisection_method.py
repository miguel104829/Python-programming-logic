def bisection_method(f, a, b, tolerance):
    """
    Implements the bisection method to find the root of a function f within the interval [a, b].
    Returns the approximate root.
    """
    if f(a) * f(b) >= 0:
        raise ValueError("Function values at interval endpoints must have opposite signs.")

    while abs(b - a) > tolerance:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2

# Example usage:
def f(x):
    return -(1/10)*x**2 + 3

root = bisection_method(f, 1, 7, 0.001)
print("Approximate root:", root)