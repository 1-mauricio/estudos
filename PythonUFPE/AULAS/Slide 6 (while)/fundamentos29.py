# Ler um número inteiro e dizer se ele é primo ou não.

import math

n = int(input("Digite um número inteiro maior ou igual a 1: "))
while n <= 0:
    n = int(input("Digite um número inteiro maior ou igual a 1: "))

i = 2
raiz=int(math.sqrt(n))
while (i < raiz) and  (n % i != 0):
    i += 1

if i == raiz+1:
    print(f"O número {n} é primo")
else:
    print(f"O número {n} não é primo")
