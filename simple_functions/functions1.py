from functools import cache

__all__ = ['my_sum', 'factorial', 'sin']


def my_sum(iterable):
    """Return the sum of the items in iterable."""
    tot = 0
    for i in iterable:
        tot += i
    return tot


@cache
def factorial(n):
    """Return n! (n factorial) for a non-negative integer n."""
    return n * factorial(n-1) if n else 1


def sin(x, terms=20):
    """Approximate sin(x) using a Taylor series with ``terms`` terms."""
    total = 0.0

    for k in range(terms):
        numerator = (-1)**k * x**(2*k + 1)
        denominator = factorial(2*k + 1)
        total += numerator / denominator

    return total
