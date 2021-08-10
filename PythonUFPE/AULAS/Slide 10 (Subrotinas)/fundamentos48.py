def quebra_numero(num):
    algs = [-1] * 4
    i = 0
    while num != 0:
            algs[i] = num % 10
            num //= 10
            i += 1
    

    return algs

def palindromo(num):
    algs = quebra_numero(num)
    valor = 0
    i = 0
    while (i < 4) and (algs[i] != -1):
        valor = valor * 10 + algs[i]
        i += 1

    if num == valor:
        return True
    else:
        return False


for i in range(100, 5001):
    if palindromo(i):
        print(i)