def factorial(n):
    """Calculate the factorial of n."""
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)

def approx_sin(x, n):
    """Approximate the sine function using a Taylor series expansion."""
    result = 0
    for i in range(n):
        term = (-1)**i * x**(2 * i + 1) / factorial(2 * i + 1)
        result += term
    return result

def approx_cos(x, n):
    """Approximate the cosine function using a Taylor series expansion."""
    result = 0
    for i in range(n):
        term = (-1)**i * x**(2 * i) / factorial(2 * i)
        result += term
    return result

def approx_sinh(x, n):
    """Approximate the hyperbolic sine function using a Taylor series expansion."""
    result = 0
    for i in range(n):
        term = x**(2 * i + 1) / factorial(2 * i + 1)
        result += term
    return result

def approx_cosh(x, n):
    """Approximate the hyperbolic cosine function using a Taylor series expansion."""
    result = 0
    for i in range(n):
        term = x**(2 * i) / factorial(2 * i)
        result += term
    return result

# Test Cases
print(f"approx_sin(x = 3.14, n = 10): {approx_sin(3.14, 10)}")
print(f"approx_cos(x = 3.14, n = 10): {approx_cos(3.14, 10)}")
print(f"approx_sinh(x = 3.14, n = 10): {approx_sinh(3.14, 10)}")
print(f"approx_cosh(x = 3.14, n = 10): {approx_cosh(3.14, 10)}")