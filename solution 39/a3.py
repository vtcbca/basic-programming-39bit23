def fibonacci_memoization(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoization(n-1, memo) + fibonacci_memoization(n-2, memo)
    return memo[n]

def get_fib_sequence(n):
    return [fibonacci_memoization(i) for i in range(n)]

# Example usage:
print(get_fib_sequence(10)) 