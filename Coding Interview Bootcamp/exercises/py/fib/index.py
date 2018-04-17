# --- Directions
# Print out the n-th entry in the fibonacci series.
# The fibonacci series is an ordering of numbers where
# each number is the sum of the preceeding two.
# For example, the sequence
#  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
# forms the first ten entries of the fibonacci series.
# Example:
#   fib(4) === 3

def memoize(fn):
    cache = {}
    def helper(x):
        if x not in cache:
            cache[x] = fn(x)
        return cache[x]
    return helper

@memoize
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

#memoization decreses rutime from O(2^n) to O(n)
