# SEQUENCIA FIBONACCI RECURSIVA

##### PROFESSOR 1
def fib (n) :
    t1 = -1
    t2 = 1
    for i in range (1, n + 1) :
        res = t1 + t2
        t1 = t2
        t2 = res
    return res
#####

###### PROFESSOR 2
def fibR(n):
    if n == 1:
        res = 0
    else:
        if n == 2:
            res = 1
        else:
            res = fibR(n-1) + fibR(n-2)
    return res
#####

##### PROFESSOR 2
def fibR2(n, t1 = 1, res = 0):
    if n > 1:
        res = fibR2 (n-1, res, t1 + res)
    return res
#####


num = int(input("Digite um número positivo: "))
while num<1:
    num = int(input("Digite um número positivo: "))
    
while num>=0:
    r = fib(num)
    print(f"Termo {num} de Fibonacci é {r}")
    num = int(input("Digite um número positivo: "))
    while num == 0:
        num = int(input("Digite um número positivo: "))