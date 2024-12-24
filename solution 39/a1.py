factorial_lambda = lambda n: 1 if n == 0 else n * factorial_lambda(n - 1)

# Example usage:
print(factorial_lambda(5))