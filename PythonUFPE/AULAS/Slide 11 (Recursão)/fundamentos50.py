#FATORIAL SEM RECURSAO
def fatorial(num):
    f = 1
    for i in range(2, num+1):
        f *= i
    return f

num = int(input("DIgite um número: "))
print(fatorial(num))

