# SEQUENCIA FIBONACCI
def fibonacci(n, t0 = 1, t1 = 0):
    if n <= 1:
        res = t1
    else:
        res = fibonacci(n-1, t1, t0 + t1)
    return res
