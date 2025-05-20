def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
    # testy
    assert factorial(0) == 1
    assert factorial(3) == 6
    assert factorial(5) == 120