# Ler um número inteiro e dizer se ele é primo ou não.

n = int(input("Digite um número inteiro maior ou igual a 1: "))
while n <= 0:
    n = int(input("Digite um número inteiro maior ou igual a 1: "))

i = 2
while (i < n) and  (n % i != 0):
    i += 1

if n == i:
    print(f"O número {n} é primo")
else:
    print(f"O número {n} não é primo")
