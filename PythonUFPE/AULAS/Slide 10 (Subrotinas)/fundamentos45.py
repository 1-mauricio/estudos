import math

def primo(num):
    raiz = int(math.sqrt(num))
    i = 2
    while (i <= raiz) and ((num % i) != 0):
        i += 1

    if i > raiz:
        return True
    else:
        return False


print(primo(8))