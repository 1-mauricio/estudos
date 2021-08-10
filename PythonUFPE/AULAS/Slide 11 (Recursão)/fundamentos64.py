def fib(n):
    if n==1 or n==2:
        return n-1

    return fib(n-1) + fib(n-2)

def fib_c(n):
    if n==1 or n==2:
        return 0

    return 2 + fib_c(n-1) + fib_c(n-2)


def fib2_c(n, t1=1, res=0):
    if n>1:
        return 1 + fib2_c(n-1, res, t1+res)
    else:
        return 0

print(fib_c(30))
print(fib2_c(30))