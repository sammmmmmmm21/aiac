def factr(n):
    # Ensure n is an integer
    if isinstance(n, str):
        n = int(n)
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factr(n - 1)

print(factr(5))